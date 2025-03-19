import requests
import json
import os
import sqlalchemy
import pandas as pd

class DocHelper:
    def __init__(self, datasource, dataset, version, filepath):
        '''
        
        Parameters
        ----------
        datasource : str
            data source of target table/dataset
        dataset : str
            dataset/table name of target table/dataset
        version : str
            version number of target table/dataset
        filepath : str
            filepath of py scripts and NHS pid lookups

        Returns
        -------
        None.

        '''
        # define std input variables
        self.data = dataset
        self.source = datasource
        self.version = version
        self.fp = filepath 
        # get all the pid ids need these available for every instance 
        self.pids = self.load_pids()
        # get single pid for this instance
        self.pid = self.get_pid()
        # get api data
        self.api_data = self.get_api_data() 
        # open DB connection
        #self.cnxn = self.connect()
        # ukllc api connection
        self.api_key = os.environ['FASTAPI_KEY']

        
    def load_pids(self):
        '''
        
        Uses json of HDRUK provided persistent ids (dataset level)

        Returns
        -------
        newpids : list
            persistent IDs for all available NHS datasets available via API

        '''
        
        pid_loc = self.fp + 'datasets_pids_lookup.json'
        with open(pid_loc, "r") as f:
            pids = json.load(f)
        return pids
    
    
    def get_pid(self):
        '''
        
        Returns
        -------
        pid : str
            persistent ID retreived from pid:shortname lookup   

        '''
        
        # deal with multi tables where 1 API record but more than 1 table
        multi = ['IAPT', 'CSDS']
        if any(i in self.data for i in multi):
            datamain = self.data[:4]
        else:
            datamain = self.data
            
        for pid, ds_name in self.pids.items():
            if ds_name == datamain:
                return(pid)
            
                
    def get_api_data(self):
        '''
        
        Returns
        -------
        metadata : dict
            metdata json/dictionary for target dataset

        '''
        # define URL and add persistent ID of target dataset
        url = "https://api.www.healthdatagateway.org/api/v1/datasets/"+self.pid
        # make request 
        response = requests.get(url)
        # get data as text
        data = response.text
        # convert to json and return 
        metadata = json.loads(data)
        return(metadata['data'])
    

    def connect(self):
        '''
        
        Raises
        ------
        Exception
            Database connection failure

        Returns
        -------
        cnxn : database connection
            connection to heroku database with metrics

        '''
        # attempt db connection
        try:
            db_str = os.environ['DATABASE_URL'].replace("postgres", "postgresql+psycopg2", 1)
            cnxn = sqlalchemy.create_engine(db_str)
            return(cnxn)
        # raise exception if connection failure
        except Exception as e:
            raise Exception("DB connection failed with error", e)
            
    
    def get_cohort_count(self):
        '''

        Returns
        -------
        cnt : df
            dataframe containing counts of participants by LPS

        '''

        # get data from api endpoint
        url = "https://metadata-api-4a09f2833a54.herokuapp.com/nhs-dataset-counts/?table={}".format(self.data)
        r = requests.get(url, headers={'access_token': self.api_key}) 
        data = r.text
        # convert to json
        pj = json.loads(data)
        # convert to dataframe
        df = pd.json_normalize(pj)
        
        # remove cohorts not included
        rm = ['GENSCOT', 'NICOLA', 'SABRE']
        df = df[~df['cohort'].isin(rm)]
        
        # strip down df and rename
        df = df[['cohort', 'count']].rename(columns={'cohort': 'LPS',
                                'count': 'Participant count'})
    
        # CALC TOTAL
        # treat <10 as 0
        df['count1'] = df['Participant count'].replace('<10', '0')
        # convert to ensure counts are numeric
        df['count1'] = df['count1'].astype(int)
        # get total        
        df.loc["Total"] = df['count1'].sum()
        # drop temp column
        df = df.drop(columns = ['count1'])
        # sort index and total naming
        df = df.reset_index(drop = True)
        df.loc[df.index[-1], 'LPS'] = 'TOTAL'
        return df
    
    
    def get_dataset_info(self):
        '''

        Returns
        -------
        dfm : dataframe
            retrieved data from multiple endpoints of UK LLC metadata API and creating summary table

        '''

        # get observation and row counts from versions endpoint
        # IAPT and CSDS being multi part tables need skipping via dummy dfs
        multi = ['IAPT', 'CSDS']
        if any(i in self.data for i in multi):
            # create dummy dataframe
            df1 = pd.DataFrame()
        else:
            # get observation and row counts from versions endpoint
            url1 = "https://metadata-api-4a09f2833a54.herokuapp.com/all-datasets-versions/?source={}&table={}".format(self.source, self.data)
            r1 = requests.get(url1, headers={'access_token': self.api_key }) 
            data1 = r1.text
            # convert to json
            pj1 = json.loads(data1)
            # convert to dataframe
            df1 = pd.json_normalize(pj1)
            # dedup keeping latest
            df1 = df1.sort_values('version_num').drop_duplicates('table', keep='last')
            # keep only select columns
            to_keep = ['num_columns', 'num_rows']
            df1 = df1[to_keep]
            df1['num_columns'] = df1['num_columns'].astype(int)
            df1['num_rows'] = df1['num_rows'].astype(int)
            # rename
            df1 = df1.rename(columns={'num_columns': 'Number of variables',
                                    'num_rows': 'Number of observations'})
            # transpose and rename columns
            df1 = df1.T
            df1 = df1.rename(columns = {df1.columns[0] : 'Dataset-specific information'})
        
        # guidebook specific table/endpoint
        multipart = ['IAPT_', 'CSDS_']
        if any(i in self.data for i in multipart):
            # create dummy dataframe
            df2 = pd.DataFrame()
        else:
            url2 = "https://metadata-api-4a09f2833a54.herokuapp.com/nhs-datasets-gb/?Name_of_dataset_in_TRE={}".format(self.data)
            r2 = requests.get(url2, headers={'access_token': self.api_key }) 
            data2 = r2.text
            # convert to json
            pj2 = json.loads(data2)
            # convert to dataframe
            df2 = pd.json_normalize(pj2)
            # shift dataset name to first place
            col_ord = ['Name_of_dataset_in_TRE', 'Other_name', 'Temporal_coverage', 'TRE_temporal_coverage']
            df2 = df2[col_ord + [col for col in df2.columns if col not in col_ord]]
            # transpose and rename columns
            df2 = df2.T
            df2 = df2.rename(columns = {df2.columns[0] : 'Dataset-specific information'})
        # need to merge 2 dataframe to get complete picture
        dfm = pd.concat([df2, df1])

        # get total count of participants in each dataset
        if any(i in self.data for i in multi):
            # create dummy dataframe
            df3 = pd.DataFrame()
        else:
            df3 = self.get_cohort_count()
            df3 = df3[df3['LPS'] == 'TOTAL'].drop('LPS', axis=1)
            # and transpose
            df3 = df3.T
            df3 = df3.rename(columns = {df3.columns[0] : 'Dataset-specific information'})
        # and merge
        dfm = pd.concat([dfm, df3])
            
        # End point for latest extract
        if any(i in self.data for i in multi):
            # create dummy dataframe
            df4 = pd.DataFrame()
        else:
            url4 = "https://metadata-api-4a09f2833a54.herokuapp.com/nhs-extract-dates/"
            r4 = requests.get(url4, headers={'access_token': self.api_key }) 
            data4 = r4.text
            # convert to json
            pj4 = json.loads(data4)
            # convert to dataframe
            df4 = pd.json_normalize(pj4)
            # dedup keeping latest and filter to target dataset
            df4 = df4[df4['dataset'].str.contains(self.data)].sort_values('date').drop_duplicates('dataset', keep='last')
            df4 = df4[['date']]
            # rename 
            df4 = df4.rename(columns={'date': 'Date of last extract'})
            # and transpose
            df4 = df4.T
            df4 = df4.rename(columns = {df4.columns[0] : 'Dataset-specific information'})
        # and merge
        dfm = pd.concat([dfm, df4])
        
        # FINAL CLEARUP
        dfm = dfm.reset_index()
        dfm = dfm.rename(columns = {'index' : 'Dataset descriptor'})
        dfm = dfm.reset_index(drop = True)
        dfm['Dataset descriptor'] = dfm['Dataset descriptor'].str.replace('_', ' ')  
        return dfm
    

    def style_table(self, df):
        '''

        Parameters
        ----------
        df : dataframe
            df to be styled

        Returns
        -------
        df : dataframe
            df with styling applied 

        '''
        
        # apply styling 
        df = df.style.set_table_attributes('style="font-size: 14px"')\
        .set_table_styles([dict(selector='th', props=[('text-align', 'left'),])])\
        .set_properties(**{'text-align': 'left'})
        # LPS tables
        if 'LPS' in df.columns:
            df.set_properties(subset = ['LPS'], **{'font-weight' : 'bold'})\
            .set_properties(subset = df.index[-1], **{'font-weight' : 'bold'})
        # hide index as don't want to display
        df.hide()
        return df



    
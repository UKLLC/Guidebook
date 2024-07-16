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
            #db_str = os.environ['CLEARDB_DATABASE_URL'].replace("mysql", "mysql+pymysql", 1).replace('?reconnect=true', '', 1)

            # need to swap password for local var
            #cnxn = sqlalchemy.create_engine('***REMOVED***')
            cnxn = sqlalchemy.create_engine('***REMOVED***')
            return(cnxn)
        # raise exception if connection failure
        except Exception as e:
            raise Exception("DB connection failed with error", e)
            
    # def get_extract_count(self):
    #     '''

    #     Returns
    #     -------
    #     extract_cnt : df
    #         dataframe containing counts of records by extract dates

    #     '''
    #     # build query
    #     q = '''SELECT date as extract_date, count
    #     FROM heroku_9146b3bcb7a2912.nhs_dataset_extracts
    #     where dataset = '{}_{}'
    #     order by date;'''.format(self.data, self.version)
    #     # pull data from database and return
    #     extract_cnt = pd.read_sql(q, self.cnxn)
    #     return extract_cnt
    
    def get_cohort_count(self):
        '''

        Returns
        -------
        cnt : df
            dataframe containing counts of participants by LPS

        '''

        # build query (like used to pickup reg dataset which have date)
        q = '''
        SELECT cohort, count
        FROM nhs_dataset_cohort_linkage
        where dataset like '{}_{}%%'
        and cohort not in ('GENSCOT', 'NICOLA', 'SABRE')
        order by cohort;'''.format(self.data, self.version)
        # pull data from database and return
        cnxn = self.connect()
        cnt = pd.read_sql(q, cnxn)
        # treat <10 as 0
        cnt['count1'] = cnt['count'].replace('<10', '0')
        # convert to ensure counts are numeric
        cnt['count1'] = cnt['count1'].astype(int)
        # get total
        total = cnt.sum(numeric_only = True).iloc[0]
        # drop temp column
        cnt = cnt.drop(columns = ['count1'])
        # add total to df and return
        cnt.loc[len(cnt)] = ['total', total]
        return cnt
    
    def get_dataset_info(self):
        '''

        Returns
        -------
        cnt : df
            dataframe containing counts of participants by LPS

        '''

        # build query (like used to pickup reg dataset which have date)
        q = '''
            SELECT * FROM nhs_england_datasets_info 
            where "Name of dataset in TRE" = \'{}\''''.format(self.data)

        # pull data from database and return
        cnxn = self.connect()

        df = pd.read_sql(q, cnxn)
        
        return df
    

if __name__ == "__main__":
    schema = 'nhsd'
    table = 'HESOP'
    version = 'v0002'
    # import functions from script helper
    import sys
    script_fp = ""
    helper = DocHelper(schema, table, version, script_fp)
    df = helper.get_dataset_info()


    helper.get_cohort_count()
    

    
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
        self.cnxn = self.connect()

        
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
        for pid, ds_name in self.pids.items():
            if ds_name == self.data:
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
            db_str = os.environ['CLEARDB_DATABASE_URL'].replace("mysql", "mysql+pymysql", 1).replace('?reconnect=true', '', 1)
            cnxn = sqlalchemy.create_engine(db_str, pool_recycle=300).connect()
            return cnxn
        # raise exception if connection failure
        except Exception as e:
            print("Connection to database failed, retrying.")
            raise Exception("DB connection failed")
            
    def get_extract_count(self):
        '''

        Returns
        -------
        extract_cnt : df
            dataframe containing counts of records by extract dates

        '''
        # build query
        q = '''SELECT date as extract_date, count
        FROM heroku_9146b3bcb7a2912.nhs_dataset_extracts
        where dataset = '{}_{}'
        order by date;'''.format(self.data, self.version)
        # pull data from database and return
        extract_cnt = pd.read_sql(q, self.cnxn)
        return extract_cnt
    
    def get_cohort_count(self):
        '''

        Returns
        -------
        cnt : df
            dataframe containing counts of participants by LPS

        '''
        # build query
        q = '''SELECT cohort, count
        FROM heroku_9146b3bcb7a2912.nhs_dataset_cohort_linkage
        where dataset = '{}_{}'
        and cohort not in ('GENSCOT', 'NICOLA', 'SABRE')
        order by cohort;'''.format(self.data, self.version)
        # pull data from database and return
        cnt = pd.read_sql(q, self.cnxn)
        # convert to ensure counts are numeric
        cnt['count'] = cnt['count'].astype(int)
        # get total
        total = cnt.sum(numeric_only = True).iloc[0]
        # add total to df and return
        cnt.loc[len(cnt)] = ['total', total]
        return cnt
    
    
#temp - DELETE THIS ONCE DB HAS BEEN UPDATED AND ALL WORKING
# schema = 'nhsd'
# table = 'HESAPC'
# version = 'v0002'
# fp = 'C:/Users/rt17581/OneDrive - University of Bristol/MyFiles-Migrated/Documents/github/jupyter-book/ukllc_book/docs/scripts/'

# t1 = DocHelper(schema, table, version, fp)
# cnxn = t1.connect()
# t4 = t1.get_extract_count()
# t5 = t1.get_cohort_count()

# q = '''SELECT * FROM heroku_9146b3bcb7a2912.nhs_dataset_cohort_linkage
# where dataset_stem like 'HESAPC'
# and cohort not in ('GENSCOT', 'NICOLA', 'SABRE')'''
# t1 = pd.read_sql(q, cnxn)

# q = '''SELECT * FROM heroku_9146b3bcb7a2912.nhs_dataset_extracts
# '''
# t2 = pd.read_sql(q, cnxn)



    

    
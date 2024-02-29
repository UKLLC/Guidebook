import requests
import json

class DocHelper:
    def __init__(self, datasource, dataset, version, filepath):
        '''
        
        Parameters
        ----------
        datasource : str
            data source of target table/dataset
        dataset : TYPE
            dataset/table name of target table/dataset
        version : TYPE
            version number of target table/dataset

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
        
    def load_pids(self):
        '''
        Uses json of HDRUK provided persistent ids (dataset level)

        Returns
        -------
        newpids : list
            persistent IDs for all available NHS datasets available via API

        '''
        #pid_loc = pathlib.Path(sys.argv[0]).parent / 'datasets_pids_lookup.json'
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

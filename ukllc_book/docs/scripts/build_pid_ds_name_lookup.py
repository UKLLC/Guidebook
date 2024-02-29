import requests
import json
import sys
import pathlib


def load_pids():
    '''
    Uses json of HDRUK provided persistent ids (dataset level)

    Returns
    -------
    newpids : list
        persistent IDs for all available NHS datasets available via API

    '''
    pid_loc = pathlib.Path(sys.argv[0]).parent / 'dataset_pids_nhs-d.json'
    with open(pid_loc, "r") as f:
        pids = json.load(f)
    # new list
    newpids = []
    for i in pids:
        pids2 = list(i.values())[0]
        newpids.append(pids2)
    return newpids

def load_json(pid):
    '''
    
    Parameters
    ----------
    pid : str
        persistent ID to identify NHS datasets

    Returns
    -------
    pj : dict
        json data retrieved from HDRUK NHS API

    '''
    url = "https://api.www.healthdatagateway.org/api/v1/datasets/"+pid
    response = requests.get(url)
    # get data as text
    data = response.text
    # convert to json
    pj = json.loads(data)
    return(pj)

def match_dataset_id(pids, js):
    '''
    
    Parameters
    ----------
    pids : list
        of all pids
    js : dict
        json metadata 
    
    Returns
    -------
    js : dict
        lookup of pid to full dataset name
        

    '''
    # switch keys
    for i in list(pids):
        # get pid new name
        new_value = js[i]['data']['name']
        # reorg dict
        js.update({i : new_value})
    return(js)
    
def match_nhs_shortname(datasets):
    '''
    Parameters
    ----------
    datasets : dict
        of all pids to NHS long name to be switched to shortname
    
    Returns
    -------
    datasets_fil : dict
        stripped down dict to only datasets LLC hold eith pid and shortname

    '''
    # lookup long to short names of all datasets LLC hold
    nhs_ds_name_lookup = {
        'Cancer Registration Data' : 'CANCER',
        'COVID-19 SARI-Watch (formerly CHESS)' : 'CHESS',
        'Medicines dispensed in Primary Care (NHSBSA data)' : 'PCM',
        'Improving Access to Psychological Therapies Data Set' : 'IAPT',
        'Community Services Data Set' : 'CSDS',
        'Civil Registration - Deaths' : 'MORTALITY',
        'Hospital Episode Statistics Accident and Emergency' : 'HESAE',
        'COVID-19 Vaccination Status' : 'CVS',
        'COVID-19 Vaccination Adverse Reaction' : 'CVAR',
        'Covid-19 UK Non-hospital Antibody Testing Results' : 'IELISA',
        # NPEX matched by process of elimination - keep under review
        'Covid-19 UK Non-hospital Antigen Testing Results' : 'NPEX',
        'Hospital Episode Statistics Admitted Patient Care' : 'HESAPC',
        'Hospital Episode Statistics Critical Care' : 'HESCC',
        'Hospital Episode Statistics Outpatients' : 'HESOP',
        'Covid-19 Second Generation Surveillance System' : 'COVIDSGSS',
        'Emergency Care Data Set (ECDS)' : 'ECDS',
        'GPES Data for Pandemic Planning and Research (COVID-19)' : 'GDPPR',
        'Mental Health Minimum Dataset v4.1 (Non-Sensitive) Episodes' : 'MHSDS'
        #'Mental Health Minimum Data Set' : 'MHSDS'
        }    
    # switch keys and values
    datasets = {v : k for k, v in datasets.items()}
    # convert lookup to set
    lookup_set = set(nhs_ds_name_lookup.keys())
    # switch
    datasets_fil = {datasets[k]:nhs_ds_name_lookup[k] for k in lookup_set}
    return(datasets_fil)

def main():
    # load pids
    pids = load_pids()
    # empty d
    d = {}
    # load json
    for i in pids:
        d[i] = load_json(i)
    # switch keys for long name
    d2 = match_dataset_id(pids, d)
    # switch long name for short name - MOD JUST NEED MATCH TO PID NOT WHOLE API md
    d3 = match_nhs_shortname(d2)
    # run function to write json to wd
    with open('datasets_pids_lookup.json', 'w') as fp:
        json.dump(d3, fp)
        
# run main
if __name__ == "__main__":
    main()

import json

def read_config(config_file_name):
    '''
    Read a JSON config file in the current directory, return JSON
    :param config_file_name: 
    :return: 
    '''
    with open(config_file_name) as f:
        config = json.load(f)
    return config

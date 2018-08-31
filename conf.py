"""
this is a conf reader

conf_reader responsibilities:
    read the conf
    take the values from the conf and put them in the right places
    anything going wrong means default for that value

conf format is json
"""

class app_conf:
    conf = {
        "configuration_path": "./conf/econ-sim-conf.json",
        "worldfile_path": "./worldfiles/test-worldfile.json",
        "max_world_size": "359"
    }
    

class conf_reader:
    
    def __init__(self):
        
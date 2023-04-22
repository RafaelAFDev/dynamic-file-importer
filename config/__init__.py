import json
import os

def read_config(configfile):
    if os.path.exists(configfile):
        f = open(configfile, encoding='utf-8')
        conf = json.load(f)
        f.close()
        return conf
    else:
        raise Exception('O arquivo de configuração definido não existe: ' + str(configfile))

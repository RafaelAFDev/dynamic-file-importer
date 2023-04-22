from argparse import ArgumentParser
import sys
import config
import filehandler

def main():
    global _CONFIG
    FH = filehandler.FileHandler(_CONFIG)
    rows = FH.import_files()

    return rows

if __name__ == '__main__':
    argParser = ArgumentParser('Dynamic File Handler - By Rafael Alves Ferreira - 2023')
    argParser.add_argument('--config', help='Define o caminho do arquivo json de configuração', required=True)
    _params = argParser.parse_args()
    _CONFIG = config.read_config(configfile=_params.config)
    
    rows = main()
    
    try:
        sys.stdout.write(str(rows))
        sys.stdout.flush()
        sys.exit(0x00)
        
    except Exception as error:
        exc_type, value, traceback = sys.exc_info()
        errmessage = "Failed: [%s] " % exc_type.__name__ + str(error)[:255]
        sys.stdout.write(errmessage)
        sys.stdout.flush()
        sys.exit(0x01)
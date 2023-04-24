import polars as pl
import glob
import os
import zipfile

class FileHandler():
    
    def __init__(self, _CONFIG):
        self._CONFIG = _CONFIG
        self.files = []
        self.get_files()
    
    def get_files(self):
        self.files = []
        for file in self._CONFIG['files']:
            list_paths = []
            list_paths = glob.glob(self._CONFIG['files'][file]['path'])
            
            if len(list_paths) == 0 and self._CONFIG['files'][file]['file_required'] == 'yes':
                raise Exception('Arquivo não localizado: ' + self._CONFIG['files'][file]['path'])
            else:
                for path in list_paths:
                    path_data = []
                    path_data.append(file)
                    path_data.append(path)
                    self.files.append(path_data)
        
    def import_files(self):
        rows = 0
        for file in self.files:
            self.df = pl.DataFrame()
            
            if file[1][-4:] in ['.csv', '.txt'] : self.read_csv(file)
            elif file[1][-5:] == '.json': self.read_json(file)
            elif file[1][-5:] in ['.xlsx', '.xlsm', '.xlsb']: self.read_excel(file)
            else: raise Exception('O formato do arquivo especificado não é suportado.')

            self.df = self.df.select(list(self._CONFIG['files'][file[0]]['fields'].keys()))
            self.df = self.df.rename(self._CONFIG['files'][file[0]]['fields'])
            if self._CONFIG['files'][file[0]]['skip_footer'] > 0:
                self.df = self.df[0:len(self.df)-self._CONFIG['files'][file[0]]['skip_footer']]
            
            r = len(self.df)
            rows += r
            if r > 0:
                self.df.write_database(
                     table_name=self._CONFIG['files'][file[0]]['target_table']
                    ,connection_uri=self._CONFIG['conn_string']
                    ,if_exists='append'
                    ,engine='sqlalchemy'

                )
                if self._CONFIG['files'][file[0]].get('delete_file', None):
                    self.delete_file(file)
                elif self._CONFIG['files'][file[0]].get('move_file', None):
                    self.move_file(file)
                    
        return rows

    def read_csv(self, file):
        self.df = pl.read_csv(
             source=file[1]
            ,separator=self._CONFIG['files'][file[0]]['separator']
            ,quote_char=self._CONFIG['files'][file[0]]['quote_char']
            ,skip_rows=self._CONFIG['files'][file[0]]['skip_header']
            ,encoding=self._CONFIG['files'][file[0]]['encoding']
        )
        
    def read_excel(self, file):
        self.df = pl.read_excel(
             source=file[1]
            ,sheet_name=self._CONFIG['files'][file[0]]['sheet_name']
        )
    
    def read_json(self, file):
        self.df = pl.read_json(source=file[1])

    def delete_file(self, file):
        os.remove(file[1])
    
    def move_file(self, file):
        path = self._CONFIG['files'][file[0]]['move_file']
        f = file[1].split('\\')
        f = f[len(f)-1]

        if not os.path.exists(path):
            os.makedirs(path)

        zp = zipfile.ZipFile(path+f+'.zip', 'w', zipfile.ZIP_DEFLATED)
        zp.write(file[1])
        zp.close()
        
        self.delete_file(file)

from mlproject.entity.config_entity import DataValidationConfig
import os
import pandas as pd
from mlproject import logger



class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
        

            all_schema = self.config.all_schema.keys()
            l1 = list(all_cols)
            l2 = list(all_schema)
            

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f" validation status { validation_status}")
                    
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f" validation status { validation_status}")
        
            return validation_status

        except Exception as e:
            raise e
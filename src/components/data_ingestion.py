import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import custom_exception
from dataclasses import dataclass

@dataclass
class data_ingestion_config:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')

class data_ingestion:
    def __init__(self):
        self.ingestion_config = data_ingestion_config()

    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        try:
            df = pd.read_csv(os.path.join('notebooks/data','text.csv'))
            logging.info("dataset read as pandas dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path))
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            df.to_csv(self.ingestion_config.train_data_path, index=False)
            df.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("train test split")

            train_set , test_set = train_test_split(df, test_size=0.2, Random_stae=42)
            logging.info("data ingestion completed")

            return (
                self.ingestion.train_data_path,
                self.ingesiton.test_data_path
            )
        
        except Exception as e:
            logging.info("Error occured in data ingestion config")
            raise custom_exception(e, sys)
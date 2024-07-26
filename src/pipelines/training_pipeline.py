import os
import sys
from src.logger import logging
from src.exception import custom_exception
from src.components.data_ingestion import data_ingestion

if __name__ == "__main__":
    try:
        obj = data_ingestion()
        train_data_path, test_data_path = obj.initiate_data_ingestion()
    except custom_exception as e:
        logging.info(e)
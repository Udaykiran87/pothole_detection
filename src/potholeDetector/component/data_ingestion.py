import os  # Import the os module
import urllib.request as request  # Import the request module from urllib
import zipfile  # Import the zipfile module
from potholeDetector import logger  # Import the logger module from potholeDetector
from potholeDetector.utils.common import *  # Import common utilities module
from potholeDetector.entity.config_entity import DataIngestionConfig  # Import DataIngestionConfig entity class
from pathlib import Path  # Import the Path class from pathlib


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """    def extract_zip_file(self):
        """
        """
        Initializes the DataIngestion class.

        Args:
            config (DataIngestionConfig): Data ingestion configuration.
        """
        self.config = config

    def download_file(self):
        """
        Downloads the file from the source URL.

        Returns:
            None
        """
        if not os.path.exists(self.config.local_data_file):  # Check if the file already exists
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )  # Download the file using request.urlretrieve()
            logger.info(f"{filename} download! with following info: \n{headers}")  # Log the download info
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory and renames the extracted folder.
        """
        print("i am here")
        unzip_path = self.config.unzip_dir
        unzip_folder = self.config.unzip_folder
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            zip_infos = zip_ref.infolist()
            final_folder_name = zip_infos[0].filename            

        # Get the extracted folder name
        # extracted_folder_name = os.path.splitext(os.path.basename(self.config.local_data_file))[0]
        print(final_folder_name)

        # Get the full path of the extracted folder
        extracted_folder_full_path = os.path.join(unzip_path, final_folder_name)


        # Rename the extracted folder
        renamed_folder_path = os.path.join(unzip_path, unzip_folder)
        print(extracted_folder_full_path,renamed_folder_path)
        os.rename(extracted_folder_full_path, renamed_folder_path)

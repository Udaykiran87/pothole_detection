import os  # Import the os module
import urllib.request as request  # Import the request module from urllib
import zipfile  # Import the zipfile module
from potholeDetector import logger  # Import the logger module from potholeDetector
from potholeDetector.utils.common import *  # Import common utilities module
from potholeDetector.entity.config_entity import DataIngestionConfig  # Import DataIngestionConfig entity class
from pathlib import Path  # Import the Path class from pathlib


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
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
        Extracts the zip file into the unzip directory.

        Returns:
            None
        """
        unzip_path = self.config.unzip_dir  # Get the unzip directory path
        os.makedirs(unzip_path, exist_ok=True)  # Create the unzip directory if it doesn't exist
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:  # Open the zip file
            zip_ref.extractall(unzip_path)  # Extract all files to the unzip directory

# Import required modules and classes
from potholeDetector.constants import *  # Import constants module
from potholeDetector.utils.common import *  # Import common utilities module
from potholeDetector.entity.config_entity import (DataIngestionConfig, # Import DataIngestionConfig entity class
                                                  DataValidatorConfig) # Import DataValidatorConfig entity class


class ConfigurationManager:
    def __init__(
        self,
        config_filepath: str = CONFIG_FILE_PATH,
        params_filepath: str = PARAMS_FILE_PATH
    ):
        """
        Initializes the ConfigurationManager.

        Args:
            config_filepath (str): Filepath of the config YAML file.
            params_filepath (str): Filepath of the params YAML file.
        """
        self.config = read_yaml(config_filepath)  # Read the config YAML file
        self.params = read_yaml(params_filepath)  # Read the params YAML file

        create_directories([self.config.artifacts_root])  # Create required directories

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Retrieves the data ingestion configuration from the config file.

        Returns:
            DataIngestionConfig: Data ingestion configuration object.
        """
        config = self.config.data_ingestion  # Get the data ingestion configuration

        create_directories([config.root_dir])  # Create required directories

        # Create a DataIngestionConfig object with the extracted configuration values
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidatorConfig:
        """
        Retrieves the data validation configuration from the config file.

        Returns:
            DataValidatorConfig: Data validation configuration object.
        """
        config = self.config.data_validation  # Get the data validation configuration

        # Create a DataIngestionConfig object with the extracted configuration values
        data_validation_config = DataValidatorConfig(
            data_dir=config.data_dir,
            data_folder=config.data_folder,
            train_folder=config.train_folder,
            val_folder=config.val_folder,
            sub_dirs=config.sub_dirs,      
        )

        return data_validation_config

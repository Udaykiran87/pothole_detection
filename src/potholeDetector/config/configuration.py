from potholeDetector.constants import *  # Import constants module
from potholeDetector.utils.common import *  # Import common utilities module
from potholeDetector.entity.config_entity import (
    DataIngestionConfig,  # Import DataIngestionConfig entity class
    DataValidatorConfig,  # Import DataValidatorConfig entity class
    PrepareBaseModelConfig,  # Import PrepareBaseModelConfig entity class
    CustomTrainingConfig,  # Import CustomTrainingConfig entity class
    ValidationConfig,  # Import ValidationConfig entity class
)


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
            unzip_dir=config.unzip_dir,
            unzip_folder=config.unzip_folder
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
    

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        """
        Get the configuration for preparing the base model.

        Returns:
            PrepareBaseModelConfig: An instance of PrepareBaseModelConfig containing the configuration for
            preparing the base model.
        """
        # Retrieve the configuration for preparing the base model from the main configuration
        config = self.config.prepare_base_model

        # Retrieve the parameters for training from the main parameters
        params = self.params.training

        # Create the required directories if they do not exist
        create_directories([config.root_dir, config.weights_dir])

        # Create an instance of PrepareBaseModelConfig with the retrieved configuration
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            weights_dir=Path(config.weights_dir),
            download_url=config.download_url,
            task=params.task,
            mode=params.mode,
            model=params.model,
            imgsz=params.imgsz,
            data=params.data,
            epochs=params.epochs,
            batch=params.batch,
            name=params.name,
        )

        # Return the PrepareBaseModelConfig instance
        return prepare_base_model_config
    
    def get_custom_training_config(self) -> CustomTrainingConfig:
        """
        Get the configuration for custom training.

        Returns:
            CustomTrainingConfig: An instance of CustomTrainingConfig containing the configuration for
            custom training.
        """
        # Retrieve the configuration for custom training from the main configuration
        config_training = self.config.training
        config_prepare_base_model = self.config.prepare_base_model
        params = self.params.training

        # Create the required directories if they do not exist
        create_directories([
            self.config.artifacts_root, 
            config_training.root_dir, 
            config_training.trained_model_dir
        ])

        # Create an instance of CustomTrainingConfig with the retrieved configuration
        custom_training_config = CustomTrainingConfig(
            root_dir=Path(config_training.root_dir),
            trained_weights_dir=Path(config_training.trained_model_dir),
            params_task=params.task,
            params_mode=params.mode,
            params_model=params.model,
            params_imgsz=params.imgsz,
            params_data=Path(params.data),
            params_epochs=params.epochs,
            params_batch=params.batch,
            params_name=params.name,
            params_project=Path(params.project),
            base_weight_dir=config_prepare_base_model.weights_dir,  
            params_resume=params.resume,    
        )

        # Return the CustomTrainingConfig instance
        return custom_training_config
    

    def get_validation_config(self) -> ValidationConfig:
        """
        Get the configuration for validation.

        Returns:
            ValidationConfig: An instance of ValidationConfig containing the configuration for
            validation.
        """
        # Retrieve the configuration for validation from the main configuration
        config_validation = self.config.validation
        params = self.params.evaluation

        # Create the required directories if they do not exist
        create_directories([
            self.config.artifacts_root, 
            config_validation.root_dir, 
            config_validation.validation_results_dir
        ])

        # Create an instance of ValidationConfig with the retrieved configuration
        validation_config = ValidationConfig(
            params_task=params.task,
            params_mode=params.mode,
            params_model=params.model,
            params_imgsz=params.imgsz,
            params_name=params.name, 
            params_project=params.project, 
        )

        # Return the ValidationConfig instance
        return validation_config

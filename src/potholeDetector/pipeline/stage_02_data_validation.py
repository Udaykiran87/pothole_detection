from potholeDetector.config.configuration import ConfigurationManager  # Import ConfigurationManager from config module
from potholeDetector.component.data_validation import DataValidation  # Import DataValidation from component module
from potholeDetector import logger  # Import the logger module from potholeDetector

STAGE_NAME = "Data Validation stage"


class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        # Create a ConfigurationManager instance and retrieve the data validation configuration
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        # Create a DataValidation instance with the data validation configuration
        data_validation = DataValidation(config=data_validation_config)

        # Perform data validation steps
        data_validation.validate_folder_structure()
        data_validation.validate_image_label_counts()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        # Create an instance of the DataValidationPipeline class and run the main method
        obj = DataValidationPipeline()
        obj.main()

        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e

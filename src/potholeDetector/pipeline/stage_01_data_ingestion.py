from potholeDetector.config.configuration import ConfigurationManager  # Import ConfigurationManager from config module
from potholeDetector.component.data_ingestion import DataIngestion  # Import DataIngestion from component module
from potholeDetector import logger  # Import the logger module from potholeDetector

STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Create a ConfigurationManager instance and retrieve the data ingestion configuration
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        # Create a DataIngestion instance with the data ingestion configuration
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # Perform data ingestion steps
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        # Create an instance of the DataIngestionTrainingPipeline class and run the main method
        obj = DataIngestionTrainingPipeline()
        obj.main()

        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e

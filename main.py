from potholeDetector import logger  # Import the logger module from potholeDetector
from potholeDetector.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline  # Import DataIngestionTrainingPipeline from pipeline module

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    # Create an instance of DataIngestionTrainingPipeline and run the main method
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

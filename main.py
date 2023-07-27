from potholeDetector import logger  # Import the logger module from potholeDetector
from potholeDetector.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline  # Import DataIngestionTrainingPipeline from pipeline module
from potholeDetector.pipeline.stage_02_data_validation import DataValidationPipeline  # Import DataValidationPipeline from pipeline module
from potholeDetector.pipeline.stage_03_prepare_base_model import PrepareBaseModelPipeline  # Import PrepareBaseModelPipeline from pipeline module
from potholeDetector.pipeline.stage_04_custom_training import CustomTrainingPipeline  # Import CustomTrainingPipeline from pipeline module

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

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    # Create an instance of DataValidationPipeline and run the main method
    data_validation = DataValidationPipeline()
    data_validation.main()

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    # Create an instance of PrepareBaseModelPipeline and run the main method
    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Custom Model training stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    # Create an instance of CustomTrainingPipeline and run the main method
    custom_training = CustomTrainingPipeline()
    custom_training.main()

    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
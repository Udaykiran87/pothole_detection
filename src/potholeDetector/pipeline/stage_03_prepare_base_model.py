from potholeDetector.config.configuration import ConfigurationManager  # Import ConfigurationManager from config module
from potholeDetector.component.prepare_base_model import PrepareBaseModel  # Import PrepareBaseModel from component module
from potholeDetector import logger  # Import the logger module from potholeDetector

STAGE_NAME = "Prepare Base Model stage"


class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        # Create a ConfigurationManager instance and retrieve the prepare base model configuration
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()

        # Create a prepare_base_model instance with the prepare_base_modelconfiguration
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)

        # Perform prepare_base_model steps
        prepare_base_model.download_base_model()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        # Create an instance of the DataValidationPipeline class and run the main method
        obj = PrepareBaseModelPipeline()
        obj.main()

        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e

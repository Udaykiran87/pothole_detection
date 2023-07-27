from potholeDetector.config.configuration import ConfigurationManager  # Import ConfigurationManager from config module
from potholeDetector.component.custom_training import CustomTraining  # Import CustomTraining from component module
from potholeDetector import logger  # Import the logger module from potholeDetector

STAGE_NAME = "Custom Model training stage"


class CustomTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Create a ConfigurationManager instance and retrieve the prepare base model configuration
        config = ConfigurationManager()
        custom_training_config = config.get_custom_training_config()

        # Create a prepare_base_model instance with the custom_training_config
        custom_training = CustomTraining(config=custom_training_config)

        # Perform prepare_base_model steps
        custom_training.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        # Create an instance of the custom_training class and run the main method
        obj = CustomTrainingPipeline()
        obj.main()

        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e

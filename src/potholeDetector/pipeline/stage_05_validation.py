from potholeDetector.config.configuration import ConfigurationManager  # Import ConfigurationManager from config module
from potholeDetector.component.evaluation import Validation  # Import Validation from component module
from potholeDetector import logger  # Import the logger module from potholeDetector

STAGE_NAME = "Model validation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        # Create a ConfigurationManager instance and retrieve the validation configuration
        config = ConfigurationManager()
        Validation_config = config.get_validation_config()

        # Create a prepare_base_model instance with the Validation_config
        validation = Validation(config=Validation_config)

        # Perform validation steps
        validation.val()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        # Create an instance of the EvaluationPipeline class and run the main method
        obj = EvaluationPipeline()
        obj.main()

        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e

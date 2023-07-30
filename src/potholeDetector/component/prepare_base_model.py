import requests
import os  # Import the os module
import shutil
from potholeDetector.entity.config_entity import PrepareBaseModelConfig  # Import PrepareBaseModelConfig entity class
from potholeDetector import logger  # Import the logger module from potholeDetector

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        """
        Initialize the PrepareBaseModel class with the provided configuration.

        Args:
            config (PrepareBaseModelConfig): An instance of PrepareBaseModelConfig containing the
            configuration for preparing the base model.
        """
        self.config = config

    def download_base_model(self):
        """
        Downloads the YOLOv8 model to a custom folder.
        """
        # Create the full path for the downloaded model
        model_path = os.path.join(self.config.weights_dir, 'model.pt')        
        if self.config.resume == True:
            # Download the last saved model
            logger.info("Downloading YOLOv8 last saved model...")
            # Copy the file from the last_saved_model to the prepare_base_model dir
            shutil.copyfile(self.config.last_saved_model, model_path)            
        else:
            # Get the URL for the YOLOv8 pretrained model
            model_url = self.config.download_url + self.config.pre_trained_model

            # Download the model
            logger.info("Downloading YOLOv8 pretrained model...")
            response = requests.get(model_url, stream=True)        
            with open(model_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)                                

        # Print success message
        logger.info("Model downloaded successfully!")

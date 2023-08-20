from potholeDetector.entity.config_entity import ValidationConfig  # Import ValidationConfig entity class
from potholeDetector import logger  # Import the logger module from potholeDetector
from ultralytics import YOLO
import shutil
import os

class Validation:
    def __init__(self, config: ValidationConfig):
        """
        Initialize the Validation class.

        Args:
            config (ValidationConfig): An instance of ValidationConfig containing the configuration for validation.
        """
        self.config = config
    
    def val(self):
        """
        Perform validation of the YOLOv8 model.

        This method loads the YOLOv8 model using the provided configuration and performs evaluation on the specified data.

        Returns:
            None
        """
        # Load the YOLOv8 model.
        model = YOLO(self.config.params_model)

        # Evaluate the model.
        results = model.val(
            task=self.config.params_task,
            mode=self.config.params_mode,
            imgsz=self.config.params_imgsz,
            name=self.config.params_name,
            project=self.config.params_project,
        )
        
    def copy_final_model_weight(self, proj_config):
        """
        Copy the final model weight file to the specified destination directory.

        This function takes the source path of the final model weight file and the
        destination directory path from the project configuration.

        Args:
            proj_config (ProjectConfig): An instance of the project configuration class.

        Returns:
            None
        """
        # Get the source path of the final model weight file from params
        source_path = self.config.params_model
        
        # Get the destination directory from the project configuration
        destination_directory = proj_config.config.validation.weights_dir
        
        # Check if the source file and destination directory exist
        if os.path.isfile(source_path) and os.path.isdir(destination_directory):
            # Copy the source file to the destination directory with a specific name
            destination_path = os.path.join(destination_directory, 'final_weight.pt')
            shutil.copy(source_path, destination_path)
            logger.info(f"Final model weight file copied to {destination_path}")
        else:
            logger.info("Error: Either the source file or the destination directory does not exist.")
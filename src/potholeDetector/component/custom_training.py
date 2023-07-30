from potholeDetector.entity.config_entity import CustomTrainingConfig  # Import CustomTrainingConfig entity class
from potholeDetector import logger  # Import the logger module from potholeDetector
from ultralytics import YOLO  # Import the YOLO class from the ultralytics library
import os

class CustomTraining:
    def __init__(self, config: CustomTrainingConfig):
        """
        Constructor for the CustomTraining class.

        Args:
            config (CustomTrainingConfig): An instance of the CustomTrainingConfig data class containing the custom training configuration.
        """
        self.config = config
    
    def train(self):
        """
        Method to perform custom training using YOLOv8 model.

        Returns:
            None
        """
        # Load the YOLOv8 model using the specified model path.
        model_path = os.path.join(self.config.base_weight_dir, 'model.pt')
        model = YOLO(model_path)

        # Train the YOLOv8 model with the provided training configuration.
        results = model.train(
            task=self.config.params_task,
            mode=self.config.params_mode,
            imgsz=self.config.params_imgsz,
            data=self.config.params_data,
            epochs=self.config.params_epochs,
            batch=self.config.params_batch,
            name=self.config.params_name,
            project=self.config.params_project,
            resume=self.config.params_resume,
        )

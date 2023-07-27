from potholeDetector.entity.config_entity import ValidationConfig  # Import ValidationConfig entity class
from potholeDetector import logger  # Import the logger module from potholeDetector
from ultralytics import YOLO

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

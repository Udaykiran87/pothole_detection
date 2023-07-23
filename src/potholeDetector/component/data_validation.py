import os  # Import the os module
import glob
from pathlib import Path # Import the Path class from pathlib
from potholeDetector import logger  # Import the logger module from potholeDetector
from potholeDetector.utils.common import *  # Import common utilities module
from potholeDetector.entity.config_entity import DataValidatorConfig  # Import DataValidatorConfig entity class


class DataValidation:
    def __init__(self, config:DataValidatorConfig):
        self.config = config
        self.train_dir = os.path.join(self.config.data_dir, self.config.data_folder, self.config.train_folder)
        self.valid_dir = os.path.join(self.config.data_dir, self.config.data_folder, self.config.val_folder)        
        

    def validate_folder_structure(self):
        """
        Validate the folder structure of the dataset for YOLO.

        Returns:
            bool: True if the folder structure is valid, False otherwise.
        """        
        required_subdirs = self.config.sub_dirs
        for dir in [self.train_dir, self.valid_dir]:
            if not os.path.isdir(dir):
                raise False
            for folder in required_subdirs:
                path = os.path.join(dir, folder)
                if not os.path.isdir(path):
                    raise False
        return True

    def validate_image_label_counts(self):
        """
        Validate that the number of images matches the number of label files for YOLO.
        If a mismatch is found, delete the corresponding files.
        """        
        self._validate_counts_for_folder(self.train_dir)
        self._validate_counts_for_folder(self.valid_dir)

    def _validate_counts_for_folder(self, folder_path):
        """
        Validate image and label counts for a specific folder.
        If a mismatch is found, delete the corresponding files.

        Args:
            folder_path (str): Path to the folder containing images and labels.
        """
        required_subdirs = self.config.sub_dirs
        image_dir = os.path.join(folder_path, required_subdirs[0])  # Path to the folder containing images
        label_dir = os.path.join(folder_path, required_subdirs[1])  # Path to the folder containing labels

        image_files = set(self._get_file_names(image_dir, ".jpg"))
        label_files = set(self._get_file_names(label_dir, ".txt"))

        missing_image_files = list(label_files - image_files)
        missing_label_files = list(image_files - label_files)

        # Delete files with missing image or label
        for file in missing_image_files:
            image_path = os.path.join(image_dir, f"{file}.jpg")
            label_path = os.path.join(label_dir, f"{file}.txt")
            self._delete_file(image_path)
            self._delete_file(label_path)

        for file in missing_label_files:
            image_path = os.path.join(image_dir, f"{file}.jpg")
            label_path = os.path.join(label_dir, f"{file}.txt")
            self._delete_file(image_path)
            self._delete_file(label_path)

    def _get_file_names(self, directory, extension):
        """
        Get a list of file names with a specific extension in a directory.

        Args:
            directory (str): Directory path.
            extension (str): File extension (e.g., ".jpg", ".txt").

        Returns:
            list: List of file names.
        """
        return [Path(file).stem for file in glob.glob(os.path.join(directory, f"*{extension}"))]            

    def _delete_file(self, file_path):
        """
        Delete a file.

        Args:
            file_path (str): Path to the file.
        """
        if os.path.isfile(file_path):
            os.remove(file_path)                                    

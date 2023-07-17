import os  # Import the os module for operating system functionalities
from box.exceptions import BoxValueError  # Import the BoxValueError exception from the box.exceptions module
import yaml  # Import the yaml module for working with YAML files
from potholeDetector import logger  # Import the logger from the potholeDetector module
import json  # Import the json module for working with JSON data
# import joblib  # Import the joblib module for serialization and deserialization of Python objects
from ensure import ensure_annotations  # Import the ensure_annotations decorator for enforcing type annotations
from box import ConfigBox  # Import the ConfigBox class from the box module for working with configuration settings
from pathlib import Path  # Import the Path class from the pathlib module for working with file paths
from typing import Any  # Import the Any type from the typing module for type hinting
import base64  # Import the base64 module for encoding and decoding binary data



@ensure_annotations   # It indicates that the function's parameters and return value should have type annotations.
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: Exception if an error occurs while reading the file.

    Returns:
        ConfigBox: ConfigBox object representing the YAML file content.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories.

    Args:
        path_to_directories (list): List of paths of directories to be created.
        verbose (bool, optional): Flag to log directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")



@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Calculate the size in KB
    return f"~ {size_in_kb} KB"  # Return the size as a string with the "KB" suffix


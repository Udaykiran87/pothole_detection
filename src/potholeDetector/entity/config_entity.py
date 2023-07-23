from dataclasses import dataclass  # Import the dataclass decorator
from pathlib import Path  # Import the Path class from pathlib
from typing import List


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Data class representing the configuration for data ingestion.

    Attributes:
        root_dir (Path): The root directory path for data ingestion.
        source_URL (str): The source URL from where the data will be downloaded.
        local_data_file (Path): The local data file path where the downloaded data will be stored.
        unzip_dir (Path): The path of the directory where the downloaded data will be unzipped.
        unzip_folder (str): The name of the folder after the data is unzipped in `unzip_dir`.
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    unzip_folder: str

@dataclass(frozen=True)
class DataValidatorConfig:
    """
    Data class representing the configuration for data validation.

    Attributes:
        data_dir (Path): The root directory path where the data is located.
        data_folder (str): The name of the main data folder within `data_dir`.
        train_folder (str): The name of the folder containing training data within `data_folder`.
        val_folder (str): The name of the folder containing validation data within `data_folder`.
        sub_dirs (List[str]): A list of required subdirectories within `train_folder` and `val_folder`.
    """
    data_dir: Path
    data_folder: str
    train_folder: str
    val_folder: str
    sub_dirs: List[str]

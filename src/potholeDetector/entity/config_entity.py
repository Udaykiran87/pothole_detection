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

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    """
    Data class representing the configuration for preparing the base model.

    Attributes:
        root_dir (Path): The root directory path for preparing the base model.
        weights_dir (Path): The directory path to store the downloaded model weights.
        download_url (str): The URL to download the base model weights.
        task (str): The task for which the model will be used (e.g., object detection).
        mode (str): The mode of the model preparation (e.g., train, test).
        model (str): The specific model architecture to use.
        imgsz (int): The image size used for the model (e.g., 416).
        data (str): The type of data used for training the model (e.g., coco.yaml).
        epochs (int): The number of training epochs for the model.
        batch (int): The batch size used during training.
        name (str): The name of the model.
    """
    root_dir: Path
    weights_dir: Path
    download_url: str
    task: str
    mode: str
    model: str
    imgsz: int
    data: str
    epochs: int
    batch: int
    name: str
from dataclasses import dataclass  # Import the dataclass decorator
from pathlib import Path  # Import the Path class from pathlib


@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Data class representing the configuration for data ingestion.
    """
    root_dir: Path  # Root directory path
    source_URL: str  # Source URL
    local_data_file: Path  # Local data file path
    unzip_dir: Path  # Unzip directory path

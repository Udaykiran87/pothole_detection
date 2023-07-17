"""
This is constant module because all the configuration like config.yaml and params.yaml are constant in nature.
We mneed to change once at this place and entire project will be updated accordingly.
"""
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")  # Path to the configuration file (config.yaml)
PARAMS_FILE_PATH = Path("params.yaml")  # Path to the parameters file (params.yaml)

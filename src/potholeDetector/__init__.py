"""
This code sets up the logging configuration, including the format, file handler, and stream handler, 
and creates a logger instance named "potholeDetector" that can be used for logging in the rest of the code.
"""
import os
import sys
import logging

# Define the logging format
logging_str = "[%(asctime)s: %(levelname)s:%(module)s:%(message)s]"

# Define the directory for log files
log_dir = "logs"

# Create the full file path for the log file
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging module
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_str,  # Set the logging format using the defined logging string
    handlers=[
        logging.FileHandler(log_filepath),  # Add a file handler to log to the file
        logging.StreamHandler(sys.stdout)  # Add a stream handler to log to the console
    ]
)

# Create a logger instance with the specified name
logger = logging.getLogger("potholeDetector")

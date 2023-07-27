# pothole_detection

## Overview 

The Pothole Detection System is a computer vision-based project that aims to detect and analyze potholes in images. This system consists of several stages, each performing a specific task in the overall pipeline.
Steps to Create a Block Diagram
### Step 1: Data Ingestion

    The first step is to ingest the data required for training and validation.
    Run the stage_01_data_ingestion.py script to download and prepare the dataset.
    The data will be saved in the artifacts/data_ingestion/dataset directory.

### Step 2: Data Validation

    The second step is to validate the ingested data to ensure its quality and consistency.
    Execute the stage_02_data_validation.py script to perform data validation.
    The data will be validated and overwritten in the artifacts/data_ingestion/dataset directory.
    Note: The data folder is marked as always_changed to force re-evaluation each time.

### Step 3: Prepare Base Model

    In the third step, prepare the base model required for training.
    Run the stage_03_prepare_base_model.py script to prepare the base model.
    The prepared model weights will be saved in the artifacts/prepare_base_model/weights directory.

### Step 4: Custom Training

    The fourth step is to perform custom training on the prepared base model.
    Execute the stage_04_custom_training.py script to start custom training.
    The training process will use the configuration provided in config/params.yaml.
    The training results will be saved in the artifacts/training/runs directory.

### Step 5: Model Evaluation

    In the final step, evaluate the trained model's performance.
    Run the stage_05_validation.py script to evaluate the model.
    The evaluation results will be saved in the artifacts/validation/runs directory.


## Block Diagram

The block diagram for the Pothole Detection System can be illustrated as follows:

               +--------------+
               |              |
               | Data         |
               | Ingestion    |
               |              |
               +-----+--------+
                     |
                     v
               +-----+--------+
               |              |
               | Data         |
               | Validation   |
               |              |
               +-----+--------+
                     |
                     v
               +-----+--------+
               |              |
               | Prepare      |
               | Base Model   |
               |              |
               +-----+--------+
                     |
                     v
               +-----+--------+
               |              |
               | Custom       |
               | Training     |
               |              |
               +-----+--------+
                     |
                     v
               +-----+--------+
               |              |
               | Model        |
               | Evaluation   |
               |              |
               +--------------+



## Steps to Update the Pothole Detection System
### Step 1: Update config.yaml
Overview

    Make necessary changes to the config.yaml file.
    Update configuration settings related to data ingestion, validation, and other components.
    Provide accurate paths and URLs for data sources and directories.

### Step 2: Update params.yaml
Overview

    Modify the params.yaml file to update parameters used during training and evaluation.
    Adjust hyperparameters such as epochs, batch size, and other model-specific settings.

### Step 3: Update the Entity
Overview

    Make changes to data classes or entities used in the project.
    Update entity files to reflect the latest data representations.

### Step 4: Update the Configuration Manager in src config
Overview

    Update the ConfigurationManager class in the src/config module.
    Reflect changes made in the config.yaml and params.yaml files.
    Ensure proper reading and parsing of YAML files.

### Step 5: Update the Components
Overview

    Review and update individual components/modules used in the project.
    Modify components to utilize the updated configurations and entities.

### Step 6: Update the Pipeline
Overview

    Update pipeline stages in the src/pipeline module.
    Accommodate changes made in the configuration and components.
    Ensure proper utilization of updated settings and entities.

### Step 7: Update main.py
Overview

    Modify the main.py file.
    Reflect any changes made to the pipeline or components.
    Ensure proper initialization of classes and execution of pipeline stages.

### Step 8: Update dvc.yaml
Overview

    Update the dvc.yaml file.
    Reflect changes made in the pipeline stages and data paths.
    Define the dependencies and outputs for each pipeline stage.

## Conclusion

The Pothole Detection System can be effectively updated by following the steps in sequence. Each step addresses specific aspects of the project, such as configurations, entities, components, and the pipeline. A systematic approach to updating the project ensures it continues to function correctly and incorporates any modifications or enhancements required for improved performance.

### Folder Structure

```
pothole_detection
├── .github
│   └── workflows
│       └── .github
├── .gitignore
├── LICENSE
├── README.md
├── YOLOv8
│   ├── yolov8n
│   │   ├── args.yaml
│   │   └── weights
│   ├── yolov8n2
│   │   ├── args.yaml
│   │   ├── labels.jpg
│   │   ├── labels_correlogram.jpg
│   │   └── weights
│   └── yolov8n3
│       ├── args.yaml
│       └── weights
├── artifacts
│   ├── data_ingestion
│   │   ├── data.zip
│   │   ├── dataset
│   │   │   ├── README.txt
│   │   │   ├── class.names
│   │   │   ├── classes.txt
│   │   │   ├── labelmap.txt
│   │   │   ├── only_rainy_frames
│   │   │   │   └── train
│   │   │   │       ├── images
│   │   │   │       │   ├── img-1000_jpg.rf.f754fec46f449e3a04fa2d679a7cb384.jpg
│   │   │   │       │   ├── img-1002_jpg.rf.98fe082c7e3e0589440d49ec3a113d6c.jpg
│   │   │   │       ├── labels
│   │   │   │       │   ├── classes.txt
│   │   │   │       │   ├── img-1000_jpg.rf.f754fec46f449e3a04fa2d679a7cb384.txt
│   │   │   │       │   ├── img-1002_jpg.rf.98fe082c7e3e0589440d49ec3a113d6c.txt
│   │   │   │       └── labels.cache
│   │   │   ├── pothole.yaml
│   │   │   ├── remove_img_without_obj.py
│   │   │   ├── separate_labels_given_frames.py
│   │   │   ├── train
│   │   │   │   ├── images
│   │   │   │   │   ├── China_Drone_000048.jpg
│   │   │   │   │   ├── China_Drone_000048.npy
│   │   │   │   ├── labels
│   │   │   │   │   ├── China_Drone_000048.txt
│   │   │   │   └── labels.cache
│   │   │   ├── train_to_valid
│   │   │   │   ├── images
│   │   │   │   │   ├── G0011195.jpg
│   │   │   │   └── labels
│   │   │   │       ├── G0011195.txt
│   │   │   └── valid
│   │   │       ├── images
│   │   │       │   ├── G0011195.jpg
│   │   │       │   ├── G0011195.npy
│   │   │       ├── labels
│   │   │       │   ├── G0011195.txt
│   │   │       └── labels.cache
│   │   └── pothole_dataset_v8
│   │       ├── README.txt
│   │       ├── class.names
│   │       ├── classes.txt
│   │       ├── labelmap.txt
│   │       ├── only_rainy_frames
│   │       │   └── train
│   │       │       ├── images
│   │       │       │   ├── img-1000_jpg.rf.f754fec46f449e3a04fa2d679a7cb384.jpg
│   │       │   └── labels
│   │       │       ├── China_Drone_000048.txt
│   │       ├── train_to_valid
│   │       │   ├── images
│   │       │   │   ├── G0011195.jpg
│   │       │   └── labels
│   │       │       ├── G0011195.txt
│   │       └── valid
│   │           ├── images
│   │           │   ├── G0011195.jpg
│   │           └── labels
│   │               ├── G0011195.txt
│   ├── prepare_base_model
│   │   └── weights
│   │       └── yolov8n.pt
│   ├── training
│   │   └── runs
│   │       ├── yolov8n_v8_1e6
│   │       │   ├── F1_curve.png
│   │       │   ├── PR_curve.png
│   │       │   ├── P_curve.png
│   │       │   ├── R_curve.png
│   │       │   ├── args.yaml
│   │       │   ├── confusion_matrix.png
│   │       │   ├── confusion_matrix_normalized.png
│   │       │   ├── labels.jpg
│   │       │   ├── labels_correlogram.jpg
│   │       │   ├── results.csv
│   │       │   ├── results.png
│   │       │   ├── train_batch0.jpg
│   │       │   ├── train_batch1.jpg
│   │       │   ├── train_batch2.jpg
│   │       │   ├── val_batch0_labels.jpg
│   │       │   ├── val_batch0_pred.jpg
│   │       │   ├── val_batch1_labels.jpg
│   │       │   ├── val_batch1_pred.jpg
│   │       │   ├── val_batch2_labels.jpg
│   │       │   ├── val_batch2_pred.jpg
│   │       │   └── weights
│   │       │       ├── best.pt
│   │       │       └── last.pt
│   └── validation
│       └── runs
│           ├── yolov8n_eval
│           │   ├── F1_curve.png
│           │   ├── PR_curve.png
│           │   ├── P_curve.png
│           │   ├── R_curve.png
│           │   ├── confusion_matrix.png
│           │   ├── confusion_matrix_normalized.png
│           │   ├── val_batch0_labels.jpg
│           │   ├── val_batch0_pred.jpg
│           │   ├── val_batch1_labels.jpg
│           │   ├── val_batch1_pred.jpg
│           │   ├── val_batch2_labels.jpg
│           │   └── val_batch2_pred.jpg
├── config
│   └── config.yaml
├── dvc.yaml
├── environment.yml
├── logs
│   └── running_logs.log
├── main.py
├── params.yaml
├── pothole_v8.yaml
├── requirements.txt
├── research
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_prepare_base_model.ipynb
│   ├── 04_custom_training.ipynb
│   ├── 05_model_evaluate.ipynb
│   ├── logs
│   │   └── running_logs.log
│   └── trials.ipynb
├── setup.py
├── src
│   ├── potholeDetector
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   └── __init__.cpython-310.pyc
│   │   ├── component
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── custom_training.cpython-310.pyc
│   │   │   │   ├── data_ingestion.cpython-310.pyc
│   │   │   │   ├── data_validation.cpython-310.pyc
│   │   │   │   ├── evaluation.cpython-310.pyc
│   │   │   │   └── prepare_base_model.cpython-310.pyc
│   │   │   ├── custom_training.py
│   │   │   ├── data_ingestion.py
│   │   │   ├── data_validation.py
│   │   │   ├── evaluation.py
│   │   │   └── prepare_base_model.py
│   │   ├── config
│   │   │   ├── __pycache__
│   │   │   │   └── configuration.cpython-310.pyc
│   │   │   └── configuration.py
│   │   ├── constants
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       └── __init__.cpython-310.pyc
│   │   ├── entity
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   └── config_entity.cpython-310.pyc
│   │   │   └── config_entity.py
│   │   ├── pipeline
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── stage_01_data_ingestion.cpython-310.pyc
│   │   │   │   ├── stage_02_data_validation.cpython-310.pyc
│   │   │   │   ├── stage_03_prepare_base_model.cpython-310.pyc
│   │   │   │   ├── stage_04_custom_training.cpython-310.pyc
│   │   │   │   └── stage_05_validation.cpython-310.pyc
│   │   │   ├── stage_01_data_ingestion.py
│   │   │   ├── stage_02_data_validation.py
│   │   │   ├── stage_03_prepare_base_model.py
│   │   │   ├── stage_04_custom_training.py
│   │   │   └── stage_05_validation.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       │   ├── __init__.cpython-310.pyc
│   │       │   └── common.cpython-310.pyc
│   │       └── common.py
│   └── potholeDetector.egg-info
│       ├── PKG-INFO
│       ├── SOURCES.txt
│       ├── dependency_links.txt
│       └── top_level.txt
├── template.py
├── weights
└── yolov8n.pt
```

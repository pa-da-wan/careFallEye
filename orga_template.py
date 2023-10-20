import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "careFallEye"
project_sub_name = 'fall_detection'

list_of_files = [
    # ".github/workflows/.gitkeep",
    f"src/{project_sub_name}/__init__.py",
    "src/elder_main.py",
    f"src/{project_sub_name}/dataset_creation/__init__.py",
    f"src/{project_sub_name}/configs/__init__.py",
    f"src/{project_sub_name}/configs/config.py",
    f"src/{project_sub_name}/utils/__init__.py",
    f"src/{project_sub_name}/utils/elder_utils.py",
    f"src/{project_sub_name}/utils/telegram_utils.py",
    f"src/{project_sub_name}/model_training/__init__.py",
    f"src/{project_sub_name}/trained_models/__init__.py",
    f"src/{project_sub_name}/sample_files/__init__.py",
    "requirements.txt",
    "setup.py"
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass #creating an empty file only
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")

# careFallEye: Elderly Fall Detection System
careFallEye is an advanced fall detection system developed to enhance safety and well-being, particularly for the elderly and vulnerable individuals. The project was implemented using YOLO (You Only Look Once) object detection model. Upon detecting a fall, the system captures relevant frames and promptly sends notifications via Telegram, allowing caregiver or family members to respond swiftly.



## Table of Contents
- [Demo](#demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Running the Fall Detection System](#running-the-fall-detection-system)
- [Training Your Own Model (Optional)](#training-your-own-model-optional)
  - [Dataset Preparation](#dataset-preparation)
  - [Training the Model](#training-the-model)
- [Customization](#customization)

## Demo

![github](
https://github.com/pa-da-wan/careFallEye/assets/73534577/72288dbb-0040-4b06-80f4-e75ffd206900)



## Features

- **Real-time Fall Detection:** Utilizes YOLO object detection to identify and detect falls in real-time video streams.
- **Telegram Alerts:** Sends instant alerts with captured images to a designated Telegram group or user upon detecting a fall.
- **Customizable Configuration:** Easily configurable parameters such as confidence threshold, wait duration after fall, and snapshot interval.
- **Sample Files:** Includes sample video files for testing the fall detection system.


## Installation

1. **Clone the Repository:**

    Clone the repository to your local machine using the following command:

    ```
    git clone https://github.com/pa-da-wan/careFallEye.git
    ```

2. **Navigate to the Project Directory:**

    Change your working directory to the project folder:

    ```
    cd careFallEye
    ```

3. **Install Required Packages:**

    Install the necessary Python packages by running the following command:

    ```
    pip install -r requirements.txt
    ```
    
## Usage
### Configuration

1. **Modify Configuration Parameters:**

   - Open the `src/fall_detection/configs/config.py` file with a text editor.
   - Customize the configuration parameters according to your preferences. Key configurations include:
     - Paths and filenames
     - Detection settings (confidence threshold, wait duration after fall, etc.)
     - Telegram API settings

### Running the Fall Detection System

1. **Execute the System:**

   To run the fall detection system on a video or camera stream, execute the following command:
   ```
    python src/fall_main.py

    ```
2. **Exit the Program:**

- Press the 'q' key to exit the program.

## Training Your Own Model (Optional)
### Dataset Preparation

1. **Prepare a Custom Dataset:**

- Create a custom dataset for fall detection.
- Organize the dataset according to the required directory structure.

### Training the Model

1. **Training Your YOLO Model:**

- Use the provided `train_model.ipynb` Jupyter Notebook to train your YOLO model with the custom dataset.
- Save your trained model in the `fall_detection/trained_models` directory.


## Customization

- **Scripts:** You can customize existing scripts or create new ones based on your specific requirements.
- **Extensions:** Extend the system's functionality by integrating additional features or technologies.

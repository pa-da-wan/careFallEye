
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
DEMO 1:
![github](
https://github.com/pa-da-wan/careFallEye/assets/73534577/6da99666-c41b-4368-b3c3-3da607f5d82a)

DEMO 2:
![github](https://github.com/pa-da-wan/careFallEye/assets/73534577/5a337ee1-76bc-4289-a837-b6ea91e58b48)




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

3. **Create a Virtual Environment:**

    Choose one of the following methods to create and activate a virtual environment:

    - **Using Pip:**
      ```bash
      python -m venv venv
      source venv/bin/activate   # On Windows: .\venv\Scripts\activate
      ```

    - **Using Conda:**
      ```bash
      conda create --name careFallEye python=3.9
      conda activate careFallEye
      ```

4. **Install Required Packages:**

    Install the necessary Python packages by running the following command:

    ```
    pip install -r requirements.txt
    ```
    
## Usage
### Configuration

1. **Modify Configuration Parameters:**


    - Open the `config.yaml` file in the `fall_detection/configs` directory with a text editor.
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

The dataset used for training the model was collected from various publically available sources to ensure a diverse and comprehensive set of scenarios for fall detection. The data sources include:

1. [**CAUCAFall**](https://www.sciencedirect.com/science/article/pii/S2352340922008162)
2. [**Multicam Fall Dataset, U. Montreal**](http://www.iro.umontreal.ca/~labimage/Dataset/)
3. [**UR Fall Detection Dataset (URFD)**](http://fenix.ur.edu.pl/~mkepski/ds/uf.html)
4. [**Le2i fall detection dataset**](https://www.kaggle.com/datasets/tuyenldvn/falldataset-imvia)
5. [**High quality fall simulation data**](https://kuleuven.app.box.com/s/dyo66et36l2lqvl19i9i7p66761sy0s6)
6. Google Images

### Data Collection Process

Screenshots of relevant scenes were extracted from video clips obtained from the mentioned datasets. These screenshots were then annotated to create a labeled dataset with three categories: "no_fall," "fall," and "fall_prone."

### Annotated Dataset

The annotated dataset is available in the [src/fall_detection/dataset_creation](src/fall_detection/dataset_creation) directory. The dataset includes images labeled for fall detection training. Feel free to explore and utilize this dataset for training purposes.

I encourage contributions and the addition of more image data to enhance the robustness of the model. If you have additional data that could benefit the project, please consider sharing it with the community.
### Training the Model

1. **Training Your YOLO Model:**

- Use the provided `train_model.ipynb` Jupyter Notebook to train your YOLO model with the custom dataset.
- Save your trained model in the `fall_detection/trained_models` directory.


## Customization

- **Scripts:** You can customize existing scripts or create new ones based on your specific requirements.
- **Extensions:** Extend the system's functionality by integrating additional features or technologies.

import cv2
from ultralytics import YOLO
import yaml
import os


config_path='src/fall_detection/configs/config.yaml'
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

max_snaps = config['detection_settings']['max_snapshots']

class ObjectDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_objects(self, image, confidence_threshold=0.5, class_index=1):
        result = self.model(image, conf=confidence_threshold, classes=class_index)
        bbox = result[0].boxes.xyxy.cpu().numpy().astype(int)
        return bbox

def create_snapshot_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def clear_snapshots_directory(directory_path, max_snapshots=max_snaps):
    # Clear existing files in the snapshots directory, keeping at most `max_snapshots` number of pictures
    files = sorted(os.listdir(directory_path), key=lambda x: os.path.getctime(os.path.join(directory_path, x)))
    while len(files) > max_snapshots:
        file_to_remove = os.path.join(directory_path, files[0])
        os.remove(file_to_remove)
        files.pop(0)

def draw_bounding_boxes(image, bbox):
    for box in bbox:
        x1, y1, x2, y2 = box
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
        center_x = int(x1 + (x2 - x1) / 2)
        center_y = int(y1 + (y2 - y1) / 2)
        cv2.circle(image, (center_x, center_y), 7, (0, 255, 0), -1)
    return image

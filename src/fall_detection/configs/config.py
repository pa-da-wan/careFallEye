import os


# Paths and Filenames
MODEL_PATH = os.path.join('src','fall_detection','trained_models','YOLO_best1200.pt') #'path to trained model'
VIDEO_PATH =  os.path.join('fall_detection','sample_files','fall-02-cam0.mp4') #'path/to/your/video.mp4'
# VIDEO_PATH =  0  # 'for camera'
SNAPSHOT_DIRECTORY = 'snapshots'
MAX_SNAPSHOTS=25

# Detection Settings
CONFIDENCE_THRESHOLD = 0.47
WAIT_DURATION_AFTER_FALL = 2  # Time in seconds to wait after detecting a fall before sending an alert
MAX_SNAPSHOTS = 20  # Maximum number of images to keep in the snapshots directory
SNAPSHOT_INTERVAL = 10

# Telegram API Settings
TELEGRAM_BOT_API = os.environ.get("TELEGRAM_BOT_API")
TELEGRAM_FD_GROUP_CODE = os.environ.get("TELEGRAM_FD_GROUP_CODE")

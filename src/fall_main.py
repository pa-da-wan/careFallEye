import cv2
from fall_detection.utils.fall_utils import ObjectDetector, create_snapshot_directory, clear_snapshots_directory, draw_bounding_boxes
from fall_detection.utils.telegram_utils import send_message_with_image
from fall_detection.configs.config import *
import time

def main():
    detector = ObjectDetector(MODEL_PATH)
    last_snapshot_time = time.time() - SNAPSHOT_INTERVAL
    fall_detected_time = None

    create_snapshot_directory(SNAPSHOT_DIRECTORY)
    clear_snapshots_directory(SNAPSHOT_DIRECTORY)

    cap = cv2.VideoCapture(VIDEO_PATH)

    while cap.isOpened():
        ret, img = cap.read()

        if ret:
            bbox = detector.detect_objects(img, confidence_threshold=CONFIDENCE_THRESHOLD, class_index=1)
            img_with_boxes = draw_bounding_boxes(img, bbox)
            cv2.imshow("Detection", img_with_boxes)

            fall_detected = len(bbox) > 0

            if fall_detected and (time.time() - last_snapshot_time) >= SNAPSHOT_INTERVAL:
                if fall_detected_time is None:
                    fall_detected_time = time.time()

                if (time.time() - fall_detected_time) >= WAIT_DURATION_AFTER_FALL:
                    bbox_after_wait = detector.detect_objects(img, confidence_threshold=CONFIDENCE_THRESHOLD, class_index=1)
                    fall_still_detected = len(bbox_after_wait) > 0

                    if fall_still_detected:
                        timestamp = time.strftime("%d-%B-%Y_%H:%M:%S")
                        snapshot_filename = f'{SNAPSHOT_DIRECTORY}/snap_{timestamp}.jpg'
                        cv2.imwrite(snapshot_filename, img_with_boxes)
                        caption = f'Check on the person, clicked at: {timestamp}'
                        send_message_with_image(snapshot_filename, caption)

                        last_snapshot_time = time.time()
                        fall_detected_time = None

                        clear_snapshots_directory(SNAPSHOT_DIRECTORY, max_snapshots=MAX_SNAPSHOTS)
        else:
            print("Error: Could not read a frame from the video.")
            break

        key = cv2.waitKey(1)
        if key == 27 or key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

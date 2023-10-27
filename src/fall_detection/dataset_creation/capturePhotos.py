import cv2
import os
import uuid

imgCount = 0
i = 1
running = True
paused = False
current_frame = 0

video_directory = 'fall_sim_data'  # Directory containing the video files

# Check whether the specified path exists or not
imageCaptureDirectory = "captured_photos"+"_"+video_directory
if not os.path.exists(imageCaptureDirectory):
    os.makedirs(imageCaptureDirectory)
    print(f"New directory '{imageCaptureDirectory}' created!")

video_files = sorted([f for f in os.listdir(video_directory) if os.path.isfile(os.path.join(video_directory, f))])

for video_file in video_files:
    video_path = os.path.join(video_directory, video_file)
    
    if not video_file.lower().endswith(('.mp4', '.avi', '.mov')):  # Filter video files based on extensions
        continue
    
    video = cv2.VideoCapture(video_path)

    while video.isOpened() and running:
        if not paused:
            ret, frame = video.read()
            if not ret:
                print(f"\n\nERROR OPENING THE STREAM: {video_file}!!!\n\n")
                break
            current_frame = video.get(cv2.CAP_PROP_POS_FRAMES)  # Get the current frame position
            cv2.imshow(f'output stream: {video_file}', frame)
        else:
            # Set the video frame to the current paused frame to freeze the video stream
            video.set(cv2.CAP_PROP_POS_FRAMES, current_frame)

        key = cv2.waitKeyEx(30) & 0XFF

        if key == ord('n'):
            next_index = video_files.index(video_file) + 1
            if next_index < len(video_files):
                next_vid = video_files[next_index]
                video_file = next_vid  # Update video_file for correct numbering
                next_vid_path = os.path.join(video_directory, next_vid)
                i += 1  # Increment 'i' only when switching to a new video
                print(f"Playing video number {i} next @ {next_vid_path}")
                print(50*'-'+'\n\n')
                break
            else:
                print("No more videos available.")
                break
        elif key == ord('p'):
            if video_files.index(video_file) > 0:
                previous_vid = video_files[video_files.index(video_file) - 1]
                video_file = previous_vid  # Update video_file for correct numbering
                previous_vid_path = os.path.join(video_directory, previous_vid)
                i -= 1  # Decrement 'i' only when switching to a new video
                print('\n\n' + 50 * '=')
                print(f"Playing video number {i} next @ {previous_vid_path}")
                print(50 * '=' + '\n\n')
                break
            else:
                print("This is the first video.")
                break

        elif key == ord(' '):  # Spacebar to pause/resume
            paused = not paused
        elif key == ord('a'):  # 'a' key to move 5 frames back
            current_frame = video.get(cv2.CAP_PROP_POS_FRAMES)
            new_frame = max(current_frame - 150, 0)
            video.set(cv2.CAP_PROP_POS_FRAMES, new_frame)
        elif key == ord('d'):  # 'd' key to move 5 frames forward
            current_frame = video.get(cv2.CAP_PROP_POS_FRAMES)
            total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
            new_frame = min(current_frame + 150, total_frames - 1)
            video.set(cv2.CAP_PROP_POS_FRAMES, new_frame)
        elif key == ord('s'):  # 's' key to save frames
            imgCount += 1
            captured_img_path = os.path.join(imageCaptureDirectory, '{}.jpg'.format(uuid.uuid1()))
            cv2.imwrite(captured_img_path, frame)
            print(f'Saved image number {imgCount} from {video_file} in {imageCaptureDirectory}')
        elif key == ord('q'):  # 'q' key to quit the program
            print('\n\n' + 25 * '#')
            print('Exiting the program. Bye!')
            print(25 * '#' + '\n\n')
            running = False
            break

video.release()
cv2.destroyAllWindows()

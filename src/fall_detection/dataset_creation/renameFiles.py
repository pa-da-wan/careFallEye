import os
import random

filesList = (os.listdir(os.path.join('selfieCapture','selfieWebcam_images')))
random.shuffle(filesList)


print('number of items = ', len(filesList))

    
n = 1
# for n,item in enumerate(filesList):
for item in filesList:
    filename, extension = os.path.splitext(item)
    os.rename(os.path.join('selfieCapture','selfieWebcam_images', item), os.path.join('selfieCapture','selfieWebcam_images', f'webcam_img_{n}{extension}'))
    n+=1


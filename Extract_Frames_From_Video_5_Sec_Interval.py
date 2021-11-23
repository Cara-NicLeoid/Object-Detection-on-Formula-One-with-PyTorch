# This script takes an mp4 video file as input, then saves frames as a jpg at a 5 second interval. 
# The output of this script the images, ready to be labelled. 

import cv2
vidcap = cv2.VideoCapture('F1_Car.mp4')
success,image = vidcap.read()
count = 0
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*5000)) 
  cv2.imwrite("frame%d.jpg" % count, image)     
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1 


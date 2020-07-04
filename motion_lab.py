# This program does simple motion detection. It uses OpenCV to perform
# background subtraction. If the differences between the images exceeds a threshold
# it indicates motion

# On a new install on a Raspberry Pi you need to run the following from the
# bash command line
# pip3 install opencv-contrib-python; sudo apt-get install -y libhdf5-dev libatlas-base-dev libjasper-dev  libqtgui4  libqt4-test

# import the necessary packages
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
import os  # Need to execute scp from the command line to move the image to AWS server
import datetime

# This program will accept an argument --video and the path to a video file to
# process or no parameters means it will use the Raspberry Pi Camera.

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
	vs = VideoStream(src=0).start()
	time.sleep(2.0)

# otherwise, we are reading from a video file
else:
	vs = cv2.VideoCapture(args["video"])

# initialize the first frame in the video stream
firstFrame = None
framecount = 1
# loop over the frames of the video
print("Monitoring for motion")
while True:
# Get current date and time
	now = datetime.datetime.now()

# This handles slowly changing lighting in a scene. Every 10 occupied frames or
# 10 minutes it will reset the base frame. Not really needed where there is
# artiifical lighting, but doesn't hurt.

	if now.minute % 10 == 0:
		firstFrame = None
		framecount = 0
	if framecount > 10:
		firstFrame = None
		framecount = 0

# Create a time stamp string to be used with the image file name when we detect motion
	timestamp = "%4d%02d%02d%02d%02d%02d" % (now.year, now.month, now.day, now.hour, now.minute, now.second)

#Get the current frame and initialize the occupied/unoccupied text
	frame = vs.read()
	frame = frame if args.get("video", None) is None else frame[1]
	text = "Unoccupied"

# If the frame could not be grabbed, then we have reached the end of the video
	if frame is None:
		break

# Resize the frame, convert it to grayscale, and blur it
# This reduces the information we have to deal with, which reduces the processing
# power needed. A downside to this is it will not detect very subtle motion that
# only affects a small part of the frame.

	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

# If the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue # We don't want to do the rest of the loop if it is the first frame

# Compute the absolute difference between the current frame and first frame
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

# Dilate the thresholded image to fill in holes, then find contours on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

# Loop over the contours
	for c in cnts:

# If the contour is too small, ignore it
		if cv2.contourArea(c) < args["min_area"]:
			continue

# Compute the bounding box for the contour, draw it on the frame, and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Occupied"

# Draw the text and timestamp on the frame
	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

# If you are running this from the GUI you can uncomment the three cv2.imshow lines
# This will show you the intermediate images during processing.
# If you are using ssh to get into your Raspberry Pi. Don't uncomment them as it
# will cause the program to fail. Also since we would be probably using
# this headless we won't use them anyway.

# Show the frame
#	cv2.imshow("Security Feed", frame)
#	cv2.imshow("Thresh", thresh)
#	cv2.imshow("Frame Delta", frameDelta)

# If the room is Occupied we want to write it out to a file.

	if text == "Occupied":
		filename = 'img'+timestamp+".jpg"
		cv2.imwrite(filename, frame)
		print("Motion detected. Saved to file: %s" % filename)

# Add your code here to use scp to copy the imagefile just created to the AWS server
# You will need to use the os module to execute the scp command as if it was typed
# in at the command line.


		framecount = framecount + 1
		time.sleep(1)	# Sleep for 1 second to reduce the number of files
	else:
		framecount = 0
# If the `q` key is pressed, break from the lop
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

# cleanup the camera and close any open windows
vs.stop() if args.get("video", None) is None else vs.release()

# cv2.destroyAllWindows()  # Uncomment this if you are running from the GUI.

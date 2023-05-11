
# Motion Detection Test

This is a Python application that uses computer vision techniques to detect motion in videos. It provides a graphical user interface (GUI) for selecting a video file, configuring detection settings, and displaying the detected motion in real-time.

## Features

- Select a video file for motion detection.
- Adjust various settings for motion detection. (In works)
- Display the video feed with motion bounding boxes and contours.
- Save and load configuration settings from a file.
- Simple and intuitive graphical user interface. 

## Prerequisites

- Python 3.x
- OpenCV library
- tkinter library

## Installation

pip install opencv-python

Run the script:
python motion_detection.py

  The application window will appear.

  Click on "Input video" to select a video file for motion detection.

  Adjust the settings by clicking on "Settings" and make changes as desired.

  Click on "Start" to begin motion detection.

  The video feed will be displayed with motion bounding boxes and contours.

  Press the "Esc" key to stop motion detection and close the application.

## Configuration Settings

The application provides the following configuration settings that can be adjusted via the "Settings" option:

- **Show Masks**: When enabled, the binary mask of the detected motion will be displayed.

- **Region of Interest**: Allows focusing the motion detection on a specific region of the video by specifying a region of interest (ROI).

- **Show Contours**: When enabled, contours will be displayed around the detected motion.

- **History**: The number of frames to use for background modeling. Higher values capture longer history, which may help in handling gradual changes in the background.

- **varThreshold**: The threshold value for segmenting the foreground from the background. Adjusting this value affects the sensitivity of motion detection.

Feel free to adjust these settings based on your specific requirements. The graphical user interface (GUI) allows easy configuration and experimentation to achieve the desired motion detection results.




## License
MIT License

Feel free to contribute, report issues, or suggest improvements by creating pull requests or submitting issues.

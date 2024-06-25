Hand Gesture Control with OpenCV and Mediapipe

This project demonstrates how to use hand gestures to control the mouse cursor using OpenCV, Mediapipe, and PyAutoGUI. The index finger tip is used to move the cursor, and bringing the index finger tip close to the thumb tip performs a click action.
Features

    Hand detection and tracking using Mediapipe.
    Mouse cursor control using PyAutoGUI.
    Click action by bringing the index finger and thumb tips close together.

Requirements

    Python 3.7+
    OpenCV
    Mediapipe
    PyAutoGUI

Installation

    Clone the repository:

    bash

git clone https://github.com/your-username/hand-gesture-control.git
cd hand-gesture-control

Create a virtual environment and activate it:

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:

bash

    pip install opencv-python mediapipe pyautogui

Usage

    Run the script:

    bash

    python hand_gesture_control.py

    Allow access to your webcam if prompted.

    Move your index finger to control the mouse cursor.

    Perform a click by bringing the index finger tip close to the thumb tip.

Code Explanation

The main components of the code are:

    Initialize Mediapipe Hand Detector: Set up the hand detection and tracking with a minimum detection and tracking confidence of 0.7.
    Screen Dimensions: Get the screen width and height using PyAutoGUI.
    Video Capture: Initialize video capture to read frames from the webcam.
    Hand Landmarks Detection: Process the frames to detect hand landmarks.
    Cursor Movement: Move the mouse cursor based on the index finger tip position.
    Click Action: Perform a click when the index finger tip is close to the thumb tip.

    Contributing

Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.
License

This project is licensed under the MIT License. See the LICENSE file for details.

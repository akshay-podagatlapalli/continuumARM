# Hand Position Tracking and Servo Control System
## Overview

This project consists of two main components: a Python script for tracking hand position using a webcam and a corresponding Arduino script for controlling servo motors based on the detected hand position.


## Python Script

The Python script uses OpenCV and MediaPipe to capture and process webcam video data to track the position of a hand. The script calculates the wrist's coordinates and sends this data through a serial port.

## Arduino Script

The Arduino script receives the coordinate data from the Python script and uses it to control two servo motors, mapping the hand's position to the servos' movements.

## Requirements

### For the Python Script:

    Python 3.x
    OpenCV (cv2) library
    MediaPipe library
    NumPy library
    PySerial library

### For the Arduino Script:

    An Arduino board (e.g., Arduino Uno)
    Servo motors (2x)
    Arduino IDE for uploading the script to the board

## Setup and Installation

## Python Environment Setup:

    Install Python 3.x from python.org.
    Install the required Python libraries using pip:

    sh

    pip install opencv-python-headless mediapipe numpy pyserial

## Arduino Setup:

    Connect the servo motors to the Arduino board.
    Use the Arduino IDE to upload the provided Arduino script to the board.

## Usage Instructions

## Running the Python Script:

    Connect the Arduino board to your computer.
    Open the Python script and adjust the serial port in the script to match the port where the Arduino is connected.
    Run the Python script. It will start using your webcam to track your hand's position.

## Operating the Arduino Script:

    Once the Python script is running and sending data, the Arduino script will receive hand position coordinates.
    The servos will move according to the hand's position detected by the webcam.

## Troubleshooting

    Ensure that the correct serial port is specified in the Python script.
    Check the connections of the servo motors to the Arduino board.




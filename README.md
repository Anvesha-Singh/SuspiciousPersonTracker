# RavenEYE: Suspicious Person Tracker

RavenEYE is an autonomous robotic surveillance system designed to enhance security by actively tracking suspicious individuals using a pan-tilt camera system. This project combines real-time face detection with dynamic camera control to overcome the limitations of static security cameras.

## Project Overview
Traditional surveillance systems have limited fields of view and fixed orientations, which can lead to blind spots in security coverage. RavenEYE addresses these challenges by dynamically tracking faces and adjusting the camera's angle, allowing continuous surveillance in dynamic environments. The system is particularly useful for monitoring events, offices, homes, and public spaces.

## Table of Contents
- [Features](#features)
- [System Architecture](#system-architecture)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Setup and Installation](#setup-and-installation)

## Features
- **Real-time Face Detection**: Utilizes OpenCV's Viola-Jones algorithm for efficient face detection in varying lighting conditions.
- **Dynamic Camera Control**: A pan-tilt mechanism, controlled via Arduino, adjusts the camera angle based on the detected face position.
- **Laptop-Arduino Communication**: PySerial provides real-time data exchange, synchronizing camera adjustments with the face tracking model.
- **Adaptable for Various Environments**: Suitable for security applications in homes, offices, and events, with potential customization options for specific needs.

## System Architecture
1. **Camera**: A high-resolution USB camera mounted on a tilt-and-pan servo system captures video frames.
2. **Face Detection Module**: OpenCV detects and tracks faces, calculating the face’s position in each frame.
3. **Arduino**: Controls the servo motors, adjusting the camera orientation to keep detected faces in the center of the frame.
4. **Communication (PySerial)**: Sends tracking data from the laptop to the Arduino, maintaining synchronized movements for real-time tracking.

## Hardware Requirements
- **USB Camera**: High-resolution camera for clear face detection.
- **Arduino UNO**: Microcontroller to control the servo motors.
- **Servo Motors**: At least two servo motors for pan and tilt movements.
- **Laptop or PC**: Runs the face detection model and communicates with the Arduino.
- **USB Cable**: Connects Arduino to the laptop.

## Software Requirements
- **Python 3.13.0**
- **Arduino IDE**
- **Python Libraries**:
  - OpenCV
  - YOLOv8
  - PySerial
  - NumPy 

## Setup and Installation

```bash
git clone https://github.com/Anvesha-Singh/SuspiciousPersonTracker.git
cd SuspiciousPersonTracker
python tracker.py
```

# Gesture-Controlled Mouse using Hand Tracking

This project implements a gesture-controlled mouse system using Python, OpenCV, Mediapipe, and PyAutoGUI. It tracks hand movements through a webcam and translates them into mouse cursor movements on the screen. A specific hand gesture is used to simulate mouse clicks.

## Technologies Used:
- **OpenCV:** Captures webcam input and processes the video stream.
- **Mediapipe:** Detects hand landmarks to track hand gestures.
- **PyAutoGUI:** Controls the mouse movement and simulates clicks.
- **NumPy:** Calculates the distance between hand landmarks for gestures.

## Features:
- **Hand Tracking:** Detects hand landmarks in real-time, focusing on the thumb and index finger for cursor movement.
- **Smooth Cursor Movement:** A smoothing algorithm ensures that the cursor movement is fluid and precise.
- **Click Gesture:** When the thumb and index finger are close to each other, the system triggers a mouse click.
- **Real-time Feedback:** The webcam feed is displayed with a circle around the tracked finger. A "click" label appears when the click gesture is detected.


git clone https://github.com/yourusername/gesture-controlled-mouse.git
cd gesture-controlled-mouse

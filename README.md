# Automated Home Security Camera with Face Recognition

## Introduction
This Python script is designed to create a simple automated security camera system with face recognition capabilities. The system captures live video from a camera, detects faces in the frames, and compares them to a preloaded set of known faces. If an unknown face is detected, it sends an email alert to the owner.
Prerequisites
Make sure you have the following installed before running the code:
* Python 3.x
* OpenCV (cv2) library
* Face recognition library
* smtplib for sending emails

Install the required libraries using the following:
```
pip install opencv-python face_recognition
```
## Usage
1. Clone the repository to your local machine
2. Navigate to the project directory
3. Run the main script
4. Follow the instructions shown on the screen.
## Files
* main.py: The main script that initiates the system, takes user input, and starts the camera.
* detector.py: Contains functions for face encoding and face comparison.
* mail.py: Sends email alerts using the smtplib library.
* email.txt: Stores the recipient's email address.
* media : directory for storing the known faces
## Notes
1. Ensure the "media" folder is empty before starting the system.
2. The camera feed will be displayed, and face recognition will be performed in real-time.
3. If a stranger is detected, an email alert will be sent to the specified recipient.
4. Press 'q' to exit the camera feed.

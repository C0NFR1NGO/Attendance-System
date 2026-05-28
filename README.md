\# Real-Time Face Recognition Attendance System



\## 📌 About the Project

This project is a Python-based, real-time facial recognition script designed to automate the attendance-taking process. By utilizing a standard webcam, the program detects faces in the live video feed, compares them against a pre-loaded database of known faces, and logs the recognized individuals into a CSV file with an accurate date and timestamp. 



\## ⚙️ What it Implements

The script leverages the power of computer vision and machine learning libraries to achieve its functionality:

\* \*\*`OpenCV` (cv2):\*\* Handles the webcam video stream, image resizing (for performance optimization), and drawing bounding boxes/text on the live feed.

\* \*\*`face\_recognition`:\*\* Powered by dlib, this library handles the heavy lifting of detecting facial landmarks (using the HOG model) and generating 128-dimension face encodings for comparison.

\* \*\*`NumPy`:\*\* Used for mathematical operations, specifically finding the minimum facial distance (best match) between the live frame and known encodings.



\## 🚀 Features (What it Does)

\* \*\*Real-Time Detection:\*\* Captures and processes webcam frames in real-time.

\* \*\*Automated Logging:\*\* Automatically appends the recognized person's name, the current date, and the exact time to an `Attendance.csv` file.

\* \*\*Session Management:\*\* Utilizes a Python `set` (`marked\_this\_session`) to ensure a person is only logged once per script execution, preventing duplicate spam in the CSV file.

\* \*\*Visual Feedback:\*\* Displays a live video window drawing a bounding box around detected faces and overlaying the recognized person's name.



\---



\## 🛠️ Prerequisites and Requirements



To run this script successfully, you will need a few system requirements and Python libraries installed.



\### System Requirements

\* \*\*Python:\*\* Version 3.7 or higher.

\* \*\*Hardware:\*\* A working webcam (built-in or USB).

\* \*\*C++ Compiler:\*\* Because the `face\_recognition` library depends on `dlib`, you often need a C++ compiler installed on your system (e.g., Visual Studio Build Tools on Windows, or `build-essential` on Linux/macOS) to build `dlib` successfully.

\* \*\*A Folder named imagesBasic containing photos of people (jpg) to mark attendance for , for the program to reference with.



\### Python Dependencies

Install the required libraries using `pip`:



```bash

pip install opencv-python numpy face\_recognition face\_recognition\_models setuptools


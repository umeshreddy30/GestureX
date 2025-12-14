AI Hand Tracker (Sign Language Beta)
This is a simple program that uses Artificial Intelligence to track your hand movements in real-time through your webcam. It draws a digital skeleton on your hands!

It is built to be the first step for a Sign Language Translator.

🚀 How to Run It (The Easy Way)
You don't need to type any code. I have made a "One-Click" launcher for you.

Download this project folder.

Make sure you have Python 3.10 installed on your computer.

Double-click the file named START_PROJECT.bat.

That's it! A black window will open, install the necessary tools, and then your camera will turn on.

📋 What You Need
Windows Laptop/PC

Webcam

Python 3.10 (Download Here)

Important: When installing Python, check the box that says "Add Python to PATH".

🎮 Controls
Show Hands: Put your hands in front of the camera to see the skeleton tracking.

Quit: Press the q key on your keyboard to close the app.

📂 File Description
Here is what the files in this folder do:

START_PROJECT.bat ➔ The Launcher. Double-click this to run the app.

main.py ➔ The Brain. This contains the Python code that powers the AI.

requirements.txt ➔ The Shopping List. Tells the computer which libraries (MediaPipe, OpenCV) to download.

❓ Common Problems
"The black window opens and closes immediately!" This usually means you don't have Python 3.10 installed. Please download it from the link above.

"It says Camera not found" If you have multiple cameras, open main.py in a text editor (like Notepad) and change cv2.VideoCapture(0) to cv2.VideoCapture(1).

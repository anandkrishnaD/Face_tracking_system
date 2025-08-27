# Face Tracking Laser Project

This project uses **computer vision** to detect and track faces in real time, controlling a **laser pointer mounted on servo motors** to follow the target. It combines **OpenCV**, **YOLO object detection**, and **Arduino integration** for a fun but practical demonstration of face tracking technology.
<img width="810" height="507" alt="Laser_Tracking_reco" src="https://github.com/user-attachments/assets/b693db57-4337-4f7c-aed9-76a54c64abd4" />

---

## Features
- Real-time **face detection** using [face-recognition](https://github.com/ageitgey/face_recognition) and **OpenCV**.
- **YOLO model** integration for detecting other objects (e.g., bowl, cup, etc.).
- Smooth tracking using **servo motors** connected via **Arduino**.
- Automatic switch between **face detection mode** and **YOLO object detection mode**.
- User-friendly control and adjustable settings.

---

## 🛠️ Tech Stack
- **Python 3**
- **OpenCV** – Computer vision & webcam integration  
- **face_recognition** – Face detection & recognition  
- **YOLO (Ultralytics)** – Object detection  
- **Arduino (C++)** – Servo motor control  
- **PySerial** – Communication between Python and Arduino  

---

## ⚙️ Hardware Requirements
- Laptop/Desktop with webcam  
- Arduino Uno (or compatible board)  
- Servo motors (2x – horizontal & vertical rotation)  
- Laser pointer  
- Mounting frame (3D printed or DIY)  

---

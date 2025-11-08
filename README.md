# 🚗 Parking Spot Detection using YOLOv10 and OpenCV

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![YOLOv10](https://img.shields.io/badge/YOLO-v10-green?logo=yolo)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-orange?logo=opencv)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

---

### 🎥 Real-Time Parking Detection Demo

<p align="center">
  <img src="assets/sample_output.gif" alt="Parking Spot Detection Demo" width="700"/>
</p>

> This project performs **real-time detection of empty and occupied parking spaces** using **YOLOv10** and **OpenCV**, providing instant feedback on available parking slots.

---

## 🧠 Overview

This is my **Semester 1 EL Project at RV College of Engineering**, focused on applying **Computer Vision and Deep Learning** for **Smart Parking Automation**.  
The system identifies cars within predefined parking regions and dynamically updates the visual map to show available and occupied spots.

---

## 🎯 Features

- 🚘 **Real-Time Detection** — Detects vehicles using YOLOv10  
- 🟩 **Dynamic Visualization** — Shows filled and empty parking spaces  
- 🔲 **Custom Parking Zones** — Define any number of parking areas using polygons  
- 💡 **Instant Count Display** — Shows available parking spaces on-screen  
- ⚙️ **Plug & Play Setup** — Simple Python-based script, no web dependencies  

---

## 🗂️ Project Structure

📦 Parking-Spot-Detection
┣ 📜 model.py # Main detection script
┣ 📜 coco.txt # COCO class labels
┣ 📜 test1.mp4 # Input parking lot video
┣ 📜 requirements.txt # Python dependencies
┣ 📜 README.md # Documentation
┗ 📂 assets/
┣ 🖼️ sample_output.png # Output frame (optional)
┗ 🎞️ sample_output.gif # Demo animation (optional)

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/Parking-Spot-Detection.git
cd Parking-Spot-Detection
```
2️⃣ (Optional) Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
```
```bash
python -m venv venv
venv\Scripts\activate         # Windows
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Download Model Weights
Download the YOLOv10 small weights from the official Ultralytics repositoryand place the file as:

```bash
yolov10s.pt
```
5️⃣ Run the Project
```bash
python model.py
```
Press ESC to exit the live window.

📊 Output Preview
When running:

🟢 Green Polygons — Empty parking slots

🔴 Red Polygons — Occupied slots

🔢 Top-left counter — Total available spaces

<p align="center"> <img src="assets/sample_output.png" alt="Detected Output" width="700"/> </p>
🧩 Technical Details
Component	Description
Framework	Ultralytics YOLOv10
Libraries Used	OpenCV, NumPy, Pandas
Input Source	Video footage (.mp4)
Detection Logic	Centroid inside polygon check using cv2.pointPolygonTest()
Output	Dynamic visualization of slot occupancy

📘 Requirements
Example requirements.txt:
```bash
txt
Copy code
opencv-python
ultralytics
pandas
numpy
```
Install all dependencies with:
```bash
pip install -r requirements.txt
```
🚀 Future Enhancements
🧭 Interactive zone selection (mouse-based region marking)

🌐 IoT integration for real-time parking monitoring dashboards

📱 Mobile/web app interface for parking space display

📈 Analytics system for long-term parking trends

👨‍💻 Author
Ansh Patel
🎓 RV College of Engineering — Semester 1 Project
💡 Domain: Computer Vision & Smart IoT Systems
📬 Feel free to reach out for collaboration or improvements!

🪪 License
This project is licensed under the MIT License — you're free to use, modify, and share it with proper credit.

```vbnet
MIT License

Copyright (c) 2025 Ansh Patel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
💬 Contributing
Contributions, pull requests, and feature ideas are always welcome!
If you find this project useful, don’t forget to give it a ⭐ on GitHub 😊

🏁 Quick Commands Reference
Task	Command
Clone the repo	``` git clone <repo-url> ```
Install dependencies ```pip install -r requirements.txt```
Run the project	```python model.py ```
Exit the window	Press ESC

<p align="center"> 🚘 <b>Smart Parking Detection System – by Ansh Patel</b><br> Made with ❤️ using Python, YOLOv10, and OpenCV </p> ```

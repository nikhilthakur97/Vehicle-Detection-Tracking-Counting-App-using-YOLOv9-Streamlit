
# 🚗 Vehicle Detection, Tracking & Counting App using YOLOv9 + Streamlit

![YOLOv9 Vehicle Tracker](https://user-images.githubusercontent.com/your-screenshot.gif)

Welcome to my AI-powered vehicle tracking and counting project!  
Built using **YOLOv9**, **Roboflow**, **OpenCV**, and **Streamlit**, this app allows you to upload a video and instantly see cars, trucks, and motorcycles detected, tracked, and counted in real-time 🚀

---

## 🔍 What This App Does

- ✅ Detects **cars**, **trucks**, and **motorcycles**
- 🧠 Tracks each vehicle with a **unique ID** using BoT-SORT
- 🔢 Counts vehicles as they cross a **virtual line**
- 🎥 Outputs a **processed, downloadable video**
- 🌐 Runs in a **clean Streamlit interface**

---

## 🛠️ Tech Stack

| Tool | Role |
|------|------|
| YOLOv9 | Real-time object detection |
| Roboflow | Dataset management via API |
| Google Colab | Model training platform |
| OpenCV | Drawing, visualization, line logic |
| Streamlit | Web UI for video uploads |
| ByteTrack / BoT-SORT | Object tracking (assigning IDs) |

---

## 📦 How It Works

1. 🔗 Download dataset via Roboflow API
2. 🏋️ Train YOLOv9 in Google Colab on custom data
3. 💾 Export trained weights (`best.pt`)
4. ⚙️ Build local detection app with Streamlit
5. 🎥 Process any uploaded video — detect, track, count

---

## 📸 Screenshots

| Upload Video | Tracked Output |
|--------------|----------------|
| ![Upload Screenshot](runs/vehicle_counted_output.mp4) | ![Output Screenshot](screens/output.png) |

---

## 🚀 How to Run This Project Locally

```bash
# Clone the repo
git clone https://github.com/nikhilthakur97/Vehicle-Detection-Tracking-Counting-App-using-YOLOv9-Streamlit.git
cd vehicle-detection-yolov9

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🎬 Sample Output

Here’s a clip from the app using real traffic footage:  
📹 [Download `vehicle_counted_output.mp4`](vehicle_counted_output.mp4)

---

## 👨‍💻 About the Author

Built with ❤️ by **Nikhil Thakur**  
🔗 [LinkedIn](https://www.linkedin.com/in/nikhil-thakur)

I'm passionate about solving real-world problems using AI and Computer Vision.  
This project is part of my portfolio to demonstrate full-stack AI development — from dataset to deployable app.

---

## 💬 Let’s Connect

📩 Feel free to reach out if you're hiring or working on something exciting in AI/ML/CV!  
I’m actively looking for opportunities.

---

## ⭐ Star the Repo

If you like this project, please consider giving it a ⭐ on GitHub!

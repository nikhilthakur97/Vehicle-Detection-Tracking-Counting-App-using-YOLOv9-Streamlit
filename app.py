# make sure you have the latest version of opencv-python supervision
# pip install streamlit ultralytics opencv-python supervision


import streamlit as st
import cv2
import os
from ultralytics import YOLO
import supervision as sv

st.set_page_config(page_title="Vehicle Detection & Counting", layout="centered")
st.title("🚗 Real-Time Vehicle Detection, Tracking, and Counting (YOLOv9)")

# Load YOLOv9 pretrained model
@st.cache_resource
def load_model():
    # just for easy of everyone using below a pre trained model in case someone wants to use my code 
    return YOLO("yolov9c.pt")

model = load_model()

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    # Save uploaded video
    video_bytes = uploaded_file.read()
    input_path = "uploaded_video.mp4"
    with open(input_path, "wb") as f:
        f.write(video_bytes)

    st.video(input_path)
    st.write("⏳ Processing video... please wait.")

    # Set up video I/O
    cap = cv2.VideoCapture(input_path)
    width, height = int(cap.get(3)), int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)
    output_path = "output_counted.mp4"
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Class ID lookup
    class_ids = {name: idx for idx, name in model.names.items()}
    track_classes = {"car", "truck"}
    count_by_class = {cls: 0 for cls in track_classes}
    counted_ids = set()
    line_y = height // 2

    tracker = sv.ByteTrack()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)[0]
        detections = sv.Detections.from_ultralytics(results)

        # Filter detections to only car and truck
        filtered = detections[[model.names[int(cls)] in track_classes for cls in detections.class_id]]
        tracked = tracker.update_with_detections(filtered)

        for det, track_id, cls_id in zip(tracked.xyxy, tracked.tracker_id, tracked.class_id):
            label = model.names[int(cls_id)]
            x1, y1, x2, y2 = map(int, det)
            center_y = (y1 + y2) // 2

            # Count when crossing line
            if track_id not in counted_ids and line_y - 10 < center_y < line_y + 10:
                counted_ids.add(track_id)
                if label in count_by_class:
                    count_by_class[label] += 1

            # Draw box and label
            color = (0, 255, 0) if label == "car" else (255, 0, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label.capitalize()} #{track_id}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # Draw counting line
        cv2.line(frame, (0, line_y), (width, line_y), (0, 0, 255), 2)

        # Show count overlay
        count_text = " | ".join([f"{k.capitalize()}: {v}" for k, v in count_by_class.items()])
        cv2.putText(frame, f"Total Passed - {count_text}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

        out.write(frame)

    cap.release()
    out.release()

    # Show result
    st.success("✅ Processing complete!")
    st.video(output_path)

    with open(output_path, "rb") as file:
        st.download_button("📥 Download Counted Video", file, file_name="vehicle_counted_output.mp4", mime="video/mp4")

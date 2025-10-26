import tensorflow as tf
import cv2

# Load model once at startup
model = tf.keras.models.load_model("deepfake_detection_model.h5")

def extract_frames_from_video(video_path, max_frames=10, resize_shape=(128, 128)):
    frames = []
    cap = cv2.VideoCapture(video_path)
    count = 0
    while cap.isOpened() and count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, resize_shape)
        frames.append(frame)
        count += 1
    cap.release()
    return frames

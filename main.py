from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
import cv2
import tempfile
import tensorflow as tf
from model_loader import model, extract_frames_from_video

app = FastAPI(title="Deepfake Detection API")

# Allow CORS (for Streamlit frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Save uploaded video temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    frames = extract_frames_from_video(tmp_path)
    frames = np.array(frames).astype('float32') / 255.0
    preds = model.predict(frames)
    avg_pred = preds.mean()
    label = "FAKE" if avg_pred >= 0.5 else "REAL"

    return {"label": label, "confidence": float(avg_pred)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

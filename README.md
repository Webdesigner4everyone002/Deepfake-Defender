
# 🎭  Deepfake-Defender 

A full-stack application for **Deepfake Video Detection**, built using a **FastAPI backend** (for model inference) and a **Streamlit frontend** (for user interaction and visualization).

---

## 🚀 Project Overview

This project allows users to upload a short video clip and get a prediction on whether it is **REAL** or **FAKE**, using a pre-trained deep learning model.

---

## 🏗️ Tech Stack

| Layer | Technology |
|--------|-------------|
| **Backend API** | FastAPI |
| **Frontend UI** | Streamlit |
| **Model Framework** | TensorFlow / Keras |
| **Helper Libraries** | OpenCV, NumPy, Requests |
| **Language** | Python 3.8+ |

---

## 🧩 Folder Structure

deepfake_app/
│
├── backend/
│ ├── main.py # FastAPI backend server
│ ├── model_loader.py # Loads the trained model
│ ├── requirements.txt # Backend dependencies
│ └── deepfake_detection_model.h5 # (Download from Google Drive)
│
├── frontend/
│ ├── app.py # Streamlit frontend


---

## 🧠 Model Download

The trained model file (`deepfake_detection_model.h5`) is stored on Google Drive.  
Please **download it** manually and place it inside the `backend/` directory.

🔗 **Download here:**  
[deepfake_detection_model.h5](https://drive.google.com/file/d/1fvOHZZNCS7SoXfl8EnJHQ_PzWyRfQ5aG/view?usp=drive_link)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/deepfake_app.git
cd deepfake_app
Backend Setup (FastAPI)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
The backend will run on: http://127.0.0.1:8000

You can test it using the Swagger UI at: http://127.0.0.1:8000/docs
Frontend Setup (Streamlit)
cd frontend
pip install streamlit requests
streamlit run app.py

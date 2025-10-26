import streamlit as st
import requests
import tempfile

API_URL = "http://127.0.0.1:8000/predict"

st.title("🎭 Deepfake Detection App")
st.markdown("Upload a short video clip to check if it's **Real** or **Fake**.")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_file:
    st.video(uploaded_file)

    if st.button("Analyze Video"):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        with open(tmp_path, "rb") as f:
            files = {"file": (uploaded_file.name, f, "video/mp4")}
            with st.spinner("Analyzing video..."):
                response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            data = response.json()
            st.success(f"Prediction: **{data['label']}**")
            st.metric(label="Confidence", value=f"{data['confidence']:.3f}")
        else:
            st.error("Error during prediction. Check backend logs.")

import streamlit as st
from transformers import AutoModelForImageClassification, AutoImageProcessor
from PIL import Image
import torch

st.set_page_config(page_title="NSFW Image Detector", page_icon="🕵️")
st.title("🕵️ NSFW Image Detection App")
st.write("Upload gambar dan lihat apakah gambar tersebut **NSFW** atau **Normal**.")

@st.cache_resource
def load_model():
    model = AutoModelForImageClassification.from_pretrained("Falconsai/nsfw_image_detection")
    processor = AutoImageProcessor.from_pretrained("Falconsai/nsfw_image_detection")
    return model, processor

model, processor = load_model()

# Upload file
uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Gambar yang diupload", use_column_width=True)


    with st.spinner("Menganalisis gambar..."):
        inputs = processor(images=img, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=-1)[0]
        pred_idx = torch.argmax(probs).item()
        label = model.config.id2label[pred_idx]
        confidence = probs[pred_idx].item()

    # Hasil prediksi
    st.markdown("---")
    st.subheader("Hasil Deteksi:")
    if label.lower() == "nsfw":
        st.error(f"⚠️ **NSFW Detected** (Confidence: {confidence:.2%})")
    else:
        st.success(f"✅ **Normal Image** (Confidence: {confidence:.2%})")

    # Detail probabilitas
    st.write("**Detail probabilitas:**")
    for i, (lbl, val) in enumerate(model.config.id2label.items()):
        st.write(f"- {val}: {probs[i].item():.2%}")

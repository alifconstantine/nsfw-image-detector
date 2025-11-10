NSFW Image Detection App

Aplikasi berbasis Streamlit untuk mendeteksi apakah sebuah gambar termasuk NSFW (Not Safe For Work) atau Normal, menggunakan model machine learning dari Hugging Face — Falconsai/nsfw_image_detection.

🚀 Fitur Utama

- 🧠 Deteksi Otomatis NSFW menggunakan model pretrained.

- 📤 Upload Gambar langsung melalui antarmuka Streamlit.

- ⚡ Prediksi Cepat dengan visualisasi tingkat kepercayaan.

- 💡 Antarmuka Sederhana dan mudah digunakan.


🧩 Teknologi yang Digunakan

- Streamlit
 – Untuk UI interaktif berbasis web.

- Transformers (Hugging Face)
 – Untuk pemrosesan model deep learning.

- PyTorch
 – Backend model machine learning.

- Pillow (PIL)
 – Untuk membaca dan menampilkan gambar.

📦 Instalasi
1️⃣ Clone repository
```bash
git clone https://github.com/alifconstantine/nsfw-image-detector.git
cd nsfw--image-detector
```

2️⃣ Buat virtual environment (opsional tapi direkomendasikan)
```bash
python -m venv venv
source venv/bin/activate   # untuk macOS/Linux
venv\Scripts\activate      # untuk Windows
```

3️⃣ Instal dependencies
```bash
pip install -r requirements.txt
```
▶️ Cara Menjalankan Aplikasi

Setelah semua dependensi terinstal, jalankan perintah berikut:
```bash
streamlit run app.py
```

Aplikasi akan otomatis terbuka di browser (biasanya di http://localhost:8501).

🖼️ Cara Menggunakan

1. Jalankan aplikasi Streamlit.

2. Upload gambar berformat .jpg, .jpeg, atau .png.

3. Tunggu hasil analisis:

    - 🔴 NSFW Detected → gambar mengandung konten tidak pantas.

    - 🟢 Normal Image → gambar aman.

📁 Struktur Folder
```bash
.
├── app.py                # File utama Streamlit
├── requirements.txt      # Daftar dependensi
└── README.md             # Dokumentasi proyek
```
⚠️ Disclaimer

Model ini tidak 100% akurat.
Gunakan hanya untuk tujuan edukasi atau penelitian, bukan untuk moderasi produksi tanpa evaluasi tambahan.

👨‍💻 Author
    - Alif Constantine

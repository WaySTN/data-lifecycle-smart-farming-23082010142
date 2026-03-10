# 🌾 Data Lifecycle Smart Farming - Big Data & IoT

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://data-lifecycle-smart-farming-23082010142-nywc9n4cyfsjdvfgv7wnn.streamlit.app/)

## 📋 Deskripsi Proyek

Proyek ini merupakan tugas mata kuliah **Big Data & IoT** yang mengimplementasikan **Data Lifecycle** lengkap pada dataset **Smart Agriculture** dari sensor IoT untuk monitoring tanaman. Proyek mencakup seluruh siklus hidup data: mulai dari akuisisi, eksplorasi, pembersihan, analisis, visualisasi, hingga deployment dashboard interaktif.

### 🔗 Live Dashboard
👉 **[Buka Dashboard](https://data-lifecycle-smart-farming-23082010142-nywc9n4cyfsjdvfgv7wnn.streamlit.app/)**

---

## 📊 Dataset

| Informasi | Detail |
|-----------|--------|
| **Nama** | Smart Agriculture Dataset |
| **Sumber** | [Kaggle - Smart Agriculture Dataset](https://kaggle.com/datasets/chaitanyagopidesi/smart-agriculture-dataset) |
| **Konteks** | Monitoring tanaman menggunakan sensor IoT |
| **Jumlah Baris** | 16.412 |
| **Jumlah Kolom** | 7 (+ 1 kolom timestamp hasil cleaning) |

### Kolom Dataset

| Kolom | Tipe | Deskripsi |
|-------|------|-----------|
| `crop ID` | Kategorikal | Jenis tanaman (Wheat, Rice, Chilli, Potato, dll) |
| `soil_type` | Kategorikal | Jenis tanah (Black, Red, Clay, Sandy, Loam, dll) |
| `Seedling Stage` | Kategorikal | Tahap pertumbuhan (Germination, Flowering, Harvest, dll) |
| `MOI` | Numerik | Moisture of Irrigation (kelembaban irigasi) |
| `temp` | Numerik | Temperature / Suhu (°C) |
| `humidity` | Numerik | Kelembaban udara (%) |
| `result` | Numerik | Hasil panen (0 = gagal, 1 = normal, 2 = baik) |

---

## 📁 Struktur Folder

```
data-lifecycle-smart-farming-23082010142/
|-- README.md                              <- Dokumentasi (file ini)
|-- requirements.txt                       <- Dependencies untuk deployment
|-- Data_Lifecycle_Smart_Farming.ipynb     <- Notebook analisis utama
|-- data/
|   `-- raw/
|       `-- smart_farming_sensor_data.csv  <- Dataset mentah dari Kaggle
|-- dashboard/
|   `-- streamlit_app.py                   <- Dashboard interaktif Streamlit
`-- outputs/
    |-- analysis_report.pdf                <- Laporan analisis lengkap (PDF)
    |-- boxplot_per_crop.png               <- Boxplot per jenis tanaman
    |-- cleaned_data.csv                   <- Data yang sudah dibersihkan
    |-- correlation_heatmap.png            <- Heatmap korelasi sensor
    |-- dashboard_screenshoot.png          <- Screenshot dashboard (halaman pertama)
    |-- data_quality_score.png             <- Visualisasi skor kualitas data
    |-- distribusi_soil_type.png           <- Distribusi crop per jenis tanah
    |-- eda_distributions.png              <- Visualisasi distribusi EDA
    `-- timeseries_trend.png               <- Trend time series sensor
```

---

## 🚀 Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/WaySTN/data-lifecycle-smart-farming-23082010142.git
cd data-lifecycle-smart-farming-23082010142
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan Notebook
Buka `Data_Lifecycle_Smart_Farming.ipynb` di **Jupyter Notebook**, **VS Code**, atau **Google Colab**.

### 4. Jalankan Dashboard Lokal
```bash
streamlit run dashboard/streamlit_app.py
```
Dashboard akan terbuka di `http://localhost:8501`

---

## 📈 Tahapan Data Lifecycle

### 1️⃣ Data Acquisition (Setup)
- Dataset diunduh dari Kaggle (Smart Agriculture Dataset)
- Raw data disimpan di `data/raw/smart_farming_sensor_data.csv`
- Repository dibuat di GitHub untuk version control

### 2️⃣ Exploratory Data Analysis (EDA)
- **`df.describe()`** — Statistik deskriptif (mean, std, min, max, quartiles)
- **`df.isnull().sum()`** — Pengecekan missing values
- **Value Counts** — Distribusi per kolom kategorikal (crop, soil, stage)
- **Visualisasi** — Histogram distribusi Temperature, Humidity, MOI, Result

### 3️⃣ Data Cleaning
| Proses | Metode | Keterangan |
|--------|--------|-----------|
| Missing Values | Median (numerik) / Mode (kategorikal) | Mengisi data kosong |
| Outliers | IQR Method (cap, bukan hapus) | Menjaga jumlah data tetap utuh |
| Timestamp | Simulasi sensor IoT (interval 15 menit) | Untuk perhitungan Timeliness |

> **Catatan:** Dataset asli tidak memiliki kolom timestamp, sehingga ditambahkan simulasi timestamp dengan asumsi data sensor diambil setiap 15 menit.

### 4️⃣ Analisis & Visualisasi
- **Correlation Heatmap** — Korelasi antar variabel sensor
- **Time Series Trend** — Trend temperature, humidity, MOI over time
- **Boxplot per Crop** — Distribusi sensor per jenis tanaman
- **Distribusi Soil Type** — Jumlah data per jenis tanah

#### Temuan Utama
| Korelasi | Nilai | Interpretasi |
|----------|-------|-------------|
| temp ↔ humidity | **-0.976** | Korelasi negatif sangat kuat |
| temp ↔ result | **+0.542** | Korelasi positif sedang |
| humidity ↔ result | **-0.499** | Korelasi negatif sedang |
| MOI ↔ result | **-0.053** | Tidak ada korelasi signifikan |

### 5️⃣ Data Quality Score

| Metrik | Rumus | Hasil |
|--------|-------|-------|
| **Accuracy** | `1 - (missing/total)` | **100.00%** |
| **Completeness** | `non-null/total` | **100.00%** |
| **Timeliness** | `% data dalam 30 hari terakhir` | **~100.00%** |
| **Overall** | `Rata-rata 3 metrik` | **~100.00%** |

### 6️⃣ Dashboard & Deployment
- Dashboard interaktif dibangun dengan **Streamlit**
- Fitur: Filter (Crop, Soil, Stage), Distribusi, Heatmap, Boxplot, Time Series, Data Quality
- **Deployed** di Streamlit Cloud: [Live Dashboard](https://data-lifecycle-smart-farming-23082010142-nywc9n4cyfsjdvfgv7wnn.streamlit.app/)

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Versi | Kegunaan |
|-----------|-------|----------|
| Python | 3.x | Bahasa pemrograman utama |
| Pandas | ≥ 2.0.0 | Manipulasi & analisis data |
| NumPy | ≥ 1.24.0 | Komputasi numerik |
| Matplotlib | ≥ 3.7.0 | Visualisasi dasar |
| Seaborn | ≥ 0.12.0 | Visualisasi statistik |
| Streamlit | ≥ 1.30.0 | Dashboard interaktif & deployment |
| Jupyter Notebook | - | Environment analisis data |

---

## 📝 Kesimpulan

1. Dataset Smart Agriculture memiliki **16.412 baris** data sensor IoT dari **5 jenis tanaman** dan **7 jenis tanah**
2. Dataset memiliki **kualitas data sangat tinggi** (Accuracy & Completeness 100%) tanpa missing values
3. Ditemukan **korelasi negatif sangat kuat** antara temperature dan humidity (-0.976)
4. **Temperature berpengaruh positif** terhadap hasil panen (korelasi +0.542)
5. Dashboard Streamlit berhasil di-deploy dan dapat diakses secara online untuk eksplorasi data interaktif

---

**Mata Kuliah:** Big Data & IoT  
**Nama:** wahyu setiawan  
**NPM:** 23082010142  
**Tahun:** 2026

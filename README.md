# 🌾 Data Lifecycle Smart Farming - Big Data & IoT

## 📋 Deskripsi Proyek

Proyek ini merupakan tugas mata kuliah **Big Data & IoT** yang mengimplementasikan **Data Lifecycle** pada dataset **Smart Agriculture** dari sensor IoT untuk monitoring tanaman.

### Dataset yang Digunakan
- **Nama:** Smart Agriculture Dataset
- **Sumber:** [Kaggle - Smart Agriculture Dataset](https://kaggle.com/datasets/chaitanyagopidesi/smart-agriculture-dataset)
- **Konteks:** Monitoring tanaman menggunakan sensor IoT
- **Kolom Utama:** crop ID, soil_type, Seedling Stage, MOI, temp, humidity, result

### Informasi Dataset
| Informasi | Detail |
|-----------|--------|
| Jumlah Baris | 16.412 |
| Jumlah Kolom | 7 |
| Crop Types | Wheat, Rice, Maize, dll |
| Soil Types | Black Soil, Red Soil, dll |
| Growth Stages | Germination, Seedling, Flowering, Harvest, dll |

---

## 📁 Struktur Folder

```
data-lifecycle-smart-farming-[NIM]/
├── README.md                              ← Dokumentasi (file ini)
├── Data_Lifecycle_Smart_Farming.py        ← Script utama (bisa dijalankan di Jupyter/Colab)
├── data/
│   └── raw/
│       └── smart_farming_sensor_data.csv  ← Dataset mentah
├── dashboard/
│   └── streamlit_app.py                   ← Dashboard interaktif
└── outputs/
    ├── cleaned_data.csv                   ← Data yang sudah dibersihkan
    ├── eda_distributions.png              ← Visualisasi EDA
    ├── correlation_heatmap.png            ← Heatmap korelasi
    ├── timeseries_trend.png               ← Trend time series
    ├── boxplot_per_crop.png               ← Boxplot per tanaman
    ├── distribusi_soil_type.png           ← Distribusi jenis tanah
    └── data_quality_score.png             ← Skor kualitas data
```

---

## 🚀 Cara Menjalankan

### 1. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn streamlit
```

### 2. Jalankan Script Analisis
```bash
python Data_Lifecycle_Smart_Farming.py
```

Atau buka file `.py` di **Jupyter Notebook / VS Code** (support `# %%` cell markers) atau copy ke **Google Colab**.

### 3. Jalankan Dashboard Streamlit
```bash
streamlit run dashboard/streamlit_app.py
```

---

## 📊 Tahapan Data Lifecycle

### 1. Data Acquisition (Setup)
- Dataset diunduh dari Kaggle
- Raw data disimpan di `data/raw/smart_farming_sensor_data.csv`

### 2. Exploratory Data Analysis (EDA)
- `df.describe()` - Statistik deskriptif
- `df.isnull().sum()` - Cek missing values
- Value counts per kolom kategorikal
- Visualisasi distribusi data sensor

### 3. Data Cleaning
- **Handle Missing Values:** Isi dengan median (numerik) dan mode (kategorikal)
- **Handle Outliers:** Metode IQR (cap, bukan hapus)
- **Format Datetime:** Tambah kolom `timestamp` (simulasi sensor IoT, interval 15 menit)

### 4. Analisis & Visualisasi
- **Correlation Heatmap:** Korelasi antar variabel sensor
- **Time Series Trend:** Trend temperature, humidity, MOI
- **Boxplot per Crop:** Distribusi sensor per jenis tanaman
- **Distribusi Soil Type:** Jumlah data per jenis tanah

### 5. Data Quality Score

| Metrik | Rumus | Hasil |
|--------|-------|-------|
| **Accuracy** | 1 - (missing/total) | ~100% |
| **Completeness** | non-null/total | ~100% |
| **Timeliness** | % data dalam 30 hari terakhir | ~100% |
| **Overall** | Rata-rata 3 metrik | ~100% |

### 6. Dashboard (Streamlit)
Dashboard interaktif dengan fitur:
- Filter per Crop, Soil Type, Growth Stage
- Visualisasi distribusi, heatmap, boxplot, time series
- Tampilan Data Quality Score

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Kegunaan |
|-----------|----------|
| Python 3.x | Bahasa pemrograman utama |
| Pandas | Manipulasi & analisis data |
| NumPy | Komputasi numerik |
| Matplotlib | Visualisasi dasar |
| Seaborn | Visualisasi statistik |
| Streamlit | Dashboard interaktif |

---

## 📝 Kesimpulan

1. Dataset Smart Agriculture memiliki **16.412 baris** data sensor IoT dari berbagai jenis tanaman
2. Data memiliki **kualitas tinggi** dengan sedikit/tanpa missing values
3. Terdapat korelasi antara variabel sensor (suhu, kelembaban, MOI) dengan hasil panen
4. Dashboard Streamlit memungkinkan eksplorasi data secara interaktif

---

**Mata Kuliah:** Big Data & IoT  
**Tahun:** 2025

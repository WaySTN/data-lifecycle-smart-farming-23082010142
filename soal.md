# TUGAS
# MATA KULIAH BIG DATA & IOT
# Smart Farming Dashboard dari Sensor IoT

---

## Pilih 1 dataset sensor IoT dari Kaggle berikut (prioritas urutan 1-3)

| No | Dataset | Link Kaggle | Konteks | Kolom Utama |
|----|---------|-------------|---------|-------------|
| 1 | Smart Farming Sensor Data | kaggle.com/datasets/atharvasoundankar/smart-farming-sensor-data-for-yield-prediction | Sensor IoT pertanian | Soil Moisture, Temperature, Humidity, pH, Yield |
| 2 | Soil Moisture Dataset | kaggle.com/datasets/amirmohammdjalili/soil-moisture-dataset | Kelembaban tanah multi-layer | Soil Moisture (berbagai kedalaman), Time |
| 3 | Smart Agriculture Dataset | kaggle.com/datasets/chaitanyagopidesi/smart-agriculture-dataset | Monitoring tanaman | MOI, Temperature, Humidity, Soil Type |

---

**Saya Pilih no 3 :**

- **Dataset :** Smart Agriculture
- **Link Kaggle :** kaggle.com/datasets/chaitanyagopidesi/smart-agriculture-dataset
- **Konteks :** Monitoring tanaman
- **Kolom Utama :** MOI, Temperature, Humidity, Soil Type

---

## Gunakan Jupyter Notebook / Google Colab

## Strukturnya harus seperti ini, upload di GitHub :

```
repo_github/
├── README.md (dokumentasi)
├── data/raw/smart_farming_sensor_data.csv
├── Data_Lifecycle_Smart_Farming.ipynb  ← UTAMA
├── dashboard/
│   └── streamlit_app.py (atau PowerBI.pbix)
└── outputs/
    ├── cleaned_data.csv
    ├── analysis_report.pdf
    └── dashboard_screenshot.png
```

---

## Setup & Acquisition

1. Daftar akun Kaggle (kaggle.com)
2. Download dataset via API:
   ```
   kaggle datasets download -d atharvasoundankar/smart-farming-sensor-data-for-yield-prediction
   ```
3. Buat GitHub repo: `data-lifecycle-smart-farming-[NIM]`
4. Upload raw data ke repo

---

## Visualization & Dashboard

1. Buka Jupyter Notebook / Google Colab
2. EDA lengkap: `df.describe()`, `df.isnull().sum()`
3. Cleaning: handle missing, outliers, format datetime
4. Analisis: correlation heatmap, time series trend
5. Simpan `cleaned_data.csv`

---

## Dokumentasi & Governance

1. Hitung Data Quality Score:
   - **Accuracy** = 1 - (missing/total)
   - **Completeness** = (non-null/total)
   - **Timeliness** = % data dalam 30 hari terakhir
2. Buat `README.md` lengkap
3. Screenshot dashboard & hasil analisis

---

**KUMPULKAN LAPORAN DAN LINK GITHUB**
```

# =============================================================================
# DATA LIFECYCLE SMART FARMING - BIG DATA & IOT
# =============================================================================
# Dataset: Smart Agriculture Dataset
# Sumber: Kaggle - Smart Agriculture Dataset
# Konteks: Monitoring tanaman menggunakan sensor IoT
# Kolom Utama: MOI, Temperature, Humidity, Soil Type, crop ID, Seedling Stage
# =============================================================================

# %% [markdown]
# # 🌾 Data Lifecycle Smart Farming
# ## Mata Kuliah: Big Data & IoT
# ---

# %% [markdown]
# ## 1. Setup & Acquisition
# Import library yang diperlukan dan load dataset

# %%
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import os
import warnings
warnings.filterwarnings('ignore')

# Styling
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12

print("=" * 60)
print("DATA LIFECYCLE SMART FARMING - BIG DATA & IoT")
print("=" * 60)

# %%
# Load dataset
df = pd.read_csv('data/raw/smart_farming_sensor_data.csv')
print(f"\n✅ Dataset berhasil dimuat!")
print(f"📊 Jumlah baris: {df.shape[0]}")
print(f"📊 Jumlah kolom: {df.shape[1]}")

# %% [markdown]
# ## 2. Exploratory Data Analysis (EDA)
# Analisis awal untuk memahami struktur dan karakteristik data

# %%
print("\n" + "=" * 60)
print("📋 INFORMASI DATASET")
print("=" * 60)
print(f"\nKolom-kolom: {list(df.columns)}")
print(f"\nTipe Data:")
print(df.dtypes)

# %%
print("\n" + "=" * 60)
print("📊 STATISTIK DESKRIPTIF - df.describe()")
print("=" * 60)
print(df.describe())

# %%
print("\n" + "=" * 60)
print("🔍 CEK MISSING VALUES - df.isnull().sum()")
print("=" * 60)
print(df.isnull().sum())
print(f"\nTotal missing values: {df.isnull().sum().sum()}")

# %%
print("\n" + "=" * 60)
print("📈 VALUE COUNTS PER KOLOM KATEGORIKAL")
print("=" * 60)

print("\n--- Distribusi Crop ID ---")
print(df['crop ID'].value_counts())

print("\n--- Distribusi Soil Type ---")
print(df['soil_type'].value_counts())

print("\n--- Distribusi Seedling Stage ---")
print(df['Seedling Stage'].value_counts())

print("\n--- Distribusi Result ---")
print(df['result'].value_counts())

# %%
# Visualisasi EDA
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Exploratory Data Analysis - Smart Farming Dataset', fontsize=16, fontweight='bold')

# 1. Distribusi Temperature
axes[0, 0].hist(df['temp'], bins=30, color='#FF6B6B', edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Distribusi Temperature (°C)', fontweight='bold')
axes[0, 0].set_xlabel('Temperature')
axes[0, 0].set_ylabel('Frekuensi')

# 2. Distribusi Humidity
axes[0, 1].hist(df['humidity'], bins=30, color='#4ECDC4', edgecolor='black', alpha=0.7)
axes[0, 1].set_title('Distribusi Humidity (%)', fontweight='bold')
axes[0, 1].set_xlabel('Humidity')
axes[0, 1].set_ylabel('Frekuensi')

# 3. Distribusi MOI (Moisture of Irrigation)
axes[1, 0].hist(df['MOI'], bins=30, color='#45B7D1', edgecolor='black', alpha=0.7)
axes[1, 0].set_title('Distribusi MOI', fontweight='bold')
axes[1, 0].set_xlabel('MOI')
axes[1, 0].set_ylabel('Frekuensi')

# 4. Distribusi Crop per Result
result_crop = df.groupby(['crop ID', 'result']).size().unstack(fill_value=0)
result_crop.plot(kind='bar', stacked=True, ax=axes[1, 1], colormap='Set2')
axes[1, 1].set_title('Distribusi Result per Crop', fontweight='bold')
axes[1, 1].set_xlabel('Crop')
axes[1, 1].set_ylabel('Jumlah')
axes[1, 1].tick_params(axis='x', rotation=45)
axes[1, 1].legend(title='Result')

plt.tight_layout()
os.makedirs('outputs', exist_ok=True)
plt.savefig('outputs/eda_distributions.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Visualisasi EDA disimpan ke outputs/eda_distributions.png")

# %% [markdown]
# ## 3. Data Cleaning
# Pembersihan data: handle missing values, outliers, tambah timestamp

# %%
print("\n" + "=" * 60)
print("🧹 DATA CLEANING")
print("=" * 60)

df_cleaned = df.copy()

# 3a. Cek dan Handle Missing Values
missing_before = df_cleaned.isnull().sum().sum()
print(f"\nMissing values sebelum cleaning: {missing_before}")

# Isi missing values numerik dengan median
numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    if df_cleaned[col].isnull().sum() > 0:
        df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)
        print(f"  → Kolom '{col}': missing values diisi dengan median")

# Isi missing values kategorikal dengan mode
cat_cols = df_cleaned.select_dtypes(include=['object']).columns
for col in cat_cols:
    if df_cleaned[col].isnull().sum() > 0:
        df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)
        print(f"  → Kolom '{col}': missing values diisi dengan mode")

missing_after = df_cleaned.isnull().sum().sum()
print(f"Missing values setelah cleaning: {missing_after}")

# %%
# 3b. Handle Outliers menggunakan metode IQR
print("\n--- Handle Outliers (IQR Method) ---")
outlier_cols = ['MOI', 'temp', 'humidity']
outliers_removed = 0

for col in outlier_cols:
    Q1 = df_cleaned[col].quantile(0.25)
    Q3 = df_cleaned[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    outliers = ((df_cleaned[col] < lower) | (df_cleaned[col] > upper)).sum()
    outliers_removed += outliers
    
    # Cap outliers (bukan hapus, agar data tetap lengkap)
    df_cleaned[col] = df_cleaned[col].clip(lower=lower, upper=upper)
    print(f"  → Kolom '{col}': {outliers} outliers di-cap (range: {lower:.2f} - {upper:.2f})")

print(f"Total outliers yang ditangani: {outliers_removed}")

# %%
# 3c. Tambah kolom Timestamp (simulasi sensor IoT)
print("\n--- Menambahkan Kolom Timestamp ---")

# Simulasi: data sensor diambil setiap 15 menit mulai dari 30 hari lalu
base_time = datetime.now() - timedelta(days=30)
timestamps = [base_time + timedelta(minutes=15 * i) for i in range(len(df_cleaned))]
df_cleaned['timestamp'] = timestamps
df_cleaned['timestamp'] = pd.to_datetime(df_cleaned['timestamp'])

print(f"  → Timestamp ditambahkan: {df_cleaned['timestamp'].min()} sampai {df_cleaned['timestamp'].max()}")
print(f"  → Interval: setiap 15 menit")

# %%
# 3d. Rename kolom agar lebih konsisten
df_cleaned.columns = df_cleaned.columns.str.strip()
print(f"\n✅ Data setelah cleaning: {df_cleaned.shape[0]} baris, {df_cleaned.shape[1]} kolom")
print(f"Kolom: {list(df_cleaned.columns)}")

# %% [markdown]
# ## 4. Analisis & Visualisasi
# Correlation heatmap, time series trend, analisis per crop

# %%
print("\n" + "=" * 60)
print("📊 ANALISIS & VISUALISASI")
print("=" * 60)

# 4a. Correlation Heatmap
fig, ax = plt.subplots(figsize=(10, 8))
numeric_data = df_cleaned[['MOI', 'temp', 'humidity', 'result']].corr()
mask = np.triu(np.ones_like(numeric_data, dtype=bool))
sns.heatmap(numeric_data, annot=True, fmt='.3f', cmap='coolwarm',
            mask=mask, center=0, square=True, linewidths=1,
            cbar_kws={"shrink": 0.8}, ax=ax)
ax.set_title('Correlation Heatmap - Sensor Data', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('outputs/correlation_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Correlation Heatmap disimpan ke outputs/correlation_heatmap.png")

print("\nMatriks Korelasi:")
print(numeric_data)

# %%
# 4b. Time Series Trend (simulasi, menggunakan rolling average)
fig, axes = plt.subplots(3, 1, figsize=(16, 12))
fig.suptitle('Time Series Trend - Sensor Data (Rolling Average 100)', fontsize=14, fontweight='bold')

# Plot subset agar lebih readable (1000 data points pertama)
subset = df_cleaned.head(1000).copy()

axes[0].plot(subset['timestamp'], subset['temp'].rolling(10).mean(), color='#FF6B6B', linewidth=1.5)
axes[0].set_title('Temperature Trend', fontweight='bold')
axes[0].set_ylabel('Temperature (°C)')
axes[0].fill_between(subset['timestamp'], subset['temp'].rolling(10).mean(), alpha=0.2, color='#FF6B6B')

axes[1].plot(subset['timestamp'], subset['humidity'].rolling(10).mean(), color='#4ECDC4', linewidth=1.5)
axes[1].set_title('Humidity Trend', fontweight='bold')
axes[1].set_ylabel('Humidity (%)')
axes[1].fill_between(subset['timestamp'], subset['humidity'].rolling(10).mean(), alpha=0.2, color='#4ECDC4')

axes[2].plot(subset['timestamp'], subset['MOI'].rolling(10).mean(), color='#45B7D1', linewidth=1.5)
axes[2].set_title('MOI (Moisture) Trend', fontweight='bold')
axes[2].set_ylabel('MOI')
axes[2].set_xlabel('Timestamp')
axes[2].fill_between(subset['timestamp'], subset['MOI'].rolling(10).mean(), alpha=0.2, color='#45B7D1')

for ax in axes:
    ax.tick_params(axis='x', rotation=30)

plt.tight_layout()
plt.savefig('outputs/timeseries_trend.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Time Series Trend disimpan ke outputs/timeseries_trend.png")

# %%
# 4c. Boxplot per Crop
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('Boxplot Sensor Data per Crop', fontsize=14, fontweight='bold')

sns.boxplot(data=df_cleaned, x='crop ID', y='temp', ax=axes[0], palette='Set2')
axes[0].set_title('Temperature per Crop', fontweight='bold')
axes[0].tick_params(axis='x', rotation=45)

sns.boxplot(data=df_cleaned, x='crop ID', y='humidity', ax=axes[1], palette='Set2')
axes[1].set_title('Humidity per Crop', fontweight='bold')
axes[1].tick_params(axis='x', rotation=45)

sns.boxplot(data=df_cleaned, x='crop ID', y='MOI', ax=axes[2], palette='Set2')
axes[2].set_title('MOI per Crop', fontweight='bold')
axes[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('outputs/boxplot_per_crop.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Boxplot per Crop disimpan ke outputs/boxplot_per_crop.png")

# %%
# 4d. Distribusi per Soil Type
fig, ax = plt.subplots(figsize=(10, 6))
soil_crop = df_cleaned.groupby(['soil_type', 'crop ID']).size().unstack(fill_value=0)
soil_crop.plot(kind='bar', ax=ax, colormap='viridis', edgecolor='black')
ax.set_title('Distribusi Crop per Soil Type', fontsize=14, fontweight='bold')
ax.set_xlabel('Soil Type')
ax.set_ylabel('Jumlah Data')
ax.tick_params(axis='x', rotation=45)
ax.legend(title='Crop', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('outputs/distribusi_soil_type.png', dpi=150, bbox_inches='tight')
plt.close()
print("✅ Distribusi per Soil Type disimpan ke outputs/distribusi_soil_type.png")

# %% [markdown]
# ## 5. Data Quality Score
# Menghitung skor kualitas data: Accuracy, Completeness, Timeliness

# %%
print("\n" + "=" * 60)
print("⭐ DATA QUALITY SCORE")
print("=" * 60)

total_cells = df.shape[0] * df.shape[1]
total_rows = df.shape[0]

# 5a. Accuracy = 1 - (missing / total)
missing_count = df.isnull().sum().sum()
accuracy = 1 - (missing_count / total_cells)
print(f"\n📌 Accuracy = 1 - (missing/total)")
print(f"   = 1 - ({missing_count}/{total_cells})")
print(f"   = {accuracy:.4f} ({accuracy*100:.2f}%)")

# 5b. Completeness = (non-null / total)
non_null_count = df.notna().sum().sum()
completeness = non_null_count / total_cells
print(f"\n📌 Completeness = non-null / total")
print(f"   = {non_null_count}/{total_cells}")
print(f"   = {completeness:.4f} ({completeness*100:.2f}%)")

# 5c. Timeliness = % data dalam 30 hari terakhir
# (Gunakan data cleaned yang sudah ada timestamp)
now = datetime.now()
thirty_days_ago = now - timedelta(days=30)
recent_data = df_cleaned[df_cleaned['timestamp'] >= thirty_days_ago].shape[0]
timeliness = recent_data / total_rows
print(f"\n📌 Timeliness = % data dalam 30 hari terakhir")
print(f"   = {recent_data}/{total_rows}")
print(f"   = {timeliness:.4f} ({timeliness*100:.2f}%)")

# Overall Score
overall_score = (accuracy + completeness + timeliness) / 3
print(f"\n{'='*40}")
print(f"📊 OVERALL DATA QUALITY SCORE")
print(f"{'='*40}")
print(f"   Accuracy    : {accuracy*100:.2f}%")
print(f"   Completeness: {completeness*100:.2f}%")
print(f"   Timeliness  : {timeliness*100:.2f}%")
print(f"   ────────────────────────")
print(f"   Overall     : {overall_score*100:.2f}%")

# Buat visualisasi Data Quality Score
fig, ax = plt.subplots(figsize=(8, 6))
scores = [accuracy * 100, completeness * 100, timeliness * 100, overall_score * 100]
labels = ['Accuracy', 'Completeness', 'Timeliness', 'Overall']
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
bars = ax.barh(labels, scores, color=colors, edgecolor='black', height=0.6)

for bar, score in zip(bars, scores):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
            f'{score:.1f}%', va='center', fontweight='bold', fontsize=12)

ax.set_xlim(0, 115)
ax.set_title('Data Quality Score', fontsize=14, fontweight='bold')
ax.set_xlabel('Score (%)')
ax.axvline(x=80, color='green', linestyle='--', alpha=0.5, label='Target 80%')
ax.legend()
plt.tight_layout()
plt.savefig('outputs/data_quality_score.png', dpi=150, bbox_inches='tight')
plt.close()
print("\n✅ Visualisasi Data Quality Score disimpan ke outputs/data_quality_score.png")

# %% [markdown]
# ## 6. Export Data

# %%
print("\n" + "=" * 60)
print("💾 EXPORT DATA")
print("=" * 60)

os.makedirs('outputs', exist_ok=True)
df_cleaned.to_csv('outputs/cleaned_data.csv', index=False)
print(f"✅ cleaned_data.csv disimpan ke outputs/cleaned_data.csv")
print(f"   Jumlah baris: {df_cleaned.shape[0]}")
print(f"   Jumlah kolom: {df_cleaned.shape[1]}")
print(f"   Kolom: {list(df_cleaned.columns)}")

# %%
print("\n" + "=" * 60)
print("🎉 SELESAI! Semua output telah disimpan.")
print("=" * 60)
print("""
File yang dihasilkan:
├── outputs/
│   ├── cleaned_data.csv
│   ├── eda_distributions.png
│   ├── correlation_heatmap.png
│   ├── timeseries_trend.png
│   ├── boxplot_per_crop.png
│   ├── distribusi_soil_type.png
│   └── data_quality_score.png
""")

# =============================================================================
# STREAMLIT DASHBOARD - SMART FARMING IoT MONITORING
# =============================================================================
# Jalankan dengan: streamlit run dashboard/streamlit_app.py
# =============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import os

# Force white background on all matplotlib charts (agar tidak transparan di dark mode)
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['savefig.facecolor'] = 'white'
plt.rcParams['text.color'] = 'black'
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'

# Page Config
st.set_page_config(
    page_title="🌾 Smart Farming IoT Dashboard",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - fixed for dark mode compatibility
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        padding: 1rem 0;
    }
    [data-testid="stMetric"] {
        background-color: #1E1E2E;
        border: 1px solid #3A3A5A;
        padding: 15px;
        border-radius: 12px;
    }
    [data-testid="stMetric"] label {
        color: #B0B0D0 !important;
    }
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-size: 1.8rem !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# LOAD DATA
# =============================================================================
@st.cache_data
def load_data():
    """Load dan proses dataset"""
    # Coba beberapa path
    possible_paths = [
        'data/raw/smart_farming_sensor_data.csv',
        '../data/raw/smart_farming_sensor_data.csv',
        os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'raw', 'smart_farming_sensor_data.csv')
    ]
    
    df = None
    for path in possible_paths:
        if os.path.exists(path):
            df = pd.read_csv(path)
            break
    
    if df is None:
        st.error("❌ Dataset tidak ditemukan! Pastikan file CSV ada di folder data/raw/")
        st.stop()
    
    # Tambah timestamp (simulasi sensor IoT)
    base_time = datetime.now() - timedelta(days=30)
    df['timestamp'] = [base_time + timedelta(minutes=15 * i) for i in range(len(df))]
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    return df

df = load_data()

# =============================================================================
# SIDEBAR
# =============================================================================
st.sidebar.markdown("## 🌾 Smart Farming Dashboard")
st.sidebar.markdown("---")

# Filter Crop
crop_options = ['Semua'] + sorted(df['crop ID'].unique().tolist())
selected_crop = st.sidebar.selectbox("🌱 Pilih Crop:", crop_options)

# Filter Soil Type
soil_options = ['Semua'] + sorted(df['soil_type'].unique().tolist())
selected_soil = st.sidebar.selectbox("🏔️ Pilih Soil Type:", soil_options)

# Filter Stage
stage_options = ['Semua'] + sorted(df['Seedling Stage'].unique().tolist())
selected_stage = st.sidebar.selectbox("📊 Pilih Growth Stage:", stage_options)

# Apply filters
df_filtered = df.copy()
if selected_crop != 'Semua':
    df_filtered = df_filtered[df_filtered['crop ID'] == selected_crop]
if selected_soil != 'Semua':
    df_filtered = df_filtered[df_filtered['soil_type'] == selected_soil]
if selected_stage != 'Semua':
    df_filtered = df_filtered[df_filtered['Seedling Stage'] == selected_stage]

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Data ditampilkan:** {len(df_filtered):,} baris")
st.sidebar.markdown(f"**Total data:** {len(df):,} baris")

# =============================================================================
# HEADER
# =============================================================================
st.markdown('<div class="main-header">🌾 Smart Farming IoT Dashboard</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Monitoring Data Sensor Pertanian Cerdas - Big Data & IoT</p>", unsafe_allow_html=True)
st.markdown("---")

# =============================================================================
# OVERVIEW METRICS
# =============================================================================
st.subheader("📊 Overview Statistik")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("🌡️ Avg Temperature", f"{df_filtered['temp'].mean():.1f}°C")
with col2:
    st.metric("💧 Avg Humidity", f"{df_filtered['humidity'].mean():.1f}%")
with col3:
    st.metric("🌿 Avg MOI", f"{df_filtered['MOI'].mean():.1f}")
with col4:
    st.metric("🌱 Jumlah Crop", f"{df_filtered['crop ID'].nunique()}")
with col5:
    st.metric("📏 Total Data", f"{len(df_filtered):,}")

st.markdown("---")

# =============================================================================
# VISUALISASI
# =============================================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Distribusi", 
    "🔥 Correlation Heatmap", 
    "📊 Per Crop Analysis",
    "📉 Time Series",
    "⭐ Data Quality"
])

# Tab 1: Distribusi
with tab1:
    st.subheader("📈 Distribusi Data Sensor")
    col1, col2 = st.columns(2)
    
    with col1:
        fig, ax = plt.subplots(figsize=(8, 5), facecolor='white')
        ax.hist(df_filtered['temp'], bins=25, color='#FF6B6B', edgecolor='black', alpha=0.7)
        ax.set_title('Distribusi Temperature (°C)', fontweight='bold')
        ax.set_xlabel('Temperature')
        ax.set_ylabel('Frekuensi')
        st.pyplot(fig)
        plt.close()
    
    with col2:
        fig, ax = plt.subplots(figsize=(8, 5), facecolor='white')
        ax.hist(df_filtered['humidity'], bins=25, color='#4ECDC4', edgecolor='black', alpha=0.7)
        ax.set_title('Distribusi Humidity (%)', fontweight='bold')
        ax.set_xlabel('Humidity')
        ax.set_ylabel('Frekuensi')
        st.pyplot(fig)
        plt.close()
    
    col3, col4 = st.columns(2)
    
    with col3:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(df_filtered['MOI'], bins=25, color='#45B7D1', edgecolor='black', alpha=0.7)
        ax.set_title('Distribusi MOI', fontweight='bold')
        ax.set_xlabel('MOI')
        ax.set_ylabel('Frekuensi')
        st.pyplot(fig)
        plt.close()
    
    with col4:
        fig, ax = plt.subplots(figsize=(8, 5))
        result_counts = df_filtered['result'].value_counts().sort_index()
        ax.bar(result_counts.index.astype(str), result_counts.values, 
               color=['#96CEB4', '#FFEAA7', '#FF6B6B'], edgecolor='black')
        ax.set_title('Distribusi Result', fontweight='bold')
        ax.set_xlabel('Result')
        ax.set_ylabel('Jumlah')
        st.pyplot(fig)
        plt.close()

# Tab 2: Correlation Heatmap
with tab2:
    st.subheader("🔥 Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 8), facecolor='white')
    numeric_data = df_filtered[['MOI', 'temp', 'humidity', 'result']].corr()
    mask = np.triu(np.ones_like(numeric_data, dtype=bool))
    sns.heatmap(numeric_data, annot=True, fmt='.3f', cmap='coolwarm',
                mask=mask, center=0, square=True, linewidths=1,
                cbar_kws={"shrink": 0.8}, ax=ax,
                annot_kws={"size": 14})
    ax.set_title('Correlation Heatmap - Smart Farming Sensor', fontsize=14, fontweight='bold', pad=20)
    st.pyplot(fig)
    plt.close()
    
    st.markdown("**Interpretasi:**")
    st.info("""
    - Nilai mendekati **+1**: korelasi positif kuat
    - Nilai mendekati **-1**: korelasi negatif kuat  
    - Nilai mendekati **0**: tidak ada korelasi
    """)

# Tab 3: Per Crop Analysis
with tab3:
    st.subheader("📊 Analisis Per Crop")
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6), facecolor='white')
    
    sns.boxplot(data=df_filtered, x='crop ID', y='temp', ax=axes[0], palette='Set2')
    axes[0].set_title('Temperature per Crop', fontweight='bold')
    axes[0].tick_params(axis='x', rotation=45)
    
    sns.boxplot(data=df_filtered, x='crop ID', y='humidity', ax=axes[1], palette='Set2')
    axes[1].set_title('Humidity per Crop', fontweight='bold')
    axes[1].tick_params(axis='x', rotation=45)
    
    sns.boxplot(data=df_filtered, x='crop ID', y='MOI', ax=axes[2], palette='Set2')
    axes[2].set_title('MOI per Crop', fontweight='bold')
    axes[2].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    # Table: statistik per crop
    st.markdown("### 📋 Statistik per Crop")
    crop_stats = df_filtered.groupby('crop ID').agg({
        'temp': ['mean', 'min', 'max'],
        'humidity': ['mean', 'min', 'max'],
        'MOI': ['mean', 'min', 'max']
    }).round(2)
    crop_stats.columns = ['Temp Mean', 'Temp Min', 'Temp Max',
                          'Hum Mean', 'Hum Min', 'Hum Max',
                          'MOI Mean', 'MOI Min', 'MOI Max']
    st.dataframe(crop_stats, use_container_width=True)

# Tab 4: Time Series
with tab4:
    st.subheader("📉 Time Series Trend")
    
    n_points = st.slider("Jumlah data point:", 100, min(5000, len(df_filtered)), 500)
    subset = df_filtered.head(n_points)
    
    fig, axes = plt.subplots(3, 1, figsize=(16, 10), facecolor='white')
    
    window = max(5, n_points // 50)
    
    axes[0].plot(subset['timestamp'], subset['temp'].rolling(window).mean(), color='#FF6B6B', linewidth=1.5)
    axes[0].fill_between(subset['timestamp'], subset['temp'].rolling(window).mean(), alpha=0.2, color='#FF6B6B')
    axes[0].set_title('Temperature Trend', fontweight='bold')
    axes[0].set_ylabel('Temperature (°C)')
    
    axes[1].plot(subset['timestamp'], subset['humidity'].rolling(window).mean(), color='#4ECDC4', linewidth=1.5)
    axes[1].fill_between(subset['timestamp'], subset['humidity'].rolling(window).mean(), alpha=0.2, color='#4ECDC4')
    axes[1].set_title('Humidity Trend', fontweight='bold')
    axes[1].set_ylabel('Humidity (%)')
    
    axes[2].plot(subset['timestamp'], subset['MOI'].rolling(window).mean(), color='#45B7D1', linewidth=1.5)
    axes[2].fill_between(subset['timestamp'], subset['MOI'].rolling(window).mean(), alpha=0.2, color='#45B7D1')
    axes[2].set_title('MOI Trend', fontweight='bold')
    axes[2].set_ylabel('MOI')
    axes[2].set_xlabel('Timestamp')
    
    for ax in axes:
        ax.tick_params(axis='x', rotation=30)
    
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

# Tab 5: Data Quality
with tab5:
    st.subheader("⭐ Data Quality Score")
    
    total_cells = df.shape[0] * df.shape[1]
    total_rows = df.shape[0]
    
    # Accuracy
    missing_count = df.isnull().sum().sum()
    accuracy = 1 - (missing_count / total_cells)
    
    # Completeness
    non_null_count = df.notna().sum().sum()
    completeness = non_null_count / total_cells
    
    # Timeliness
    now = datetime.now()
    thirty_days_ago = now - timedelta(days=30)
    recent_data = df[df['timestamp'] >= thirty_days_ago].shape[0] if 'timestamp' in df.columns else total_rows
    timeliness = recent_data / total_rows
    
    overall = (accuracy + completeness + timeliness) / 3
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🎯 Accuracy", f"{accuracy*100:.1f}%")
        st.caption(f"1 - ({missing_count}/{total_cells})")
    with col2:
        st.metric("📋 Completeness", f"{completeness*100:.1f}%")
        st.caption(f"{non_null_count}/{total_cells}")
    with col3:
        st.metric("⏱️ Timeliness", f"{timeliness*100:.1f}%")
        st.caption(f"Data 30 hari terakhir")
    with col4:
        st.metric("⭐ Overall Score", f"{overall*100:.1f}%")
        st.caption("Rata-rata 3 metrik")
    
    # Bar chart
    fig, ax = plt.subplots(figsize=(8, 5), facecolor='white')
    scores = [accuracy * 100, completeness * 100, timeliness * 100, overall * 100]
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
    st.pyplot(fig)
    plt.close()
    
    st.markdown("---")
    st.markdown("### 📝 Penjelasan Metrik")
    st.markdown("""
    | Metrik | Rumus | Keterangan |
    |--------|-------|-----------|
    | **Accuracy** | 1 - (missing/total) | Seberapa akurat data (minim missing) |
    | **Completeness** | non-null/total | Seberapa lengkap data terisi |
    | **Timeliness** | % data 30 hari terakhir | Seberapa baru/terkini datanya |
    """)

# =============================================================================
# DATA TABLE
# =============================================================================
st.markdown("---")
st.subheader("📋 Data Table")
show_data = st.checkbox("Tampilkan raw data", value=False)
if show_data:
    st.dataframe(df_filtered.head(100), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 1rem;'>
    🌾 Smart Farming IoT Dashboard | Big Data & IoT | 2025
</div>
""", unsafe_allow_html=True)

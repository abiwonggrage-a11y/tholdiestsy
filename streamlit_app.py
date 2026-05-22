import streamlit as st

st.title("tholdiestsy")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# ==========================================
# PAGE CONFIG & CUSTOM THEME (SOFT COLORS)
# ==========================================
st.set_page_config(
    page_title="ChemiCalc - Titrasi & Analisis",
    page_icon="🧪",
    layout="wide"
)

# Custom CSS untuk mengubah warna tema menjadi soft/pastel
st.markdown("""
    <style>
    .main {
        background-color: #FAFAFA;
    }
    h1, h2, h3 {
        color: #2E4F4F;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stTabs [data-baseweb="tab"] {
        color: #4F709C;
        font-size: 16px;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #213555;
    }
    .stTabs [aria-selected="true"] {
        color: #0E8388 !important;
        border-bottom-color: #0E8388 !important;
    }
    div.stButton > button:first-child {
        background-color: #0E8388;
        color: white;
        border-radius: 8px;
        border: none;
    }
    div.stButton > button:first-child:hover {
        background-color: #2E4F4F;
        color: white;
    }
    .result-box {
        background-color: #EBF4F6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0E8388;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR / HEADER UNIVERSAL
# ==========================================
st.title("🧪 ChemiCalc: Perhitungan & Simulasi Titrasi")
st.write("Aplikasi bantu hitung otomatis dan simulasi visual untuk Lab Kimia Analisis.")
st.write("---")

# Membuat Menu dengan Tabs agar rapi
tab_utama, tab_fitur1, tab_fitur2, tab_fitur3, tab_fitur4, tab_fitur5 = st.tabs([
    "🏠 Halaman Utama", 
    "🧮 Kalkulator Titrasi", 
    "🎨 Simulasi Indikator", 
    "📈 Kurva Titrasi", 
    "📚 Database Reaksi",
    "📝 Penentuan Kadar"
])

# ==========================================
# TAB 1: HALAMAN UTAMA
# ==========================================
with tab_utama:
    st.header("Selamat Datang di ChemiCalc")
    st.write("""
    Titrasi adalah salah satu metode kimia analisis kuantitatif yang digunakan untuk menentukan konsentrasi suatu analit di dalam sampel. 
    Dengan aplikasi ini, mahasiswa dapat melakukan perhitungan cepat, melihat visualisasi perubahan warna indikator, 
    hingga memplot kurva titrasi secara otomatis.
    """)
    
    st.subheader("Jenis Titrasi yang Didukung:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Asam-Basa**\n\nBerdasarkan reaksi netralisasi antara ion $H^+$ dan $OH^-$.")
        st.info("**Argentometri**\n\nTitrasi pengendapan yang menggunakan agen mentitrasi halogen (biasanya $AgNO_3$).")
    with col2:
        st.info("**Permanganometri**\n\nTitrasi redoks menggunakan Kalium Permanganat ($KMnO_4$) sebagai oksidator kuat.")
        st.info("**Gravimetri Sederhana**\n\nAnalisis kuantitatif berdasarkan isolasi dan pengukuran berat suatu zat/endapan.")
    with col3:
        st.info("**Iodometri / Iodimetri**\n\nTitrasi redoks yang melibatkan iodium ($I_2$) baik sebagai titran maupun analit.")

# ==========================================
# TAB 2: FITUR 1 - KALKULATOR TITRASI
# ==========================================
with tab_fitur1:
    st.header("🧮 Kalkulator Titrasi (Rumus Dasar $N_1 \times V_1 = N_2 \times V_2$)")
    st.write("Gunakan fitur ini untuk mencari Normalitas/Konsentrasi larutan yang belum diketahui.")
    
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        st.subheader("Data Titran (Larutan Standar)")
        v1 = st.number_input("Volume Titran (V1) - mL", min_value=0.0, value=25.0, step=0.1, key="v1")
        n1 = st.number_input("Normalitas Titran (N1) - N", min_value=0.0, value=0.1000, format="%.4f", key="n1")
        
    with col_input2:
        st.subheader("Data Sampel / Analit")
        v2 = st.number_input("Volume Sampel (V2) - mL", min_value=0.1, value=25.0, step=0.1, key="v2")
        
    if st.button("Hitung Normalitas Sampel (N2)"):
        # Logika: N2 = (N1 * V1) / V2
        n2 = (n1 * v1) / v2
        st.markdown(f"""
        <div class="result-box">
            <h4>Hasil Perhitungan:</h4>
            <p>Konsentrasi/Normalitas Sampel (N2) = <b>{n2:.4f} N</b></p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 3: FITUR 2 - SIMULASI WARNA INDIKATOR
# ==========================================
with tab_fitur2:
    st.header("🎨 Simulasi Warna Indikator")
    st.write("Pilih indikator untuk melihat trayek pH dan perubahan warnanya.")
    
    indikator_data = {
        "Fenolftalein (PP)": {"trayek": "8.3 - 10.0", "asam": "Tidak Berwarna", "basa": "Merah Muda / Pink", "hex_asam": "#FFFFFF", "hex_basa": "#FFB7B2"},
        "Metil Merah (MR)": {"trayek": "4.4 - 6.2", "asam": "Merah", "basa": "Kuning", "hex_asam": "#FF6B6B", "hex_basa": "#FFE699"},
        "Metil Jingga (MO)": {"trayek": "3.1 - 4.4", "asam": "Merah / Jingga Tua", "basa": "Kuning", "hex_asam": "#FFAB76", "hex_basa": "#FFE699"}
    }
    
    pilihan_ind = st.selectbox("Pilih Indikator Kimia:", list(indikator_data.keys()))
    info_ind = indikator_data[pilihan_ind]
    
    st.write(f"**pH Kerja Indikator:** {info_ind['trayek']}")
    
    col_warna1, col_warna2 = st.columns(2)
    with col_warna1:
        st.markdown(f"""
        <div style="background-color: {info_ind['hex_asam']}; border: 1px solid #DDD; padding: 30px; text-align: center; border-radius: 10px;">
            <span style="color: black; font-weight: bold;">Kondisi Asam:<br>{info_ind['asam']}</span>
        </div>
        """, unsafe_allow_html=True)
        
    with col_warna2:
        st.markdown(f"""
        <div style="background-color: {info_ind['hex_basa']}; border: 1px solid #DDD; padding: 30px; text-align: center; border-radius: 10px;">
            <span style="color: black; font-weight: bold;">Kondisi Basa:<br>{info_ind['basa']}</span>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 4: FITUR 3 - GRAFIK KURVA TITRASI
# ==========================================
with tab_fitur3:
    st.header("📈 Grafik Kurva Titrasi")
    st.write("Input data mL titran dan pH yang diperoleh saat praktikum (pisahkan dengan koma atau gunakan data default).")
    
    col_input_kurva1, col_input_kurva2 = st.columns(2)
    with col_input_kurva1:
        input_vol = st.text_area("Masukkan Volume Titran (mL):", "0, 5, 10, 15, 20, 22, 24, 25, 26, 28, 30, 35, 40")
    with col_input_kurva2:
        input_ph = st.text_area("Masukkan Nilai pH:", "1.0, 1.18, 1.37, 1.60, 1.95, 2.20, 2.69, 7.00, 11.29, 11.75, 12.05, 12.30, 12.40")
        
    try:
        vol_data = [float(x.strip()) for x in input_vol.split(",")]
        ph_data = [float(x.strip()) for x in input_ph.split(",")]
        
        if len(vol_data) == len(ph_data):
            df_kurva = pd.DataFrame({"Volume": vol_data, "pH": ph_data})
            
            # Membuat grafik interaktif dengan Plotly (Warna Soft Teal)
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=df_kurva["Volume"], y=df_kurva["pH"],
                mode='lines+markers',
                line=dict(color='#0E8388', width=3),
                marker=dict(size=8, color='#2E4F4F'),
                name='Kurva Titrasi'
            ))
            
            fig.update_layout(
                title='Kurva Titrasi Asam-Basa Interaktif',
                xaxis_title='Volume Titran (mL)',
                yaxis_title='pH Larutan',
                plot_bgcolor='#F9F9F9',
                paper_bgcolor='#FAFAFA',
                margin=dict(l=40, r=40, t=40, b=40)
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("⚠️ Jumlah data Volume dan data pH harus sama!")
    except ValueError:
        st.error("⚠️ Pastikan format input berupa angka yang dipisahkan oleh koma.")

# ==========================================
# TAB 5: FITUR 4 - DATABASE REAKSI
# ==========================================
with tab_fitur4:
    st.header("📚 Database Reaksi Titrasi")
    st.write("Referensi cepat reaksi kimia dan perubahan warna larutan standar.")
    
    db_reaksi = {
        "KMnO4 (Permanganometri)": {
            "Fungsi": "Zat pengoksidasi kuat (Oksidator), bertindak sebagai auto-indikator.",
            "Reaksi": "MnO4⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O",
            "Perubahan Warna": "Ungu pekat berubah menjadi merah muda seulas (titik akhir)."
        },
        "AgNO3 (Argentometri - Mohr)": {
            "Fungsi": "Titran untuk menetapkan kadar Halida (Cl⁻, Br⁻) dengan indikator K₂CrO₄.",
            "Reaksi": "Ag⁺ + Cl⁻ → AgCl (Endapan Putih)\n2Ag⁺ + CrO₄²⁻ → Ag₂CrO₄ (Endapan Merah Bata)",
            "Perubahan Warna": "Terbentuk endapan merah bata yang konstan."
        },
        "Na2S2O3 (Iodometri)": {
            "Fungsi": "Zat pereduksi (Reduktor) untuk titrasi balik iodium dengan indikator amilum.",
            "Reaksi": "I₂ + 2S₂O₃²⁻ → 2I⁻ + S₄O₆²⁻",
            "Perubahan Warna": "Biru tua (kompleks amilum-Iod) berubah menjadi jernih/tidak berwarna."
        }
    }
    
    pilihan_db = st.selectbox("Pilih Larutan Standar / Metode:", list(db_reaksi.keys()))
    res_db = db_reaksi[pilihan_db]
    
    st.write(f"**💡 Fungsi Utama:** {res_db['Fungsi']}")
    st.code(res_db['Reaksi'], language="chemistry" if "chemistry" else "text")
    st.write(f"**🔄 Perubahan Warna Titik Akhir:** {res_db['Perubahan Warna']}")

# ==========================================
# TAB 6: FITUR 5 - SIMULASI PENENTUAN KADAR
# ==========================================
with tab_fitur5:
    st.header("📝 Simulasi Penentuan Kadar (Contoh: Asam Asetat)")
    st.write("Hitung kadar % (b/b) atau % (b/v) asam asetat dalam sampel cuka perdagangan.")
    
    col_kd1, col_kd2 = st.columns(2)
    with col_kd1:
        v_titran_kd = st.number_input("Volume NaOH (Titran) - mL", min_value=0.0, value=12.50, step=0.05)
        n_titran_kd = st.number_input("Normalitas NaOH - N", min_value=0.0, value=0.1005, format="%.4f")
    with col_kd2:
        massa_sampel = st.number_input("Massa / Volume Sampel Cuka - (gram atau mL)", min_value=0.01, value=2.0000, format="%.4f")
        be_asam = st.number_input("Berat Ekuivalen (BE) Asam Asetat", min_value=1.0, value=60.05, help="BM Asam Asetat = 60.05 g/mol, Valensi = 1")
        
    if st.button("Hitung % Kadar Asam Asetat"):
        # Rumus: % Kadar = (V_titran * N_titran * BE * 10^-3 / Massa Sampel) * 100%
        # Ditranslasikan jadi: (V * N * BE) / (Massa * 10)
        kadar = (v_titran_kd * n_titran_kd * be_asam) / (massa_sampel * 10)
        
        st.markdown(f""")
        <div class="result-box">
            <h4>Hasil Analisis Kadar:</h4>
            <p>Kadar Asam Asetat dalam Sampel = <b>{kadar:.2f} %</b></p>
        </div>
        """, unsafe_allow_html=True)

import streamlit as st

st.title("tholdiestsy")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# PAGE CONFIG & CUSTOM THEME (SOFT COLORS)
# ==========================================
st.set_page_config(
    page_title="ChemiCalc - Kalkulator Titrimetri",
    page_icon="🧪",
    layout="wide"
)

# Custom CSS untuk warna soft pastel (Mint/Teal lembut & abu-abu terang)
st.markdown("""
    <style>
    .main {
        background-color: #F8F9FA;
    }
    h1, h2, h3 {
        color: #2C4E4B;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stTabs [data-baseweb="tab"] {
        color: #5A737E;
        font-size: 16px;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        color: #439A86 !important;
        border-bottom-color: #439A86 !important;
    }
    div.stButton > button:first-child {
        background-color: #439A86;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 8px 20px;
    }
    div.stButton > button:first-child:hover {
        background-color: #2C4E4B;
        color: white;
    }
    .result-box {
        background-color: #EBF7F5;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #439A86;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER UTAMA
# ==========================================
st.title("🧪 ChemiCalc: Perhitungan Otomatis Titrimetri")
st.write("Aplikasi praktis penentu konsentrasi larutan kerja dan kadar sampel dalam satuan Gram.")
st.write("---")

# Menu Navigasi Utama (Tanpa Tab Warna Indikator)
tab_home, tab_kalkulator = st.tabs([
    "🏠 Halaman Utama", 
    "🧮 Kalkulator Hitung"
])

# ==========================================
# TAB 1: HALAMAN UTAMA
# ==========================================
with tab_home:
    st.header("Selamat Datang di ChemiCalc")
    st.write("""
    Aplikasi ini berfungsi sebagai alat bantu digital untuk memverifikasi data perhitungan hasil praktikum kimia analisis kuantitatif (Titrimetri). 
    Semua parameter perhitungan kadar sampel pada aplikasi ini telah dikonversi secara standar ke dalam satuan **Gram (g)** untuk memastikan kesesuaian pelaporan data analitik.
    """)
    
    st.subheader("Menu Perhitungan yang Tersedia:")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Asidimetri & Alkalimetri:** Standarisasi NaOH, Standarisasi HCl, dan Kadar Campuran Warder.")
        st.info("**Permanganometri:** Standarisasi KMnO₄ dan Kadar Besi (Fe).")
    with col2:
        st.info("**Iodometri:** Standarisasi Natrium Tiosulfat dan Kadar Klor Aktif (Cl₂).")
        st.info("**Kompleksiometri:** Standarisasi EDTA dan Kesadahan Jumlah air.")

# ==========================================
# TAB 2: FITUR UTAMA - KALKULATOR
# ==========================================
with tab_kalkulator:
    st.header("🧮 Kalkulator Parameter Titrasi")
    
    materi = st.selectbox("Pilih Metode Titrasi:", [
        "Asidimetri & Alkalimetri", 
        "Permanganometri", 
        "Iodometri", 
        "Kompleksiometri"
    ])
    
    st.write("---")
    
    # ------------------------------------------
    # 1. ASIDIMETRI & ALKALIMETRI
    # ------------------------------------------
    if materi == "Asidimetri & Alkalimetri":
        sub_asidi = st.selectbox("Pilih Analisis:", [
            "Standarisasi NaOH dengan Asam Oksalat",
            "Standarisasi HCl dengan Boraks",
            "Penetapan Kadar Campuran Warder (NaOH & Na2CO3)"
        ])
        
        if sub_asidi == "Standarisasi NaOH dengan Asam Oksalat":
            st.subheader("Hitung Normalitas NaOH")
            col_in1, col_in2 = st.columns(2)
            with col_in1:
                mg_baku = st.number_input("Bobot Asam Oksalat dihidrat (mg)", min_value=0.0, value=630.0)
                v_labu = st.number_input("Volume Labu Takar (mL)", min_value=1.0, value=100.0)
            with col_in2:
                v_pipet = st.number_input("Volume Pipet Aliquot (mL)", min_value=1.0, value=25.0)
                v_titran = st.number_input("Volume Titran NaOH (mL)", min_value=0.01, value=25.0)
                
            if st.button("Hitung"):
                # BE Asam Oksalat dihidrat = MR 126.07 / valensi 2 = 63.035
                be_oksalat = 126.07 / 2  
                fp = v_labu / v_pipet    
                
                # Rumus Standarisasi: N = mg / (V_titran * BE * fp)
                n_naoh = mg_baku / (v_titran * be_oksalat * fp)
                st.markdown(f'<div class="result-box"><h4>Hasil Standarisasi:</h4>Normalitas NaOH = <b>{n_naoh:.4f} N</b></div>', unsafe_allow_html=True)

        elif sub_asidi == "Standarisasi HCl dengan Boraks":
            st.subheader("Hitung Normalitas HCl")
            col_in1, col_in2 = st.columns(2)
            with col_in1:
                mg_baku = st.number_input("Bobot Boraks (mg)", min_value=0.0, value=1500.0)
                v_labu = st.number_input("Volume Labu Takar (mL)", min_value=1.0, value=100.0)
            with col_in2:
                v_pipet = st.number_input("Volume Pipet Aliquot (mL)", min_value=1.0, value=25.0)
                v_titran = st.number_input("Volume Titran HCl (mL)", min_value=0.01, value=25.0)
                
            if st.button("Hitung"):
                # BE Boraks = MR 381.37 / valensi 2 = 190.685
                be_boraks = 381.37 / 2
                fp = v_labu / v_pipet
                
                # Rumus Standarisasi: N = mg / (V_titran * BE * fp)
                n_hcl = mg_baku / (v_titran * be_boraks * fp)
                st.markdown(f'<div class="result-box"><h4>Hasil Standarisasi:</h4>Normalitas HCl = <b>{n_hcl:.4f} N</b></div>', unsafe_allow_html=True)

        elif sub_asidi == "Penetapan Kadar Campuran Warder (NaOH & Na2CO3)":
            st.subheader("Hitung Kadar Campuran Warder")
            col_in1, col_in2 = st.columns(2)
            with col_in1:
                v_sampel = st.number_input("Volume Sampel Liquid (mL)", min_value=1.0, value=25.0)
                n_hcl_std = st.number_input("Normalitas HCl Standar (N)", min_value=0.0, value=0.1000, format="%.4f")
            with col_in2:
                vol_a = st.number_input("Volume Titrasi I - Indikator PP (a mL)", min_value=0.0, value=15.0)
                vol_b = st.number_input("Volume Total Buret - Indikator SM (b mL)", min_value=0.0, value=25.0)
                
            if st.button("Hitung Kadar"):
                if vol_b < vol_a:
                    st.error("⚠️ Volume b tidak boleh lebih kecil dari volume a!")
                else:
                    be_na2co3 = 105.99 / 2
                    be_naoh = 40.00 / 1
                    
                    # Perhitungan volumetrik Warder:
                    # V HCl untuk Na2CO3 = 2 * (b - a)
                    # V HCl untuk NaOH = 2a - b
                    g_na2co3 = (2 * (vol_b - vol_a) * n_hcl_std * be_na2co3) / 1000
                    g_naoh = ((2 * vol_a - vol_b) * n_hcl_std * be_naoh) / 1000
                    
                    kadar_na2co3 = (g_na2co3 / v_sampel) * 100
                    kadar_naoh = (g_naoh / v_sampel) * 100
                    
                    st.markdown(f"""
                    <div class="result-box">
                        <h4>Hasil Analisis Eksperimen:</h4>
                        <ul>
                            <li>Massa Na₂CO₃ dalam sampel = <b>{g_na2co3:.4f} g</b></li>
                            <li>Kadar Na₂CO₃ = <b>{kadar_na2co3:.4f} % (b/v)</b></li>
                            <hr>
                            <li>Massa NaOH dalam sampel = <b>{g_naoh:.4f} g</b></li>
                            <li>Kadar NaOH = <b>{kadar_naoh:.4f} % (b/v)</b></li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)

    # ------------------------------------------
    # 2. PERMANGANOMETRI
    # ------------------------------------------
    elif materi == "Permanganometri":
        sub_permang = st.selectbox("Pilih Analisis:", [
            "Standarisasi KMnO4 dengan Asam Oksalat",
            "Penetapan Kadar Besi (Fe) dalam Garam Besi"
        ])
        
        if sub_permang == "Standarisasi KMnO4 dengan Asam Oksalat":
            st.subheader("Hitung Normalitas KMnO₄")
            col_in1, col_in2 = st.columns(2)
            with col_in1:
                mg_baku = st.number_input("Bobot Asam Oksalat (mg)", min_value=0.0, value=630.0)
                v_labu = st.number_input("Volume Labu Takar Oksalat (mL)", min_value=1.0, value=100.0)
            with col_in2:
                v_pipet = st.number_input("Volume Pipet Aliquot Oksalat (mL)", min_value=1.0, value=25.0)
                v_titran = st.number_input("Volume Titran KMnO₄ (mL)", min_value=0.01, value=25.0)
                
            if st.button("Hitung"):
                be_oksalat = 126.07 / 2
                fp = v_labu / v_pipet
                
                n_kmno4 = mg_baku / (v_titran * be_oksalat * fp)
                st.markdown(f'<div class="result-box"><h4>Hasil Standarisasi:</h4>Normalitas KMnO₄ = <b>{n_kmno4:.4f} N</b></div>', unsafe_allow_html=True)

        elif sub_permang == "Penetapan Kadar Besi (Fe) dalam Garam Besi":
            st.subheader("Hitung Kadar Besi (Fe)")
            col_in1, col_in2 = st.columns(2)
            with col_in1:
                v_sampel = st.number_input("Volume Sampel Larutan Besi (mL)", min_value=1.0, value=25.0)
                n_kmno4_std = st.number_input("Normalitas KMnO₄ Standar (N)", min_value=0.0, value=0.1000, format="%.4f")
            with col_in2:
                v_titran = st.number_input("Volume Titran KMnO₄ Terpakai (mL)", min_value=0.0, value=24.50)
                
            if st.button("Hitung Kadar"):
                # BE Besi (Fe) Redoks = AR 55.85 / 1 = 55.85
                be_fe = 55.85
                g_fe = (v_titran * n_kmno4_std * be_fe) / 1000
                kadar_fe = (g_fe / v_sampel) * 100
                
                st.markdown(f"""
                <div class="result-box">
                    <h4>Hasil Analisis Eksperimen:</h4>
                    Massa Fe dalam sampel = <b>{g_fe:.4f} g</b><br>
                    Kadar Besi (Fe) = <b>{kadar_fe:.4f} % (b/v)</b>
                </div>
                """, unsafe_allow_html=True)

    # ------------------------------------------
    # 3. IODOMETRI
    # ------------------------------------------
    elif materi == "Iodometri":
        sub_iodo = st.selectbox("Pilih Analisis:", [
            "Standarisasi Natrium Tiosulfat dengan K2Cr2O7",
            "Penetapan Kadar Klor Aktif (Cl2) dalam Pemutih"
        ])
        
        if sub_iodo == "Standarisasi Natrium Tiosulfat dengan K2Cr2O7":
            st.subheader("Hitung Normalitas Na₂S₂O₃")
            col_in1, col_in2 = st.columns(2)
            with col_in1:
                mg_baku = st.number_input("Bobot K₂Cr₂O₇ (mg)", min_value=0.0, value=245.0)
                v_labu = st.number_input("Volume Labu Takar Dikromat (mL)", min_value=1.0, value=100.0)
            with col_in2:
                v_pipet = st.number_input("Volume Pipet Aliquot Dikromat (mL)", min_value=1.0, value=25.0)
                v_titran = st.number_input("Volume Titran Tiosulfat (mL)", min_value=0.01, value=25.0)
                
            if st.button("Hitung"):
                # BE K2Cr2O7 = MR 294.19 / valensi 6 = 49.0317
                be_cr = 294.19 / 6
                fp = v_labu / v_pipet
                
                n_tio = mg_baku / (v_titran * be_cr * fp)
                st.markdown(f'<div class="result-box"><h4>Hasil Standarisasi:</h4>Normalitas Na₂S₂O₃ = <b>{n_tio:.4f} N</b></div>', unsafe_allow_html=True)

        elif sub_iodo == "Penetapan Kadar Klor Aktif (Cl2) dalam Pemutih":
            st.subheader("Hitung Kadar Klor Aktif (Cl₂)")
            col_in1, col_in2 = st.columns(2)
            with col_in1:
                v_sampel = st.number_input("Volume Sampel Pemutih Terpipet (mL)", min_value=0.1, value=5.0)
                n_id_fp = st.number_input("Faktor Pengenceran internal sampel (jika ada, kalau tidak isi 1)", min_value=1.0, value=1.0)
                n_tio_std = st.number_input("Normalitas Na₂S₂O₃ Standar (N)", min_value=0.0, value=0.1000, format="%.4f")
            with col_in2:
                v_titran = st.number_input("Volume Titran Tiosulfat Terpakai (mL)", min_value=0.0, value=15.20)
                
            if st.button("Hitung Kadar"):
                # BE Cl2 = MR 70.90 / 2 = 35.45
                be_cl2 = 70.90 / 2
                g_cl2 = (v_titran * n_tio_std * be_cl2 * n_id_fp) / 1000
                kadar_cl2 = (g_cl2 / v_sampel) * 100
                
                st.markdown(f"""
                <div class="result-box">
                    <h4>Hasil Analisis Eksperimen:</h4>
                    Massa Cl₂ Aktif = <b>{g_cl2:.4f} g</b><br>
                    Kadar Klor Aktif (Cl₂) = <b>{kadar_cl2:.4f} % (b/v)</b>
                </div>
                """, unsafe_allow_html=True)

    # ------------------------------------------
    # 4. KOMPLEKSIOMETRI
    # ------------------------------------------
    elif materi == "Kompleksiometri":
        sub_kompleks = st.selectbox("Pilih Analisis:", [
            "Standarisasi EDTA dengan CaCO3",
            "Penetapan Kesadahan Jumlah dalam Air"
        ])
        
        if sub_kompleks == "Standarisasi EDTA dengan CaCO3":
            st.subheader("Hitung Molaritas EDTA")
            col_in1, col_in2 = st.columns(2)
            with col_in1:
                mg_baku = st.number_input("Bobot CaCO₃ (mg)", min_value=0.0, value=100.0)
                v_labu = st.number_input("Volume Labu Takar Kalsium (mL)", min_value=1.0, value=100.0)
            with col_in2:
                v_pipet = st.number_input("Volume Pipet Aliquot Kalsium (mL)", min_value=1.0, value=25.0)
                v_titran = st.number_input("Volume Titran EDTA (mL)", min_value=0.01, value=25.0)
                
            if st.button("Hitung"):
                bm_caco3 = 100.09
                fp = v_labu / v_pipet
                
                # Molaritas EDTA = mg_baku / (V_titran * BM * fp)
                m_edta = mg_baku / (v_titran * bm_caco3 * fp)
                st.markdown(f'<div class="result-box"><h4>Hasil Standarisasi:</h4>Molaritas EDTA = <b>{m_edta:.4f} M</b></div>', unsafe_allow_html=True)

        elif sub_kompleks == "Penetapan Kesadahan Jumlah dalam Air":
            st.subheader("Hitung Kesadahan Jumlah (sebagai CaCO₃)")
            col_in1, col_in2 = st.columns(2)
            with col_in1:
                v_sampel = st.number_input("Volume Sampel Air (mL)", min_value=1.0, value=50.0)
                m_edta_std = st.number_input("Molaritas EDTA Standar (M)", min_value=0.0, value=0.0100, format="%.4f")
            with col_in2:
                v_titran = st.number_input("Volume Titran EDTA Terpakai (mL)", min_value=0.0, value=12.40)
                
            if st.button("Hitung Kesadahan"):
                bm_caco3 = 100.09
                g_caco3 = (v_titran * m_edta_std * bm_caco3) / 1000
                
                # ppm = mg/L -> (g / mL) * 1.000.000
                kesadahan = (g_caco3 / v_sampel) * 1000000
                
                st.markdown(f"""
                <div class="result-box">
                    <h4>Hasil Analisis Eksperimen:</h4>
                    Massa ekivalen CaCO₃ = <b>{g_caco3:.5f} g</b><br>
                    Kesadahan Jumlah = <b>{kesadahan:.2f} mg/L (ppm) CaCO₃</b>
                </div>
                """, unsafe_allow_html=True)

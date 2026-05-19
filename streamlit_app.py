import streamlit as st

st.title("tholdiestsy")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import numpy as np

# Pengaturan halaman
st.set_page_config(page_title="Smart Lab Calculator", page_icon="🧪", layout="wide")

# Sidebar untuk Navigasi Menu
st.sidebar.title("📌 Menu Analisis")
menu = st.sidebar.radio("Pilih Alat Hitung:", ["Preparasi Larutan", "Standardisasi Larutan (Titrasi)"])

# ==========================================
# MENU 1: PREPARASI LARUTAN
# ==========================================
if menu == "Preparasi Larutan":
    st.title("🧪 Kalkulator Preparasi & Pembuatan Larutan")
    st.write("Gunakan menu ini untuk menghitung kebutuhan bahan kimia sebelum praktikum dimulai.")
    st.markdown("---")
    
    sub_menu = st.selectbox("Jenis Bahan Awal:", ["Padatan (Garam/Kristal)", "Cairan Pekat (Pengenceran)"])
    
    if sub_menu == "Padatan (Garam/Kristal)":
        st.subheader("🔹 Pembuatan Larutan dari Padatan")
        
        col1, col2 = st.columns(2)
        with col1:
            bm = st.number_input("Massa Molar / BM (g/mol):", value=40.0, step=0.1, help="Contoh: NaOH = 40.0")
            konsentrasi = st.number_input("Konsentrasi yang diinginkan (Molaritas - M):", value=0.1, step=0.01, format="%.4f")
            volume = st.number_input("Volume larutan yang akan dibuat (mL):", value=100.0, step=10.0)
        
        # Rumus: Massa = M x V(L) x BM -> V dalam mL dibagi 1000
        massa = konsentrasi * (volume / 1000) * bm
        
        with col2:
            st.info("### 📋 Hasil Perhitungan Massa")
            st.metric(label="Massa Bahan yang Harus Ditimbang", value=f"{massa:.4f} gram")
            st.markdown(f"""
            **Langkah Kerja:**
            1. Timbang **{massa:.4f} gram** padatan di neraca analitik.
            2. Larutkan dengan sedikit akuades di dalam beaker glass.
            3. Masukkan ke dalam labu ukur **{volume:.0f} mL**, impitkan hingga tanda batas, lalu homogenkan.
            """)

    elif sub_menu == "Cairan Pekat (Pengenceran)":
        st.subheader("🔹 Pengenceran Cairan Pekat")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Sifat Cairan Induk (Pekat):**")
            m1 = st.number_input("Konsentrasi Cairan Induk (M1 atau N1):", value=12.0, step=0.1)
            
            st.markdown("**Target Larutan Baru:**")
            m2 = st.number_input("Konsentrasi yang Diinginkan (M2 atau N2):", value=0.1, step=0.01, format="%.4f")
            v2 = st.number_input("Volume Target yang Diinginkan (V2 dalam mL):", value=100.0, step=10.0)
        
        # Rumus: V1 = (M2 * V2) / M1
        if m1 > 0:
            v1 = (m2 * v2) / m1
        else:
            v1 = 0.0
            
        with col2:
            st.info("### 📋 Hasil Perhitungan Volumetrik")
            st.metric(label="Volume Cairan Pekat yang Harus Dipipet (V1)", value=f"{v1:.4f} mL")
            st.markdown(f"""
            **Langkah Kerja:**
            1. Ambil sebanyak **{v1:.4f} mL** cairan pekat menggunakan pipet ukur/volume.
            2. Masukkan secara perlahan ke dalam labu ukur **{v2:.0f} mL** yang sudah diisi sedikit akuades (terutama untuk asam pekat).
            3. Tambahkan akuades hingga tanda batas, lalu homogenkan.
            """)

# ==========================================
# MENU 2: STANDARDISASI LARUTAN (TITRASI)
# ==========================================
elif menu == "Standardisasi Larutan (Titrasi)":
    st.title("🎯 Kalkulator Standardisasi Larutan")
    st.write("Hitung konsentrasi pasti larutan titran kamu berdasarkan data titrasi replikasi.")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.subheader("📥 Data Primer Titrasi")
        metode = st.selectbox("Zat Standar Primer yang Digunakan:", ["Asam Oksalat (H2C2O4)", "Boraks", "KHP", "Kustom (Input Berat)"])
        
        # Penentuan berat ekivalen (BE) atau berat molekul otomatis
        if metode == "Asam Oksalat (H2C2O4)":
            be_standar = 63.03 # BE Asam oksalat dihidrat untuk normalitas
            st.caption("BE Asam Oksalat Dihidrat = 63.03")
        elif metode == "Boraks":
            be_standar = 190.6
            st.caption("BE Boraks = 190.6")
        elif metode == "KHP":
            be_standar = 204.22
            st.caption("BE KHP = 204.22")
        else:
            be_standar = st.number_input("Masukkan BE / BM Zat Standar:", value=100.0, step=0.1)
            
        massa_standar = st.number_input("Massa Zat Standar yang Ditimbang (mg):", value=100.0, step=1.0)
        
        st.markdown("**Volume Titran (mL) yang Habis Terpakai:**")
        # Menggunakan input jumlah replikasi
        jumlah_data = st.slider("Jumlah Ulangan Titrasi (Replikasi):", min_value=2, max_value=5, value=3)
        
        # Membuat form input dinamis berdasarkan jumlah replikasi
        volume_titrasi = []
        for i in range(jumlah_data):
            v = st.number_input(f"Volume Titrasi ke-{i+1} (mL):", value=10.0 + i*0.1, step=0.05, key=f"v_{i}")
            volume_titrasi.append(v)
            
    with col2:
        st.subheader("📊 Analisis Data & Hasil")
        
        # Perhitungan Statistik Dasar menggunakan NumPy
        vol_array = np.array(volume_titrasi)
        r_rata = np.mean(vol_array)
        std_dev = np.std(vol_array, ddof=1) # Sample standard deviation
        
        # Menghitung Konsentrasi untuk tiap ulangan dan dicari rata-ratanya
        # Rumus Normalitas Titran = mg Standar / (Vol Titran * BE Standar)
        konsentrasi_tiap_ulangan = massa_standar / (vol_array * be_standar)
        konsentrasi_rata = np.mean(konsentrasi_tiap_ulangan)
        sd_konsentrasi = np.std(konsentrasi_tiap_ulangan, ddof=1)
         RSD = (sd_konsentrasi / konsentrasi_rata) * 100 if konsentrasi_rata > 0 else 0
        
        # Tampilan kartu hasil
        st.success(f"### Konsentrasi Rata-Rata Titran: {konsentrasi_rata:.4f} N / M")
        
        # Menampilkan tabel data ringkas
        data_tabel = {
            "Uji Ke-": [f"Titrasi {i+1}" for i in range(jumlah_data)],
            "Volume Titran (mL)": volume_titrasi,
            "Konsentrasi (N/M)": [f"{k:.4f}" for k in konsentrasi_tiap_ulangan]
        }
        st.table(data_tabel)
        
        # Statistik Presisi Alat
        st.markdown("#### 📉 Evaluasi Presisi (K3L/Validasi Metode):")
        c_stat1, c_stat2, c_stat3 = st.columns(3)
        c_stat1.metric("Rata-rata Volume", f"{r_rata:.2f} mL")
        c_stat2.metric("SD Konsentrasi", f"{sd_konsentrasi:.5f}")
        c_stat3.metric("RSD (%)", f"{RSD:.2f} %")
        
        # Catatan evaluasi kelayakan data analitik
        if RSD < 1.0:
            st.balloons()
            st.success("✅ **Hasil Sangat Presisi!** Nilai RSD di bawah 1%, kerja lab kamu rapi banget!")
        elif RSD <= 2.0:
            st.warning("⚠️ **Hasil Cukup Baik.** Nilai RSD di antara 1% - 2%, masih masuk rentang normal untuk praktikum.")
        else:
            st.error("❌ **Kurang Presisi!** Nilai RSD > 2%. Cek lagi penentuan titik akhir titrasi atau ketelitian pemipetan kamu.")

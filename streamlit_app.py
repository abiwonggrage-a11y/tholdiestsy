import streamlit as st

st.title("tholdiestsy")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

# Konfigurasi Halaman Utama Web
st.set_page_config(page_title="TitraSmart - Kalkulator & Simulasi Titrasi", page_icon="🧪", layout="wide")

# ==========================================
# SIDEBAR - NAVIGASI UTAMA
# ==========================================
st.sidebar.title("🧪 TitraSmart")
st.sidebar.markdown("*Asisten Pintar Kimia Analisis*")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Pilih Menu:",
    ["Halaman Utama", "Kalkulator Titrasi", "Simulasi Indikator", "Database Reaksi", "Penentuan Kadar (%)"]
)

# ==========================================
# 1. HALAMAN UTAMA
# ==========================================
if menu == "Halaman Utama":
    st.title("Selamat Datang di TitraSmart! 👋")
    st.markdown("""
    **TitraSmart** adalah platform web interaktif yang dirancang khusus untuk mempermudah perhitungan data praktikum 
    dan visualisasi simulasi dalam dunia Kimia Analisis. Tidak perlu lagi menghitung rumus rumit secara manual, 
    cukup masukkan data praktikum Anda dan biarkan TitraSmart bekerja!
    """)
    
    st.subheader("📌 Jenis-Jenis Titrasi & Analisis yang Didukung:")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        * **Titrasi Asam-Basa**: Berdasarkan reaksi netralisasi antara ion $H^+$ dan $OH^-$.
        * **Permanganometri**: Titrasi redoks menggunakan $KMnO_4$ sebagai autondikator kuat.
        * **Iodimetri/Iodometri**: Titrasi redoks yang melibatkan iodium ($I_2$) dan indikator amilum.
        """)
    with col2:
        st.markdown("""
        * **Argentometri**: Titrasi pengendapan menggunakan ion perak ($Ag^+$), contohnya metode Mohr/Volhard.
        * **Gravimetri Sederhana**: Analisis kuantitatif berdasarkan pengukuran massa konstan endapan.
        """)
        
    st.info("💡 **Tips:** Gunakan menu di sebelah kiri (sidebar) untuk mulai menggunakan fitur kalkulator atau simulasi!")

# ==========================================
# 2. FITUR 1 - KALKULATOR TITRASI
# ==========================================
elif menu == "Kalkulator Titrasi":
    st.title("🧮 Kalkulator Konsentrasi Titrasi")
    st.write("Hitung normalitas atau molaritas sampel berdasarkan data volume titrasi.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Input Data Praktikum")
        v_titran = st.number_input("Volume Titran / Penitar (mL):", min_value=0.0, value=10.0, step=0.1)
        n_titran = st.number_input("Normalitas/Molaritas Titran (N atau M):", min_value=0.0, value=0.1000, format="%.4f", step=0.0001)
        v_sampel = st.number_input("Volume Sampel / Analit (mL):", min_value=0.1, value=10.0, step=0.1)
    
    # Rumus dasar titrasi: V1 x N1 = V2 x N2
    if v_sampel > 0:
        hasil_konsentrasi = (v_titran * n_titran) / v_sampel
    else:
        hasil_konsentrasi = 0.0

    with col2:
        st.subheader("Hasil Perhitungan")
        st.metric(label="Konsentrasi Sampel Hasil Titrasi", value=f"{hasil_konsentrasi:.4f} N / M")
        
        st.markdown("**Catatan Rumus:**")
        st.latex(r"N_{sampel} = \frac{V_{titran} \times N_{titran}}{V_{sampel}}")

# ==========================================
# 3. FITUR 2 - SIMULASI WARNA INDIKATOR
# ==========================================
elif menu == "Simulasi Indikator":
    st.title("🎨 Simulasi Warna Indikator")
    st.write("Lihat perubahan warna estetis indikator kimia berdasarkan trayek pH-nya.")
    
    indikator = st.selectbox(
        "Pilih Indikator Asam-Basa:",
        ["Fenolftalein (PP)", "Metil Merah (MM)", "Metil Jingga (MO)"]
    )
    
    # Logika warna dan pH kerja
    if indikator == "Fenolftalein (PP)":
        pH_range = "8.3 - 10.0"
        sifat_asam = "Bening (Tidak Berwarna)"
        sifat_basa = "Merah Muda / Pink Tua"
        hex_asam = "#FFFFFF" # Putih/Bening
        hex_basa = "#FF69B4" # Hot Pink
    elif indikator == "Metil Merah (MM)":
        pH_range = "4.4 - 6.2"
        sifat_asam = "Merah"
        sifat_basa = "Kuning"
        hex_asam = "#FF0000"
        hex_basa = "#FFFF00"
    else: # Metil Jingga (MO)
        pH_range = "3.1 - 4.4"
        sifat_asam = "Merah"
        sifat_basa = "Kuning-Jingga"
        hex_asam = "#FF0000"
        hex_basa = "#FFA500"

    st.subheader(f"Informasi Indikator: {indikator}")
    st.markdown(f"**Trayek pH Kerja:** {pH_range}")
    
    # Representasi Visual Perubahan Warna
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"🟢 **Kondisi Asam (< {pH_range.split(' - ')[0]}):** {sifat_asam}")
        # Bikin kotak warna pakai HTML/CSS markdown
        st.markdown(f'<div style="background-color:{hex_asam}; width:100px; height:100px; border:2px solid #ccc; border-radius:10px;"></div>', unsafe_allow_html=True)
        
    with c2:
        st.markdown(f"🔴 **Kondisi Basa (> {pH_range.split(' - ')[1]}):** {sifat_basa}")
        st.markdown(f'<div style="background-color:{hex_basa}; width:100px; height:100px; border:2px solid #ccc; border-radius:10px;"></div>', unsafe_allow_html=True)

# ==========================================
# 4. FITUR 4 - DATABASE REAKSI
# ==========================================
elif menu == "Database Reaksi":
    st.title("📚 Database Reaksi & Reagen")
    st.write("Cari informasi lengkap mengenai senyawa/reagen utama yang sering digunakan dalam titrasi.")
    
    reagen = st.selectbox(
        "Pilih Reagen Kimia:",
        ["KMnO4 (Kalium Permanganat)", "AgNO3 (Perak Nitrat)", "Na2S2O3 (Natrium Tiosulfat)"]
    )
    
    # Kamus data reagen
    db_reaksi = {
        "KMnO4 (Kalium Permanganat)": {
            "fungsi": "Sebagai titran/oksidator kuat pada titrasi Permanganometri. Bersifat autondikator (bisa jadi indikator bagi dirinya sendiri).",
            "reaksi": r"MnO_4^- + 8H^+ + 5e^- \rightarrow Mn^{2+} + 4H_2O",
            "perubahan": "Ungu tua (awal titrasi) menjadi Merah Muda Seulas / konstan (titik akhir)."
        },
        "AgNO3 (Perak Nitrat)": {
            "fungsi": "Sebagai titran utama pada titrasi Argentometri (pengendapan) untuk menetapkan kadar halida seperti klorida ($Cl^-$).",
            "reaksi": r"Ag^+ + Cl^- \rightarrow AgCl \downarrow \text{ (Endapan Putih)}",
            "perubahan": "Terbentuk endapan putih kusam, dan menjadi merah bata saat berikatan dengan indikator kromat ($K_2CrO_4$)."
        },
        "Na2S2O3 (Natrium Tiosulfat)": {
            "fungsi": "Sebagai larutan standar/reduktor pada titrasi Iodometri (titrasi tidak langsung) untuk menitar Iod yang terbebas.",
            "reaksi": r"I_2 + 2S_2O_3^{2-} \rightarrow 2I^- + S_4O_6^{2-}",
            "perubahan": "Biru tua (saat ditambah indikator amilum) menjadi Bening/Tepat Hilang Warna Birunya."
        }
    }
    
    info = db_reaksi[reagen]
    
    st.subheader(f"🔍 Detail Reagen: {reagen}")
    st.markdown(f"**💡 Fungsi Utama:**\n{info['fungsi']}")
    st.markdown("**🧪 Persamaan Reaksi:**")
    st.latex(info['reaksi'])
    st.markdown(f"**🔄 Perubahan Warna Titik Akhir:**\n{info['perubahan']}")

# ==========================================
# 5. FITUR 5 - SIMULASI PENENTUAN KADAR (%)
# ==========================================
elif menu == "Penentuan Kadar (%)":
    st.title("📊 Simulasi Penentuan Kadar Sampel")
    st.write("Hitung persentase kadar (%) zat analit di dalam sampel padat atau cair.")
    
    # Contoh studi kasus Asam Asetat (Cuka)
    st.info("ℹ️ **Studi Kasus Default:** Penentuan Kadar Asam Asetat ($CH_3COOH$) dalam Cuka Perdagangan menggunakan standar NaOH. (BE Asam Asetat = 60.05)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Masukkan Parameter")
        v_titran_kadar = st.number_input("Volume Titran Terpakai (mL):", min_value=0.0, value=15.2, step=0.1, key="v_kadar")
        n_titran_kadar = st.number_input("Normalitas Titran (N):", min_value=0.0, value=0.1012, format="%.4f", step=0.0001, key="n_kadar")
        be_zat = st.number_input("Berat Ekuivalen (BE) / Mr Zat Analit:", min_value=0.1, value=60.05, step=0.01, help="Untuk Asam Asetat = 60.05")
        massa_sampel = st.number_input("Massa / Volume Sampel (mg atau mL):", min_value=0.1, value=2000.0, step=10.0, help="Jika sampel diencerkan atau ditimbang dalam mg. Contoh: 2000 mg = 2 gram")
        
    # Rumus Kadar % = (V x N x BE) / Massa Sampel (mg) * 100%
    if massa_sampel > 0:
        kadar = ((v_titran_kadar * n_titran_kadar * be_zat) / massa_sampel) * 100
    else:
        kadar = 0.0

    with col2:
        st.subheader("Hasil Analisis Kadar")
        st.metric(label="Persentase Kadar Zat (%)", value=f"{kadar:.3f} %")
        
        st.markdown("**Rumus yang Digunakan:**")
        st.latex(r"\%\text{ Kadar} = \frac{V_{titran} \times N_{titran} \times BE}{Massa\ Sampel\ (mg)} \times 100\%")
        
        if kadar > 0:
            st.success(f"Analisis Selesai! Kadar komponen di dalam sampel terdeteksi sebesar **{kadar:.3f}%**.")

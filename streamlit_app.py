import streamlit as st

st.title("tholdiestsy")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
import streamlit as nn
import streamlit as st

st.set_page_config(page_title="Kalkulator Sederhana", page_icon="🧮")

st.title("🧮 Kalkulator Sederhana")
st.write("Mulai berhitung dengan memasukkan angka dan memilih operasi di bawah ini.")

col1, col2 = st.columns(2)

with col1:
    angka1 = st.number_input("Masukkan Angka Pertama", value=0.0, step=1.0)

with col2:
    angka2 = st.number_input("Masukkan Angka Kedua", value=0.0, step=1.0)

operasi = st.selectbox(
    "Pilih Operasi",
    ("Penjumlahan (+)", "Pengurangan (-)", "Perkalian (x)", "Pembagian (/)")
)

if st.button("Hitung Hasil"):
    hasil = 0
    error_message = None

    if operasi == "Penjumlahan (+)":
        hasil = angka1 + angka2
    elif operasi == "Pengurangan (-)":
        hasil = angka1 - angka2
    elif operasi == "Perkalian (x)":
        hasil = angka1 * angka2
    elif operasi == "Pembagian (/)":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            error_message = "Aduh, tidak bisa membagi angka dengan nol (0) ya!"

    st.markdown("---")
    if error_message:
        st.error(error_message)
    else:
        st.success(f"### Hasil: {hasil}")

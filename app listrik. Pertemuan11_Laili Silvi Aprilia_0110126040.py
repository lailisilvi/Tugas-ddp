
import streamlit as st

st.set_page_config(
    page_title="Kalkulator Tagihan Listrik",
    page_icon="⚡",
    layout="centered"
)

# CSS
st.markdown("""
<style>
.stApp {
    background-color: #f0f5ff;
}
h1 {
    color: #174ea6;
    text-align: center;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #2563eb;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# Judul
st.title("⚡ Kalkulator Tagihan Listrik")
st.write("Hitung estimasi tagihan listrik bulananmu dengan mudah!")

st.divider()

# Input pengguna
st.subheader("📝 Masukkan Data Pemakaian")

nama = st.text_input("Nama pelanggan")

daya = st.selectbox(
    "Pilih daya listrik",
    [450, 900, 1300, 2200, 3500, 5500]
)

pemakaian = st.number_input(
    "Pemakaian listrik (kWh)",
    min_value=0.0,
    step=1.0
)

biaya_admin = st.number_input(
    "Biaya administrasi (Rp)",
    min_value=0,
    value=3000,
    step=500
)

# Tarif estimasi per kWh
tarif = {
    450: 415,
    900: 1352,
    1300: 1444.70,
    2200: 1444.70,
    3500: 1699.53,
    5500: 1699.53
}

# Tombol hitung
if st.button("⚡ Hitung Tagihan", use_container_width=True):

    if nama.strip() == "":
        st.warning("Silakan masukkan nama pelanggan.")

    elif pemakaian <= 0:
        st.warning("Pemakaian listrik harus lebih dari 0 kWh.")

    else:
        harga = tarif[daya]
        biaya_listrik = pemakaian * harga
        total = biaya_listrik + biaya_admin

        st.success("Perhitungan berhasil!")

        st.subheader("📄 Rincian Tagihan")

        st.markdown(f"""
        <div class="card">
        <h3>⚡ Tagihan Listrik</h3>
        <b>Nama Pelanggan:</b> {nama}<br>
        <b>Daya Listrik:</b> {daya} VA<br>
        <b>Pemakaian:</b> {pemakaian} kWh
        </div>
        """, unsafe_allow_html=True)

        st.write("**Rincian Biaya:**")

        st.write(f"Tarif per kWh: Rp {harga:,.2f}")
        st.write(f"Biaya pemakaian: Rp {biaya_listrik:,.2f}")
        st.write(f"Biaya administrasi: Rp {biaya_admin:,.0f}")

        st.divider()

        st.metric(
            "TOTAL ESTIMASI TAGIHAN",
            f"Rp {total:,.2f}"
        )

        st.caption(
            "Catatan: Hasil merupakan estimasi sederhana, "
            "bukan tagihan resmi PLN. Tarif disederhanakan "
            "dan belum memperhitungkan seluruh komponen "
            "seperti pajak, PPJ, atau ketentuan tarif khusus."
        )

st.divider()

st.caption("⚡ Kalkulator Listrik | Dibuat dengan Python & Streamlit")

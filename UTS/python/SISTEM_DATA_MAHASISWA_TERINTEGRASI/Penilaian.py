import streamlit as st
import pandas as pd
import os

# --- Inisialisasi session state untuk data mahasiswa ---
if "data_mahasiswa" not in st.session_state:
    st.session_state.data_mahasiswa = []

st.title("🎓 SISTEM DATA MAHASISWA TERINTEGRASI ©") 

# --- Fungsi menghitung nilai akhir dan huruf mutu ---
def hitung_nilai(tugas, uts, uas):
    akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    if akhir >= 85:
        grade = "A"
    elif akhir >= 70:
        grade = "B"
    elif akhir >= 55:
        grade = "C"
    elif akhir >= 40:
        grade = "D"
    else:
        grade = "E"
    return akhir, grade


# --- Input Data Mahasiswa ---
st.subheader("🧾 Input Data Mahasiswa")

nama = st.text_input("Nama Mahasiswa")
nim = st.text_input("NIM")
tugas = st.number_input("Nilai Tugas (30%)", 0.0, 100.0, step=1.0)
uts = st.number_input("Nilai UTS (30%)", 0.0, 100.0, step=1.0)
uas = st.number_input("Nilai UAS (40%)", 0.0, 100.0, step=1.0)

if st.button("➕ Tambah Data"):
    if not nama or not nim:
        st.error("⚠️ Nama dan NIM wajib diisi!")
    else:
        akhir, grade = hitung_nilai(tugas, uts, uas)
        st.session_state.data_mahasiswa.append({
            "Nama": nama,
            "NIM": nim,
            "Tugas": tugas,
            "UTS": uts,
            "UAS": uas,
            "Nilai Akhir": akhir,
            "Grade": grade
        })
        st.success(f"✅ Data mahasiswa '{nama}' berhasil ditambahkan!")


# --- Tampilkan Data ---
st.subheader("📋 Tabel Data Mahasiswa")

if st.session_state.data_mahasiswa:
    df = pd.DataFrame(st.session_state.data_mahasiswa)
    st.dataframe(df)

    # --- Simpan ke file CSV ---
    if st.button("💾 Simpan ke data_mahasiswa.csv"):
        df.to_csv("data_mahasiswa.csv", index=False)
        st.success("Data berhasil disimpan ke file 'data_mahasiswa.csv'.")

else:
    st.info("Belum ada data mahasiswa yang dimasukkan.")


# --- Fitur Cari Mahasiswa ---
st.subheader("🔍 Cari Mahasiswa Berdasarkan NIM")

nim_cari = st.text_input("Masukkan NIM untuk mencari:")
if st.button("Cari Mahasiswa"):
    hasil = [m for m in st.session_state.data_mahasiswa if m["NIM"] == nim_cari]
    if hasil:
        st.success("Data Mahasiswa Ditemukan:")
        st.table(pd.DataFrame(hasil))
    else:
        st.error("❌ Mahasiswa dengan NIM tersebut tidak ditemukan.")


# --- Fitur Hapus Mahasiswa ---
st.subheader("🗑️ Hapus Mahasiswa Berdasarkan NIM")

nim_hapus = st.text_input("Masukkan NIM untuk menghapus:")
if st.button("Hapus Mahasiswa"):
    awal = len(st.session_state.data_mahasiswa)
    st.session_state.data_mahasiswa = [
        m for m in st.session_state.data_mahasiswa if m["NIM"] != nim_hapus
    ]
    if len(st.session_state.data_mahasiswa) < awal:
        st.success(f"🗑️ Data mahasiswa dengan NIM {nim_hapus} berhasil dihapus.")
    else:
        st.error("❌ Data mahasiswa tidak ditemukan.")


# --- Tampilkan tombol reset seluruh data ---
if st.button("♻️ Reset Semua Data"):
    st.session_state.data_mahasiswa = []
    if os.path.exists("data_mahasiswa.csv"):
        os.remove("data_mahasiswa.csv")
    st.warning("⚠️ Semua data telah dihapus dari memori dan file CSV.")

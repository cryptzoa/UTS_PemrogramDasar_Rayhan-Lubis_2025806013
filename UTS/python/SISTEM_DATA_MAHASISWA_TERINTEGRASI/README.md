# 🧠 UTS Pemrograman Dasar (C & Python)

## 👤 Identitas
- Nama: Rayhan Soeangkupon Lubis
- NIM: 2025806013
- Kelas: Teknologi Informasi 2
- Dosen: Rintis Mardika Sunarto
- Repository: [\[link GitHub repo\]](https://github.com/cryptzoa/UTS_PemrogramDasar_Rayhan-Lubis_2025806013.git)

---

## 📚 Deskripsi
Proyek ini adalah Ujian Tengah Semester (UTS) Pemrograman Dasar, yang menggabungkan konsep C dan Python.  
Mahasiswa diminta membuat beberapa proyek terpisah dengan fitur logika, struktur data, file handling, dan modular programming.

---
# 🎓 SISTEM DATA MAHASISWA TERINTEGRASI

Program ini merupakan aplikasi berbasis Python yang digunakan untuk mengelola data mahasiswa secara terintegrasi.  
Konsep utama yang digunakan meliputi **struct (melalui class Python), pointer (melalui referensi objek), dynamic memory (linked list), dan file I/O**.

---

## 🧩 Fitur Program

1. **Input Data Mahasiswa**
   - Pengguna dapat menambahkan beberapa data mahasiswa yang terdiri dari:
     - Nama
     - NIM
     - Nilai Tugas
     - Nilai UTS
     - Nilai UAS

2. **Perhitungan Otomatis**
   - Program secara otomatis menghitung:
     - **Nilai Akhir** menggunakan rumus:
       ```
       Nilai Akhir = (0.3 × Tugas) + (0.3 × UTS) + (0.4 × UAS)
       ```
     - **Huruf Mutu (A–E)** berdasarkan rentang nilai akhir.

3. **Tampilan Data dalam Bentuk Tabel**
   - Data mahasiswa ditampilkan dalam format tabel rapi di layar agar mudah dibaca.

4. **Penyimpanan ke File**
   - Seluruh data yang telah diinput disimpan otomatis ke file:
     ```
     data_mahasiswa.csv
     ```
     sehingga data tidak hilang saat program ditutup.

5. **Pencarian Data**
   - Pengguna dapat mencari data mahasiswa berdasarkan **NIM** untuk melihat detail nilai.

6. **Hapus Data**
   - Program menyediakan fitur untuk menghapus data mahasiswa berdasarkan NIM.

7. **Antarmuka Interaktif (Streamlit)**
   - Program dilengkapi tampilan interaktif berbasis web menggunakan **Streamlit**, memudahkan pengguna dalam memasukkan dan mengelola data tanpa mengetik di terminal.

---

## ⚙️ Cara Menjalankan Program

### 1. Persiapkan Lingkungan
Pastikan Python dan Streamlit sudah terinstal:
```bash
pip install streamlit pandas
```
### 2. Jalankan Program
Masuk ke folder tempat file Penilaian.py berada, lalu jalankan perintah:
```bash
python -m streamlit run Penilaian.py
```
atau (jika di CMD/PowerShell)
```bash
streamlit run Penilaian.py
```

## 🧠 Konsep yang Diterapkan

   -Struct → Diwakili oleh class Mahasiswa

   -Pointer → Diimplementasikan melalui referensi antar node linked list

   -Dynamic Memory → Penambahan data dilakukan secara dinamis

   -File I/O → Menyimpan dan membaca data dari file CSV
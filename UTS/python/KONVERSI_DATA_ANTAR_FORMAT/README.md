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

# 🔄 Konversi Data Antar Format (C & Python Kombinasi)

## 🧠 Konsep Utama
Proyek ini menunjukkan **integrasi lintas bahasa (C dan Python)** untuk memproses dan mengonversi data akademik mahasiswa antar format file — dari **CSV** ke **JSON**.  
Fokus utama adalah pemahaman konsep:
- File I/O (input/output)
- Manipulasi string
- Konversi format data
- Integrasi lintas bahasa (C → Python)

---

## 📋 Deskripsi Proyek

### Langkah 1. — Program C
Program **C** digunakan untuk **menghasilkan file `data_mahasiswa.csv`** berisi data mahasiswa.

Struktur data yang disimpan:
```
nama,nim,nilai_akhir,mutu
Rina,2310001,85.5,A
Doni,2310002,61.5,C
Sinta,2310003,72.0,B
```

### Langkah 2. — Program Python
Program **Python** digunakan untuk:
1. **Membaca file CSV** hasil dari program C  
2. **Menampilkan data dengan rapi di terminal**
3. **Menghitung rata-rata nilai akhir semua mahasiswa**
4. **Mengonversi hasil ke format JSON (`data_mahasiswa.json`)**

---

## 🗂️ Struktur Folder Proyek
```
konversi_data/
├── c_program/
│ └── generate_csv.c # Program C untuk membuat data_mahasiswa.csv
├── python_program/
│ ├── main.py # File utama Python
│ ├── converter.py # Modul untuk baca CSV dan konversi ke JSON
│ ├── utils.py # Modul bantu (formatting, average, dsb)
│ ├── data_mahasiswa.csv # File CSV hasil program C
│ └── data_mahasiswa.json # File JSON hasil konversi Python
└── README.md # Dokumentasi proyek
```

---

## ⚙️ Cara Menjalankan Program

###  1. Jalankan Program C

Masuk ke folder `c` lalu jalankan:
```bash
gcc generate_csv.c -o generate_csv
./generate_csv
```
Setelah dijalankan, akan muncul file data_mahasiswa.csv seperti ini:
```
Rina,2310001,85.5,A
Doni,2310002,61.5,C
Sinta,2310003,72.0,B
```

### 2. Jalankan Program Python

Masuk ke folder `python` lalu jalankan:
```bash
python main.py
```
Output di terminal akan menampilkan:
```
=== DATA MAHASISWA ===
Nama    : Rina
NIM     : 2310001
Nilai   : 85.5
Mutu    : A
------------------------
Nama    : Doni
NIM     : 2310002
Nilai   : 61.5
Mutu    : C
------------------------
Nama    : Sinta
NIM     : 2310003
Nilai   : 72.0
Mutu    : B

Rata-rata nilai akhir: 73.0
Data berhasil disimpan ke data_mahasiswa.json
```
---
## 📁 Hasil Akhir File JSON
```json
[
  {"nama": "Rina", "nim": "2310001", "nilai_akhir": 85.5, "mutu": "A"},
  {"nama": "Doni", "nim": "2310002", "nilai_akhir": 61.5, "mutu": "C"},
  {"nama": "Sinta", "nim": "2310003", "nilai_akhir": 72.0, "mutu": "B"}
]
```
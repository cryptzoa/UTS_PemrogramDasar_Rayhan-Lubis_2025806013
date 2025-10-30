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

# 🧠 Analisis Teks Otomatis (Python Advanced)

Program ini merupakan proyek **analisis teks otomatis** yang dibuat menggunakan **Python** dengan konsep:  
➡️ *File I/O, String Manipulation, Dictionary, Modular Programming, dan Grafik ASCII.*

Program membaca file teks (`input.txt`), menganalisis isinya, lalu menghasilkan laporan statistik secara otomatis dalam file `report.txt`.  
Selain itu, program juga menampilkan **grafik frekuensi kata** di terminal dalam bentuk **grafik ASCII**.

---

## 🧩 Fitur Utama

1. **Input & Output Otomatis**
   - Input dibaca dari file `input.txt`.
   - Output hasil analisis ditulis ke file `report.txt`.

2. **Analisis Statistik Lengkap**
   - Jumlah **baris**
   - Jumlah **kata**
   - **5 kata yang paling sering muncul**
   - Jumlah **huruf vokal** dan **huruf konsonan**

3. **Visualisasi Frekuensi Kata (Grafik ASCII)**
```
python #########
program ######
belajar ###
```

4. **Modularisasi**
- Program dibagi menjadi beberapa file:
  - `main.py` → file utama
  - `analyzer.py` → modul utama untuk logika analisis
  - `utils.py` → modul pendukung untuk perhitungan dan grafik ASCII

5. **Error Handling**
- Menangani kondisi jika file input tidak ditemukan.

---

## ⚙️ Cara Menjalankan Program

### 1. Siapkan File Input
Buat file bernama **`input.txt`** di folder proyek, lalu isi dengan teks yang ingin dianalisis.  

### 2. Jalankan Program
Gunakan perintah berikut di terminal:
```bash
python main.py
```
### 3. Hasil yang akan tampil di terminal :
```
=== ANALISIS TEKS OTOMATIS ===
Membaca data dari 'input.txt'...

=== HASIL ANALISIS ===
Jumlah baris       : 3
Jumlah kata        : 15
Jumlah huruf vokal : 45
Jumlah konsonan    : 72

Top 5 Kata Terbanyak:
  python: 3
  belajar: 1
  data: 1
  populer: 1
  mesin: 1

📊 Grafik Frekuensi Kata:
python     ###
belajar    #
data       #
populer    #
mesin      #

📁 Hasil lengkap disimpan ke 'report.txt'
```

## Contoh isi file report.txt
```
=== LAPORAN ANALISIS TEKS ===
Jumlah baris: 3
Jumlah kata: 15
Jumlah huruf vokal: 45
Jumlah huruf konsonan: 72

5 Kata Paling Sering Muncul:
python: 3
belajar: 1
data: 1
populer: 1
mesin: 1
```
---

## 💡 Penjelasan Modul
**🔹 utils.py**

Berisi fungsi-fungsi bantu seperti:

   - count_vowels_and_consonants() → Menghitung huruf vokal & konsonan

   - get_word_frequency() → Menghitung frekuensi setiap kata

   - ascii_bar_chart() → Menampilkan grafik frekuensi dalam bentuk ASCII

**🔹 analyzer.py**

Modul utama yang:

   - Membaca isi file input.txt

   - Menggunakan fungsi dari utils.py untuk analisis

   - Menulis hasil ke report.txt

   - Menampilkan hasil dan grafik di terminal

**🔹 main.py**

   - Hanya berisi satu tugas: memanggil fungsi utama analyze_text() dari analyzer.py

## 🧹 Reset / Edit Hasil Analisis

   - Untuk menghapus hasil lama, cukup hapus atau kosongkan file report.txt.

   - Untuk menganalisis teks baru, cukup ganti isi input.txt lalu jalankan ulang:
   ```bash
   python main.py
   ```
---

## 👨‍💻 Konsep yang Digunakan
   - Konsep	Penjelasan
   - File I/O	Membaca dan menulis file teks
   - String Processing	Memecah teks menjadi kata dan huruf
   - Dictionary	Menyimpan dan menghitung frekuensi kata
   - Modularization	Pemisahan kode ke beberapa file untuk kerapian
   - ASCII Chart	Menampilkan grafik kata tanpa library eksternal
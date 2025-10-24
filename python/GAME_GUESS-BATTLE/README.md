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
# 🎮 Guess Battle

Guess Battle adalah game tebak angka berbasis terminal yang dikembangkan dengan Python.
Game ini menggunakan konsep **loop, conditional, modularisasi, file handling, JSON, dan pewarnaan terminal (colorama)**.

# 🧩 Fitur Utama

1. **Multi-player system**
    Pemain dapat login menggunakan nama mereka. Skor tiap pemain akan tersimpan otomatis di file scores.json.

2. **Multi-level gameplay**
    Terdapat 3 level kesulitan:

        - Level 1: Tebak angka 1–10 (3 percobaan)

        - Level 2: Tebak angka 1–50 (5 percobaan)

        - Level 3: Tebak angka 1–100 (7 percobaan)

3. **Perhitungan skor dinamis**
    Skor dihitung berdasarkan jumlah percobaan yang tersisa. Semakin cepat menebak, semakin tinggi nilainya.

4. **Penyimpanan data skor otomatis**
    Semua hasil permainan disimpan di scores.json menggunakan format JSON agar mudah diakses dan diperbarui.

5. **Top 5 pemain terbaik**
    Setelah semua level selesai, sistem akan menampilkan 5 pemain dengan skor tertinggi sepanjang permainan.

6. **Tampilan berwarna dan menarik**
    Game memanfaatkan library colorama untuk memberi efek warna di terminal, seperti hijau untuk keberhasilan, merah untuk kegagalan, dan biru untuk informasi.

7. **Penanganan error input**
    Sistem menggunakan try-except agar tidak crash jika pemain memasukkan input yang tidak valid.

---

## ⚙️ Cara Menjalankan Game

### 1. Persiapan

Pastikan Python sudah terinstal di komputer kamu.
Cek dengan perintah:
```bash
python --version
```
### 2. Instalasi Dependensi

Masuk ke folder proyek guess_battle/, lalu jalankan:
```bash
pip install colorama
```
### 3. Jalankan Game

Gunakan perintah berikut di terminal:
```bash
python main.py
```
### 4. Aturan Main

    - Masukkan nama kamu untuk login.

    - Mainkan semua 3 level secara berurutan.

    - Tebak angka sesuai rentang dan jumlah percobaan yang tersedia.

    - Setiap tebakan akan diberi petunjuk apakah terlalu besar atau kecil.

    - Setelah semua level selesai, skor kamu akan disimpan otomatis dan dibandingkan dengan pemain lain.

## 🏆 Contoh Tampilan Akhir

```bash
=== Selamat Datang di Guess Battle ===
Masukkan nama pemain: Rayhan

[LEVEL 1] Tebak angka antara 1-10
Masukkan tebakan: 5
➡️ Terlalu kecil!
Masukkan tebakan: 8
🎉 Benar! Kamu menang!

Skor kamu: 245

[LEVEL 2] ...
...
TOP 5 PEMAIN TERBAIK:
1. Rayhan - 560 poin
2. Dita - 510 poin
3. Andi - 450 poin
```

## 👨‍💻 Konsep yang Digunakan

    - Loop & Conditional → Mengatur alur permainan dan logika tebakan

    - Modularisasi → Program dibagi menjadi beberapa file agar lebih terstruktur

    - File Handling & JSON → Menyimpan dan membaca skor pemain

    - Error Handling (try-except) → Menangani input yang tidak valid

    - Colorama → Memberi efek warna pada teks di terminal
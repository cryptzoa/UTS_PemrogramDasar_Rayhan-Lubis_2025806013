import os
import csv
import json
import argparse

def load_csv(file_path):
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"⚠️ File tidak ditemukan: {file_path}")
        return []
    return data

def convert_to_json(data, output_file):
    with open(output_file, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)
    print(f"✅ File JSON berhasil dibuat: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Konversi CSV ke JSON otomatis.")
    parser.add_argument('--file', help='Nama file CSV yang akan dibaca', default=None)
    args = parser.parse_args()

    # Jika user tidak memberikan argumen --file, otomatis cari di ../c/
    if args.file is None:
        base_dir = os.path.dirname(__file__)          # folder tempat main.py berada
        csv_path = os.path.join(base_dir, "../c/data_mahasiswa.csv")
    else:
        csv_path = args.file

    csv_path = os.path.abspath(csv_path)
    print(f"📄 Membaca file CSV dari: {csv_path}")

    data = load_csv(csv_path)

    if not data:
        print("❌ Gagal membaca data CSV.")
        return

    output_json = os.path.join(os.path.dirname(csv_path), "data_mahasiswa.json")
    convert_to_json(data, output_json)

if __name__ == "__main__":
    main()

#include <stdio.h>
#include <string.h>

typedef struct {
    char nama[50];
    char nim[20];
    float nilai;
    char mutu[2];
} Mahasiswa;

// Fungsi untuk menentukan huruf mutu berdasarkan nilai
const char* tentukan_mutu(float nilai) {
    if (nilai >= 85) return "A";
    else if (nilai >= 70) return "B";
    else if (nilai >= 60) return "C";
    else if (nilai >= 50) return "D";
    else return "E";
}

// Fungsi bubble sort berdasarkan nilai
void bubble_sort(Mahasiswa mhs[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (mhs[j].nilai < mhs[j + 1].nilai) {
                Mahasiswa temp = mhs[j];
                mhs[j] = mhs[j + 1];
                mhs[j + 1] = temp;
            }
        }
    }
}

int main() {
    Mahasiswa data[] = {
        {"Rina", "2310001", 85.5, ""},
        {"Doni", "2310002", 61.5, ""},
        {"Sinta", "2310003", 72.0, ""},
        {"Andi", "2310004", 90.0, ""},
        {"Lina", "2310005", 58.0, ""}
    };
    int jumlah = sizeof(data) / sizeof(data[0]);

    // Tentukan mutu tiap mahasiswa
    for (int i = 0; i < jumlah; i++) {
        strcpy(data[i].mutu, tentukan_mutu(data[i].nilai));
    }

    // Urutkan berdasarkan nilai (descending)
    bubble_sort(data, jumlah);

    // Tulis ke file CSV
    FILE *f = fopen("data_mahasiswa.csv", "w");
    if (!f) {
        perror("Gagal membuat file");
        return 1;
    }

    for (int i = 0; i < jumlah; i++) {
        fprintf(f, "%s,%s,%.2f,%s\n", data[i].nama, data[i].nim, data[i].nilai, data[i].mutu);
    }

    fclose(f);
    printf("✅ File 'data_mahasiswa.csv' berhasil dibuat dan diurutkan berdasarkan nilai!\n");
    return 0;
}

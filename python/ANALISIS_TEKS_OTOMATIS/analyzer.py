from utils import count_vowels_and_consonants, get_word_frequency, ascii_bar_chart

def analyze_text(input_file="input.txt", output_file="report.txt"):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"❌ File '{input_file}' tidak ditemukan.")
        return

    lines = text.strip().split("\n")
    word_counter = get_word_frequency(text)
    vowel_count, consonant_count = count_vowels_and_consonants(text)

    total_lines = len(lines)
    total_words = sum(word_counter.values())
    top_5_words = word_counter.most_common(5)

    # === Tulis hasil ke report.txt ===
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("=== LAPORAN ANALISIS TEKS ===\n")
        out.write(f"Jumlah baris: {total_lines}\n")
        out.write(f"Jumlah kata: {total_words}\n")
        out.write(f"Jumlah huruf vokal: {vowel_count}\n")
        out.write(f"Jumlah huruf konsonan: {consonant_count}\n\n")
        out.write("5 Kata Paling Sering Muncul:\n")
        for word, count in top_5_words:
            out.write(f"{word}: {count}\n")

    print("\n=== HASIL ANALISIS ===")
    print(f"Jumlah baris       : {total_lines}")
    print(f"Jumlah kata        : {total_words}")
    print(f"Jumlah huruf vokal : {vowel_count}")
    print(f"Jumlah konsonan    : {consonant_count}")
    print("\nTop 5 Kata Terbanyak:")
    for word, count in top_5_words:
        print(f"  {word}: {count}")

    ascii_bar_chart(word_counter, top_n=5)
    print(f"\n📁 Hasil lengkap disimpan ke '{output_file}'")

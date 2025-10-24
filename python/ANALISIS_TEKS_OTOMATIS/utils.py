import re
from collections import Counter

def count_vowels_and_consonants(text):
    vowels = "aiueoAIUEO"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    v_count = sum(1 for ch in text if ch in vowels)
    c_count = sum(1 for ch in text if ch in consonants)
    return v_count, c_count

def get_word_frequency(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return Counter(words)

def ascii_bar_chart(counter, top_n=5):
    top_items = counter.most_common(top_n)
    print("\n📊 Grafik Frekuensi Kata:")
    for word, count in top_items:
        print(f"{word:<10} {'#' * count}")

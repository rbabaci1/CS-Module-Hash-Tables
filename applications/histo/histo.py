import sys

sys.path.append("../word_count")
from word_count import word_count


def draw_histogram(file_name):
    with open(file_name) as f:
        words = f.read()
    words = word_count(words)
    sorted_words = sorted(words.items(), key=lambda x: (-x[1], x[0]))
    longest_word = max(len(w) for w in words)

    for x in sorted_words:
        res = " " * (longest_word - len(x[0]) + 2)
        for _ in range(x[1]):
            res += "#"
        print(f"{x[0].lower()}{res}")


draw_histogram("robin.txt")

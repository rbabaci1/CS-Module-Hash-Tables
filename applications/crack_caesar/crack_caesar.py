# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

letters_frequencies = [
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",
]

letters_map = {}


def count_occurrences(characters):
    result = {}
    for c in characters:
        if c.isalpha():
            if c in result:
                result[c] += 1
            else:
                result[c] = 1
    return sorted(result.items(), key=lambda x: x[1], reverse=True)


def crack_caesar_sipher(file_name):
    with open(file_name) as f:
        words = f.read()

    characters = list(words)
    letters_occurrences = count_occurrences(characters)

    for i, s in enumerate(letters_occurrences):
        letters_map[s[0]] = letters_frequencies[i]

    for i, c in enumerate(characters):
        if c.isalpha():
            characters[i] = letters_map[c]
    return "".join(characters)


print(crack_caesar_sipher("ciphertext.txt"))

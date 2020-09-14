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


def create_map(characters):
    result = {}
    for c in characters:
        if c.isalpha():
            if c in result:
                result[c] += 1
            else:
                result[c] = 1

    result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    for i, c in enumerate(result):
        result[c] = letters_frequencies[i]
    return result


def crack_caesar_sipher(file_name):
    with open(file_name) as f:
        words = f.read()

    characters = list(words)
    letters_map = create_map(characters)

    for i, c in enumerate(characters):
        if c.isalpha():
            characters[i] = letters_map[c]
    return "".join(characters)


print(crack_caesar_sipher("ciphertext.txt"))

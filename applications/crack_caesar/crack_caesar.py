# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

letters_frequency = {
    "E": 11.53,
    "T": 9.75,
    "A": 8.46,
    "O": 8.08,
    "H": 7.71,
    "N": 6.73,
    "R": 6.29,
    "I": 5.84,
    "S": 5.56,
    "D": 4.74,
    "L": 3.92,
    "W": 3.08,
    "U": 2.59,
    "G": 2.48,
    "F": 2.42,
    "B": 2.19,
    "M": 2.18,
    "Y": 2.02,
    "C": 1.58,
    "P": 1.08,
    "K": 0.84,
    "V": 0.59,
    "Q": 0.17,
    "J": 0.07,
    "X": 0.07,
    "Z": 0.03,
}


def get_closest_value(set1, set2, val):
    diff_1 = abs(set1[1] - val)
    diff_2 = abs(set2[1] - val)

    return set2[0] if diff_2 < diff_1 else set1[0]


def get_letter(freq):
    start, end = 0, len(letters_frequency) - 1
    items = list(letters_frequency.items())

    while start <= end:
        mid = (start + end) // 2
        value = items[mid][1]
        if freq == value:
            return items[mid][0]

        if freq < value:
            if len(items) == mid + 1:
                return items[mid][0]

            if freq > items[mid + 1][1]:
                return get_closest_value(items[mid], items[mid + 1], freq)
            start = mid + 1
        else:
            if mid == 0:
                return items[mid][0]

            if freq < items[mid - 1][1]:
                return get_closest_value(items[mid], items[mid - 1], freq)
            end = mid - 1


print(get_letter(21))


def crack_caesar_sipher(file_name):
    with open(file_name) as f:
        words = f.read()
    words = words.split()


# crack_caesar_sipher("ciphertext.txt")

import random
import sys

# Read in all the words in one go
with open(
    "/Users/rab22/Lambda_School/CS/Unit_2/CS-Module-Hash-Tables/applications/markov/input.txt"
) as f:
    words = f.read()


# TODO: analyze which words can follow other words
words = words.split()
dictionary = {}

for i in range(len(words) - 1):
    word = words[i]
    if word in dictionary:
        dictionary[word].append(words[i + 1])
    else:
        dictionary[word] = [words[i + 1]]


# TODO: construct 5 random sentences


def generateText(max_sentences=5):
    word = random.choice(list(dictionary))
    print(word.capitalize(), end=" ")
    quote, new_line, num_sentences = "", False, 0

    for _ in dictionary:
        word = random.choice(dictionary[word])
        w = word
        if new_line:
            w = word.capitalize()
        new_line = False

        if w.startswith(('"', "'")):
            quote += w[0]

        if w.endswith((".", "!", "?", '."', '!"', '?"')):
            if not w.endswith(quote):
                w += quote
            num_sentences += 1
            new_line, quote = True, ""

            print(f"{w}\n")
            if num_sentences == max_sentences:
                break
        else:
            print(w, end=" ")


generateText(3)


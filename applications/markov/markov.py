import random
import sys

# Read in all the words in one go
with open("input.txt") as f:
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


def generateText():
    word = random.choice(list(dictionary))
    print(word.capitalize(), end=" ")

    for w in dictionary:
        word = random.choice(dictionary[word])
        print(word, end=" ")
        if word.endswith((".", "!", "?")):
            break

    # sys.stdout.write("\b.\n")


generateText()


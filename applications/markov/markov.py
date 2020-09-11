import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
words = words.split()
dictionary = {}

for i in range(len(words) - 1):
    word = words[i]
    if word in dictionary:
        dictionary[word].add(words[i + 1])
    else:
        dictionary[word] = set()
        dictionary[word].add(words[i + 1])

print(dictionary)
# TODO: construct 5 random sentences
# Your code here


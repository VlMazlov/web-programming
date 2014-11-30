__author__ = 'vlmazlov'

import string

file = open(input(), 'r')
words = {}

for word in file.read().split():

    word = word.strip(string.punctuation)

    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

for word in words:
    print(word, words[word])

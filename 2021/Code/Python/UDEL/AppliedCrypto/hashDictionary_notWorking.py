import hashlib

f = file('dictionary.txt', 'r')

words = [words.strip() for word in f]

words[0]

f.close()
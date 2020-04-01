# import hashlib

# f = open('C:/Users/Darius/Desktop/Projects/helloworld/Udel/AppliedCrypto/test.txt', 'r+')

# words = [word.strip() for word in f] 
# print(words)

# f.close()

import hashlib, cProfile

f=open('C:/Users/Darius/Desktop/Projects/helloworld/Udel/AppliedCrypto/test.txt','r')
words = [word.strip() for word in f]
f.close()

secretHash=hashlib.sha512("banana").hexdigest()

def checkDictionary(secret):
    return [word for word in words if hashlib.sha512(word).hexdigest() == secret]

cProfile.run('checkDictionary(secretHash)')
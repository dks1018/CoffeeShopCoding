import hashlib, os,random

# m = hashlib.sha256()
# m.update(b"Nobody inspects")
# m.update(b" the spammish repetition")
# print(m.digest())
password = input()
print(hashlib.sha256(str(password).encode('utf-8')).hexdigest())

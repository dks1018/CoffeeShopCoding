import secrets
import string
import os

rand_bytes = secrets.token_bytes(16)


alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(16))

random_key = os.urandom(16)

print(random_key)
print(password)
print(rand_bytes)
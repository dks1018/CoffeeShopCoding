from Cryptodome.Cipher import AES

key = b'0123456789abcdef'
IV = 16 * b'\x00'  # needs to be encoded, too!
mode = AES.MODE_CBC
encryptor = AES.new(key, mode, IV=IV)

text = b'j' * 64 + b'i' * 128
ciphertext = encryptor.encrypt(text)

print(ciphertext)
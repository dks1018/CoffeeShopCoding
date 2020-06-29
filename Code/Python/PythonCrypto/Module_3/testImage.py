# file = open('C:\\Users\\dks10\\OneDrive\\Desktop\\Projects\\Code\\Python\\PythonCrypto\\Module_3\\eye.png', 'rb')
file = open('encrypt_eye.png', 'rb')
image = file.read()
file.close()

image = bytearray(image)

key = 48

for index, value in enumerate(image):
    image[index] = value^key

file = open('2eye.png','wb')
file.write(image)

file.close()
from cryptography.fernet import Fernet
from Cryptodome.Cipher import AES
from Cryptodome.Cipher import Random
from PIL import Image
import os
import secrets
import string

def encrypt_AES():
    aes_key = gen_AES_key()
    iv_key = gen_iv()
    AES = AES.new(aes_key, AES.MODE_CBC, iv_key)
    
def gen_AES_key():
    rand_bytes = secrets.token_bytes(16)
    let_val = string.ascii_letters + string.digits
    secret_val = ''.join(secrets.choice(let_val) for i in range(16))
    random_key = os.urandom(16)

    key = rand_bytes

    return key

def gen_iv():
    rand_bytes = secrets.token_bytes(16)
    let_val = string.ascii_letters + string.digits
    secret_val = ''.join(secrets.choice(let_val) for i in range(16))
    random_key = os.urandom(16)

    key = rand_bytes

    return key

def generate_key():
    key = Fernet.generate_key()
    return key

def save_key():
    file = open('key.key', 'wb')
    store_key = generate_key()
    file.write(store_key)
    file.close()

def get_key():
    file = open('key.key', 'rb')
    get_stored_key = file.read()
    file.close()

    return get_stored_key

def get_image():
    file = open('C:\\Users\\dks10\\OneDrive\\Desktop\\Projects\\Code\\Python\\PythonCrypto\\Module_3\\eye.png', 'rb')
    # image = Image.open(r"C:\Users\dks10\OneDrive\Desktop\Projects\Code\Python\PythonCrypto\Module_3\eye.png") 
    
    return file

def create_image():
    enc_image = bytearray(get_image())
    key = get_key()
    enc_image = open('encrypt_eye.png','wb')
    enc_image.write(enc_image)

    return enc_image

def store_encrypted_message(enc_image):
    file = open('stored_message.txt', 'wb')
    file.write(enc_image)
    file.close()

def read_stored_message():
    file = open('stored_message.txt', 'rb')
    get_stored_message = file.read()
    file.close()

    return get_stored_message

def encrypt_with_key():
    f_key = Fernet(get_key())
    message_encrypted = f_key.encrypt(create_image().encode())
    store_encrypted_message(message_encrypted)

    return message_encrypted

def decrypt_message():
    f_key = Fernet(get_key())
    message_decrypted = f_key.decrypt(read_stored_message())
    decoded_message = message_decrypted.decode()

    return decoded_message

def show_image():
    im = Image.open(r"C:\Users\dks10\OneDrive\Desktop\Projects\Code\Python\PythonCrypto\Module_3\eye.png")
    im.show()

def main():
    save_key()
    encrypted_message = encrypt_with_key()
    decrypted_message = decrypt_message()
    # print(encrypted_message)
    # print(decrypted_message)
    while(True):
        user_input = str(input("\tIf you would like to see you encrypted enc_image type 1.\n\
    \tIf you would like to see your decrypted enc_image type 2.\n\
    \tIf you would like to quit type q.\n"))
        if(user_input == "1"):
            print(encrypted_message,"\n")
        elif(user_input == "2"):
            print(decrypted_message,"\n")
        elif(user_input == "q"):
            break
        else:
            print("Please enter a valid choice.")

if __name__ == "__main__":
    main()
from cryptography.fernet import Fernet
from Cryptodome.Cipher import AES

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

def create_message():
    message = str(input("Enter the message you want to encrypt: "))

    return message

def store_encrypted_message(message):
    file = open('stored_message.txt', 'wb')
    file.write(message)
    file.close()

def read_stored_message():
    file = open('stored_message.txt', 'rb')
    get_stored_message = file.read()
    file.close()

    return get_stored_message

def encrypt_with_key():
    f_key = Fernet(get_key())
    message_encrypted = f_key.encrypt(create_message().encode())
    store_encrypted_message(message_encrypted)

    return message_encrypted

def decrypt_message():
    f_key = Fernet(get_key())
    message_decrypted = f_key.decrypt(read_stored_message())
    decoded_message = message_decrypted.decode()

    return decoded_message

def main():
    save_key()
    encrypted_message = encrypt_with_key()
    decrypted_message = decrypt_message()
    # print(encrypted_message)
    # print(decrypted_message)
    while(True):
        user_input = str(input("\tIf you would like to see you encrypted message type 1.\n\
    \tIf you would like to see your decrypted message type 2.\n\
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
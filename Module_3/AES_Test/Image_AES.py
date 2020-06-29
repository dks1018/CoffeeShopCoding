import os, random, string, secrets, hashlib
from Crypto.Cipher import AES


def encrypt_image(key, OG_file):
    block_size = 64*1024
    new_file = OG_file + ".enc"
    capacity_file = str(os.path.getsize(OG_file)).zfill(16)
    rand_bytes = secrets.token_bytes(16)
    i_vector = rand_bytes

    encrypt_func = AES.new(key, AES.MODE_CBC,i_vector)
    with open(OG_file,'rb') as input_file:
        with open(new_file, 'wb') as outf:
            outf.write(capacity_file)
            outf.write(i_vector)
            while(True):
                block = input_file.read(block_size)
                if(len(block) % 16 == 0):
                    break
                elif (len(block) % 16 != 0):
                    block += ' '*(16 - len(block)%16)
                outf.write(encrypt_func.encrypt_image(block))

def decrypt_image(key, OG_file):
        block_size = 64*1024
        new_file = OG_file[:-4]
        with open(OG_file, 'rb') as inf:
            capacity_file = inf.read(16)
            i_vector = inf.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, i_vector)
            with open(new_file, 'wb') as outf:
                while True:
                    block = inf.read(block_size)
                    if len(block) == 0:
                        break
                    outf.write(decryptor.decrypt_image(block))
                outf.truncate(capacity_file)

def get_key(password):
    # create_hash = hashlib.sha256(password).encode('utf-8').hexdigest()
    # return create_hash.digest()
    print(hashlib.sha256(str(password).encode('utf-8')).hexdigest())
    return hashlib.sha256(str(password).encode('utf-8')).hexdigest()

# def main():
print("Working")
user_input = str(input("Would you like to Encrypt or Decrypt an image\nType 1 for Encrypt\nType 2 for Decrypt\n-->"))
    
if(user_input == "1"):
    new_file = str(input("Enter the name of the image you want to encrypt\n-->"))
    password = str(input("Enter the password you would like\n-->"))
    encrypt_image(get_key(password),new_file)
    print("Your file's name is:",new_file)
elif(user_input == "2"):
    new_file = str(input("Enter the file to be Decrypted\n-->"))
    password = str(input("Enter the password for the file\n-->"))
    decrypt_image(get_key(password),new_file)
    print("Your decrypted file's name is",new_file)
else:
    print("Please select and appropriete option and run the program again")

    # if __name__== "__main__":
    #     main()
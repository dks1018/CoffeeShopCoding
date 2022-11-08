# Imports PIL module 
from PIL import Image

def open_image():
    # open method used to open different extension image file 
    im = Image.open(r"C:\Users\dks10\OneDrive\Desktop\Projects\Code\Python\PythonCrypto\Module_3\eye.png")  

    file = open('C:\\Users\\dks10\\OneDrive\\Desktop\\Projects\\Code\\Python\\PythonCrypto\\Module_3\\eye.png', 'rb')
    # file = open('eye.png', 'rb')
    open_f = file.read()
    # print(file)
    print(open_f)
    # This method will show image in any image viewer  
    im.show()

open_image()

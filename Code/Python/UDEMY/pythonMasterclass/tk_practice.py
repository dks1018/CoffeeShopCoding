try:
    import tkinter
except ImportError: #python 2
    import Tkinter as tkinter

#set main window variable to show the windowed GUI
mainWindow = tkinter.Tk()

#Main Windppw Title
mainWindow.title("Smith & Turner")

#Set the size of the box
mainWindow.geometry('640x480+400+200')

#Set name of label
label = tkinter.Label(mainWindow, text="Busey BnB")
label.pack(side='top')

#
leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
#Create canvas inside of main window
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=5)
canvas.pack(side='left', anchor='n')

#set up right frame
rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand='True')

# canvas.pack(side='left', fill=tkinter.Y)
# canvas.pack(side='left', fill=tkinter.X, expand=True)
# canvas.pack(side='top', fill=tkinter.X)
# canvas.pack(side='top', fill=tkinter.Y, expand=True)
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)

#Create buttons
button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
# button1.pack(side='top', anchor='n')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')


mainWindow.mainloop()


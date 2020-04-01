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
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)
#Create canvas inside of main window
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=5)
canvas.grid(row=1, column=0)

#set up right frame
rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')

#Create buttons
button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
# button1.pack(side='top', anchor='n')
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

#Configure columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)

mainWindow.grid_columnconfigure(2, weight=2)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0,weight=1)
button2.grid(sticky='ew')

mainWindow.mainloop()


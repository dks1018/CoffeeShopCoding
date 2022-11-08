# try:
#     import tkinter
# except ImportError: #python 2
#     import Tkinter as tkinter
import tkinter

def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin,x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())

def plot(page, x, y):
    page.create_line(x, y, x + 1, y + 1, fill="red")
    
mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("1080x720")

canvas1 = tkinter.Canvas(mainWindow, width=540, height=720)
canvas1.grid(row=0, column=0)

canvas2 = tkinter.Canvas(mainWindow, width=540,height=720, background='blue')
canvas2.grid(row=0, column=1)

print(repr(canvas1), repr(canvas2))
draw_axes(canvas1)
draw_axes(canvas2)

def parabola(x):
    y = x * x / 100
    return y
for x in range(-100, 100):
    y = parabola(x)
    plot(canvas1, x, -y)
for x in range(-100, 100):
    y = parabola(x)
    plot(canvas2, x, -y)
    
mainWindow.mainloop()
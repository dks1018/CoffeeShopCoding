# try:
#     import tkinter
# except ImportError: #python 2
#     import Tkinter as tkinter
import tkinter
import math

def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin,x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())
    

def circle(page, radius, g, h):
    page.create_oval(g * radius, h * radius, g - radius, h- radius, outline="red", width=10)
    
    
# def circle(page, radius, g, h):
#     for x in range(g * 100, (g + radius) * 100):
#         x /= 100
#         print(x)
#         y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2 )))
#         plot(page, x, y)
#         plot(page, x, 2 * h - y)
#         plot(page, 2 * g - x, y)
#         plot(page, 2 * g - x, 2 * h - y)
        
    
def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red", width=10)
    
    
def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)
    
    
mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("1080x720")

canvas1 = tkinter.Canvas(mainWindow, width=1080, height=720)
canvas1.grid(row=0, column=0)

draw_axes(canvas1)
parabola(canvas1,100)
parabola(canvas1,200)
circle(canvas1, 100,100,100)
circle(canvas1, 100,100,-100)
circle(canvas1, 100,-100,100)
circle(canvas1, 100,-100,-100)
circle(canvas1, 10,30,30)
circle(canvas1, 10,30,-30)
circle(canvas1, 10,-30,30)
circle(canvas1, 10,-30,-30)
circle(canvas1, 30,0,0)

mainWindow.mainloop()
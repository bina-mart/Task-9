from tkinter import *
import random
window = Tk()
window.geometry('500x500')
def triangle():
    canvas.create_line(230, 10, 290, 60)
    canvas.create_line(230, 10, 60, 290)
    canvas.create_line(60, 290, 290, 60)
def rectangle():
    canvas.create_rectangle(80, 180, 310, 370)
def oval ():
    canvas.create_oval(80, 180, 310, 370)
def change():
    canvas.delete('all')
    functions = (triangle, rectangle, oval)
    choice = random.choice(functions)
    choice()
button = Button(window, text='change', command=change)
button.pack()
canvas = Canvas(window, height=500, width=500)
canvas.pack()
window.mainloop()
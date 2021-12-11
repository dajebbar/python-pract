import sys
from tkinter import *

# Paint Function


def paint(e):
    ''''''
    # Brush Parameters


root = Tk()
root.title('Funny Painter Paint')
root.geometry('800x600')
if sys.platform.startswith('win'):
    root.iconbitmap('img/infinity.ico')
else:
    icon = PhotoImage(file='img/infinity.gif')
    root.call('wm', 'iconphoto', root._w, icon)

# Variables
x1 = IntVar()
y1 = IntVar()
x2 = IntVar()
y2 = IntVar()

# Adding Canvas
canvas = Canvas(root, width=500, height=400, bg='light grey')
canvas.bind('<B1-Motion>', paint)
canvas.pack(pady=20)


root.mainloop()

import sys
from tkinter import *

# Paint Function


def paint(e):
    ''''''
    # Brush Parameters
    brush_width = 20
    brush_color = 'light green'
    brush_type = BUTT

    # Srating Position
    x1.set(e.x - 1)
    y1.set(e.y - 1)

    # Ending Position
    x2.set(e.x + 1)
    y2.set(e.y + 1)

    # Draw on the Canvas
    canvas.create_line(x1.get(), y1.get(), x2.get(), y2.get(),
                       fill=brush_color, width=brush_width, capstyle=brush_type, smooth=True)


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

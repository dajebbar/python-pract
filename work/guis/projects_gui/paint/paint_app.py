import sys
import tkinter.ttk as ttk
from tkinter import *

# Paint Function


def paint(e):
    ''''''
    # Brush Parameters
    brush_width = 20
    brush_color = 'green'
    # BRUSH TYPE: BUTT, ROUND, PROJECTING
    brush_type = PROJECTING

    # Srating Position
    x1.set(e.x - 1)
    y1.set(e.y - 1)

    # Ending Position
    x2.set(e.x + 1)
    y2.set(e.y + 1)

    # Draw on the Canvas
    canvas.create_line(x1.get(), y1.get(), x2.get(), y2.get(),
                       fill=brush_color, width=brush_width, capstyle=brush_type, smooth=True)

# change brush size Function


def change_brush_size():
    ''''''


root = Tk()
root.title('Funny Painter Paint')
root.geometry('800x800')
if sys.platform.startswith('win'):
    root.iconbitmap('img/infinity.ico')
else:
    icon = PhotoImage(file='img/infinity.gif')
    root.call('wm', 'iconphoto', root._w, icon)

# Variables
w = 600
h = 400
x1 = IntVar()
y1 = IntVar()
x2 = IntVar()
y2 = IntVar()

# Adding Canvas
canvas = Canvas(root, width=w, height=h, bg='white')
canvas.bind('<B1-Motion>', paint)
canvas.pack(pady=20)

# Create Brush Options Frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)

# Brush Size
brush_size_frame = LabelFrame(brush_options_frame, text='Brush Size')
brush_size_frame.grid(row=0, column=0, padx=50)

# Brush Slider
my_slider = ttk.Scale(brush_size_frame, from_=1, to=100,
                      command=change_brush_size, orient=VERTICAL, value=10)
my_slider.pack(padx=10, pady=10)

# Brush Slider Label
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)


root.mainloop()

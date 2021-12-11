import sys
import tkinter.ttk as ttk
from tkinter import *
from tkinter import colorchooser
# from PIL import Image, ImageTk
from tkinter import filedialog

# Paint Function


def paint(e):
    ''''''
    # Brush Parameters
    brush_width = f'{my_slider.get():0.0f}'
    # brush_colors = 'green'
    # BRUSH TYPE: BUTT, ROUND, PROJECTING
    brush_types = brush_type.get()

    # Srating Position
    x1.set(e.x - 1)
    y1.set(e.y - 1)

    # Ending Position
    x2.set(e.x + 1)
    y2.set(e.y + 1)

    # Draw on the Canvas
    canvas.create_line(x1.get(), y1.get(), x2.get(), y2.get(),
                       fill=brush_color, width=brush_width, capstyle=brush_types, smooth=True)

# change brush size Function


def change_brush_size(e):
    ''''''
    slider_label.config(text=f'{my_slider.get():0.0f}')

# change brush color Function


def change_brush_color():
    ''''''
    global brush_color
    # brush_color = 'black'
    brush_color = colorchooser.askcolor(color=brush_color)[-1]

# change canvas color Function


def change_canvas_color():
    ''''''
    global canvas_color
    # canvas_color = 'white'
    canvas_color = colorchooser.askcolor(color=canvas_color)[-1]
    canvas.config(bg=canvas_color)

# Clear Screen function


def clear_screen():
    ''''''
    canvas.delete(ALL)
    canvas['bg'] = 'white'


def save_image():
    ''''''
    result = filedialog.asksaveasfilename(initialdir='img', filetypes=(
        ('png files', '*.png'), ('all files', '*.*')))


root = Tk()
root.title('Funny Painter Paint')
root.geometry('700x700')
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
brush_type = StringVar()
# brush_color = StringVar()
brush_color = 'black'
# canvas_color = StringVar()
canvas_color = 'white'
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

# Brush Type
brush_type_frame = LabelFrame(
    brush_options_frame, text='Brush Type', width=400)
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type.set('round')
# Create Radio Buttons for Brush Types
brush_type_radio1 = Radiobutton(
    brush_type_frame, text='Round', variable=brush_type, value='round')
brush_type_radio2 = Radiobutton(
    brush_type_frame, text='Slash', variable=brush_type, value='butt')
brush_type_radio3 = Radiobutton(
    brush_type_frame, text='Diamond', variable=brush_type, value='projecting')
brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# Change Colors
change_color_frame = LabelFrame(brush_options_frame, text='Change Colors')
change_color_frame.grid(row=0, column=2)

# Color Button
brush_color_btn = Button(
    change_color_frame, text='Brush Color', command=change_brush_color)
brush_color_btn.pack(padx=10, pady=10)

# Change Canvas Background Color
canvas_color_btn = Button(
    change_color_frame, text='Canvas Color', command=change_canvas_color)
canvas_color_btn.pack(padx=10, pady=10)

# Program Options Frame
options_frame = LabelFrame(brush_options_frame, text='Program Options')
options_frame.grid(row=0, column=3, padx=50)

# Clear Screen Button
clear_btn = Button(options_frame, text='Clear Screen', command=clear_screen)
clear_btn.pack(padx=10, pady=10)

# Save Image Button
save_btn = Button(options_frame, text='Save Image', command=save_image)
save_btn.pack(pady=10, padx=10)

root.mainloop()

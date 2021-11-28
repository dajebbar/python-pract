from tkinter import *


def fake_command():
    """"""

def new():
    hide_frames()
    file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

def cut():
    hide_frames()
    edit_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

def hide_frames():
    edit_frame.grid_forget()
    file_frame.grid_forget()

root = Tk()
root.geometry('400x400')
root.title('Menu and Frames')
root.iconbitmap('img/favicon.ico')

# Define menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create menu items
# File menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new)
file_menu.add_separator()
file_menu.add_command(label='Quit', command=root.quit)

# Edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_cascade(label='Cut', command=cut)
edit_menu.add_cascade(label='Copy', command=fake_command)
edit_menu.add_cascade(label='Past', command=fake_command)



# File Menu Frame
file_frame = Frame(root, width=200, height=200, bd=5, bg='blue')
# file_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

label_title = Label(file_frame, text='File Frame', font=('Montserrat', 20))
label_title.pack(pady=20, padx=20)

# Edit Menu Frame
edit_frame = Frame(root, width=200, height=200, bd=5, bg='blue')
# edit_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

label_cut__frame = Label(edit_frame, text='Cut Frame', font=('Montserrat', 20))
label_cut__frame.pack(pady=20, padx=20)





root.mainloop()
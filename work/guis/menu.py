from tkinter import *


def fake_command():
    """"""
    Label(root, text='fake commande', font=('Helvetica 15 bold')).pack()

def show():
    """"""
    my_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

def hide():
    """"""
    # global my_frame
    my_frame.grid_forget()

root = Tk()
root.geometry('400x400')
root.title('Menu')
root.iconbitmap('img/favicon.ico')

# Define menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create menu items
# File menu
file_menu = Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=fake_command)
file_menu.add_separator()
file_menu.add_command(label='Quit', command=root.quit)

# Edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_cascade(label='Undo', command=fake_command)

show_btn = Button(root, text='Show', command=show)
hide_btn = Button(root, text='Hide', command=hide)

show_btn.grid(row=0, column=0)
hide_btn.grid(row=0, column=1)


my_frame = Frame(root, width=200, height=200, bd=5, bg='blue')
my_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

label_title = Label(my_frame, text='Hello world!', font=('Montserrat', 20))
label_title.pack(pady=20, padx=20)





root.mainloop()
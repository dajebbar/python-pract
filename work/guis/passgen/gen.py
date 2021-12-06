import string
from tkinter import *
from tkinter import font
from tkinter.font import Font
from random import randint, choice

def generate_password():
    """
        [generate password]
    """
    pass_min = 6
    pass_max = 12
    all_str = string.ascii_letters + string.punctuation + string.digits
    password = ''.join(choice(all_str) for _ in range(randint(pass_min, pass_max)))
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)


# create window 
window = Tk()

# set params
window.title('Password Generator')
window.geometry('720x480')
window.minsize(width=350, height=300)
window.iconbitmap('img/favicon.ico')
window.config(background='#4065a4')

# create fonts
bigFont = Font(family='Montserrat', size=20, weight='bold')
mediumFont = Font(family='Roboto', size=15)
smallFont = Font(family='Montserrat', size=10)

# create a frame
frame = Frame(window, bg='#4065a4')

# create a canvas
img = PhotoImage(file='img/pass.png').zoom(35).subsample(32)
can = Canvas(frame, width=300, height=300, bg='#4065a4', bd=0, highlightthickness=0)
can.create_image(150, 150, image=img)
can.grid(row=0, column=0, sticky=W)

# create a subframe
right_frame = Frame(frame, bg='#4065a4')

# create title
title_label = Label(right_frame, text='Password', 
                bg='#4065a4', font=mediumFont, fg='white')
title_label.pack()

# create entry
pass_entry = Entry(right_frame, bg='#4065a4', font=bigFont)
pass_entry.pack(fill=X)

# create button
pass_btn = Button(right_frame, text='Generate', bg='#eae2b7', 
                fg='#4065a4',command=generate_password, font=mediumFont)
pass_btn.pack(fill=X)

right_frame.grid(row=0, column=1, sticky=W)

# pack frame
frame.pack(expand=1)

# create a menu bar
menu_bar = Menu(window)
# first menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New password', command=generate_password)
file_menu.add_command(label='Quit', command=window.quit)
menu_bar.add_cascade(label='File', menu=file_menu)
window.config(menu=menu_bar)
# run
window.mainloop()
window.destroy()
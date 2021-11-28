from tkinter import *
from PIL import Image, ImageTk


def clicked():
    global label2
    input = e.get()
    label2 = Label(root, text='your name is ' + input, font=('Montserrat 15 italic bold'))
    label2.pack()

def hide():
    label2.pack_forget()
    # label2.destroy
def show():
    label2.pack()


root = Tk()
root.geometry('400x600')
root.title('Label')

# Add images
img_scarto = ImageTk.PhotoImage(Image.open('img/scarto.jpg'))
img_label = Label(image=img_scarto)
img_label.pack()

# Add labels
label_title = Label(root, text='Enter your name', fg='gray', font=('Roboto', 18))
label_title.pack()

#  Add entry
e = Entry(root, font=('Montserrat 15'))
e.pack(pady=10)

# Add button
btn1 = Button(root, text='clickme', command=clicked)
btn1.pack(pady=20)

# hide button
hide_btn = Button(root, text='Hide', command=hide)
hide_btn.pack(pady=2, fill=X)

# show button
show_btn = Button(root, text='Show', command=show)
show_btn.pack(pady=2, fill=X)



root.mainloop()
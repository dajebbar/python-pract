from tkinter import *

# create radio button function
def radio():
    """"""
    if v.get() == 1:
        my_label = Label(root, text='You clicked One', font=('helvetica', 13))
    elif v.get() == 2:
        my_label = Label(root, text='You clicked Two', font=('helvetica', 13))

    my_label.pack(pady=10)


root = Tk()
root.geometry('400x400')
root.title('Radio Buttons')
root.iconbitmap('img/favicon.ico')

# Radio Buttons

v = IntVar()
v.set(1)

rbtn1 = Radiobutton(root, text='One', variable=v, value=1).pack()
rbtn2 = Radiobutton(root, text='Two', variable=v, value=2).pack()

my_btn = Button(root, text='Click Me', command=radio)
my_btn.pack(pady=20, fill=X)




root.mainloop()
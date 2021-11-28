from tkinter import *


def toppings():
    """"""
    my_label = Label(root, text=v.get())
    my_label.pack(pady=10)

root = Tk()
root.geometry('400x400')
root.title('Checkboxes')
root.iconbitmap('img/favicon.ico')


# Check Boxes
v = StringVar()

my_check = Checkbutton(root, text='pepperoni', variable=v, onvalue='pepperoni', offvalue='no pepperoni')
my_check.deselect()
my_check.pack()

my_btn = Button(root, text='Select Toppings', command=toppings).pack(pady=20)

root.mainloop()
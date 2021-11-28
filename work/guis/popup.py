from tkinter import *
from tkinter import messagebox

# Create popups function
def popups():
    """"""
    msg = messagebox.askyesno('PopUp Title', 'This button display an infos!')
    if msg == 1:
        my_label = Label(root, text='you clicked yes').pack(pady=10)
    else:
        my_label = Label(root, text='you clicked no').pack(pady=10)


# popup boxes
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
root = Tk()
root.geometry('400x400')
root.title('PopUp')
root.iconbitmap('img/favicon.ico')


my_btn = Button(root, text='Click to popup', command=popups)
my_btn.pack(pady=20)

root.mainloop()
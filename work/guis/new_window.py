from tkinter import *

# window btn function
def window():
    new_window = Toplevel()
    btn = Button(new_window, text='Quit', command=new_window.destroy)
    btn.pack()

root = Tk()
root.geometry('400x400')
root.title('Window')
root.iconbitmap('img/favicon.ico')

window_btn = Button(root, text='New window', command=window)
window_btn.pack(pady=20)


root.mainloop()
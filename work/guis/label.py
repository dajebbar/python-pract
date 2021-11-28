from tkinter import *

root = Tk()
root.geometry('400x400')
root.title('Label')

label_title = Label(root, text='hello labels', fg='#fff', bg='#000', font=('Roboto', 32))
# label_title.pack()
label_title.grid(row=0, column=0, columnspan=2)
label_subtitle = Label(root, text='subtitle', font=('Montserrat', 15), relief='raised', state='disable') # relief='sunken'
# label_subtitle.pack(pady=50)
label_subtitle.grid(row=1, column=0, sticky=W)
label3 = Label(root, text='label', font=('Montserrat', 15))
label3.grid(row=2, column=1)



root.mainloop()
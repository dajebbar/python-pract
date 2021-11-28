from tkinter import *
from tkinter import ttk

# select button function
def select():
    if my_combo.get() == 'Sun':
        my_label = Label(root, text='Sunday').pack()
    elif my_combo.get() == 'Mon':
        my_label = Label(root, text='Monday').pack()
    elif my_combo.get() == 'Tue':
        my_label = Label(root, text='Tueday').pack()
    elif my_combo.get() == 'Wen':
        my_label = Label(root, text='Wenday').pack()
    elif my_combo.get() == 'Thu':
        my_label = Label(root, text='Thuday').pack()
    elif my_combo.get() == 'Fri':
        my_label = Label(root, text='Friday').pack()
    elif my_combo.get() == 'Sat':
        my_label = Label(root, text='Satday').pack()

root = Tk()
root.geometry('400x400')
root.title('PopUp')
root.iconbitmap('img/favicon.ico')

# combobox
days_of_week = [
    'Sun',
    'Mon',
    'Tue',
    'Wen',
    'Thu',
    'Fri',
    'Sat',
]

my_combo = ttk.Combobox(root, values=days_of_week)
my_combo.current(1)
my_combo.pack(pady=10)

my_btn = Button(root, text='Select day', command=select)
my_btn.pack(pady=10)


root.mainloop()
from tkinter import *


def feet_to_meter():
    ''''''
    global feet_entry
    inputs = round(float(feet_entry.get()) * 0.3048, 3)
    meter_lab = Label(root, text=str(inputs), font=('Roboto', 13))
    meter_lab.grid(row=1, column=1)


root = Tk()

root.title('feet to Meters')
root.geometry('600x150')

feet_entry = Entry(root, font=('Roboto', 13))
feet_label = Label(root, text='feet', font=('Roboto', 15))
text_label = Label(root, text='is equivalent to ', font=('Roboto', 15))
# meter_entry = Entry(root, font=('Roboto', 13))
meter_txt = Label(root, text='meters', font=('Roboto', 15))

calculate_btn = Button(root, text='Calculate', font=('Roboto', 15), command=feet_to_meter)


feet_entry.grid(row=0, column=1)
feet_label.grid(row=0, column=2)
text_label.grid(row=1, column=0)
# meter_entry.grid(row=1, column=1)
meter_txt.grid(row=1, column=2)
calculate_btn.grid(row=2, column=2)


root.mainloop()

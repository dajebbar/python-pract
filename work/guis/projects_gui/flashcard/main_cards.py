from tkinter import *
from random import randint
# from PIL import Image, ImageTk
import string
import sys


def main():
    # Add Function
    def add():
        ''''''
        clear_frames()
        clear()
        def check_add(event):
            if add_result.get() == '' or add_result.get() not in string.digits:
                add_label_result.config(text='Veuillez saisir un chiffre ou un nombre',
                bg='#457b9d')
            else:
                if int(add_result.get()) == num1.get() + num2.get():
                    add_label_result.config(text='Bravo!')
                    # add_frame['bg'] = '#92e6a7'
                    # add_flash['bg'] = '#92e6a7'
                    add_label_result['bg'] = '#92e6a7'
                else:
                    add_label_result.config(text='Résultat incorrect ' + string_add_res.get() +
                     ' = ' + str(num1.get() + num2.get()), bg='#457b9d')
                    # add_frame['bg'] = '#fe5f55'
                    # add_flash['bg'] = '#fe5f55'
                    add_label_result['bg'] = '#fe5f55'
            # Clear Add Entry
            add_result.delete(0, 'end')
            # Set a new numbers
            num1.set(randint(0,10))
            num2.set(randint(0, 10))
            string_add_res.set(str(num1.get()) + ' + ' + str(num2.get()))
            add_flash.config(textvariable=string_add_res)
            # add_frame['bg'] = '#457b9d'
            add_label_result.pack(pady=5)
        # variables
        num1 = IntVar()
        num2 = IntVar()
        num1.set(randint(0,10))
        num2.set(randint(0, 10))
        # Add
        string_add_res = StringVar()
        string_add_res.set(str(num1.get()) + ' + ' + str(num2.get()))
        add_flash.config(textvariable=string_add_res)
        add_flash.pack(pady=10)
        # Add Entry Paching
        add_result.bind('<Return>', check_add)
        add_result.pack(pady=10)
        # Button
        add_btn.config(text='Go', font=('Montserrat 12 italic'), command=lambda: check_add(event=Event))
        add_btn.pack(pady=5)
        # Packing Add frame
        add_frame.pack(fill='both', expand=1)    
    # Substract Function
    def substract():
        ''''''
        clear_frames()
        clear()
        def check_sub(event):
            ''''''
            if sub_result.get() == '' or sub_result.get() not in string.digits:
                sub_label_result.config(text='Veuillez saisir un chiffre ou un nombre',
                bg='#495057')
            else:
                if int(sub_result.get()) == num1.get() - num2.get():
                    sub_label_result.config(text='Bravo!')
                    # sub_frame['bg'] = '#92e6a7'
                    # sub_flash['bg'] = '#92e6a7'
                    sub_label_result['bg'] = '#92e6a7'
                else:
                    sub_label_result.config(text='Résultat incorrect ' + string_sub_res.get() + ' = ' + 
                    str(num1.get() - num2.get()))
                    # sub_frame['bg'] = '#fe5f55'
                    # sub_flash['bg'] = '#fe5f55'
                    sub_label_result['bg'] = '#fe5f55'
             # Clear Sub Entry
            sub_result.delete(0, 'end')
            # Set a new numbers
            num1.set(randint(0,10))
            num2.set(randint(0, 10))
            string_sub_res.set(str(num1.get()) + ' + ' + str(num2.get()))
            sub_flash.config(textvariable=string_sub_res)
            sub_label_result.pack(pady=5)
        # Variables
        num1 = IntVar()
        num2 = IntVar()
        num1.set(randint(0,10))
        num2.set(randint(0, 10))
        # Sub
        string_sub_res = StringVar()
        string_sub_res.set(str(num1.get()) + ' - ' + str(num2.get()))
        # Configure and Paching Sub Card
        sub_flash.config(textvariable=string_sub_res)
        sub_flash.pack(pady=10)
        # Add Entry Paching
        sub_result.bind('<Return>', check_sub)
        sub_result.pack(pady=10)
        # Button
        sub_btn.config(text='Go', font=('Montserrat 12 italic'), command=lambda: check_sub(event=Event))
        sub_btn.pack(pady=5)
        # Packing Add frame
        sub_frame.pack(fill='both', expand=1)

        
    # Multiply Function
    def multiply():
        ''''''
    # Divide Function
    def divide():
        ''''''
    # Ration Function
    def ratio():
        ''''''
    # clear items
    def clear():
        ''''''  
        # Add 
        for wget in add_frame.winfo_children():
            wget.pack_forget()
        # Sub
        for wget in sub_frame.winfo_children():
            wget.pack_forget()
        # Home
        # for wget in home_frame.winfo_children():
        #     wget.pack_forget()
        


        add_frame['bg'] = '#457b9d'
        add_flash['bg'] = '#457b9d'
        sub_frame['bg'] = '#495057'
        sub_flash['bg'] = '#495057'
        add_label_result['bg'] = '#457b9d'
        sub_label_result['bg'] = '#495057'
        add_result.delete(0, 'end')
        sub_result.delete(0, 'end')


    # clear frames
    def clear_frames():
        add_frame.pack_forget()
        sub_frame.pack_forget()
        # home_frame.pack_forget()
        

    # Create App Model
    root = Tk()
    root.geometry('400x400')
    root.title(' Flashcard App')
    if ( sys.platform.startswith('win')): 
        root.iconbitmap('img/infinity.ico')
    else:
        logo = PhotoImage(file='img/infinity.gif')
        root.call('wm', 'iconphoto', root._w, logo)
        # root.iconbitmap('@img/infinity.xbm')
    # root.iconbitmap('img/infinity.ico')
    

    # Define main Menu
    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Create Menu Items
    math_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label='Cards', menu=math_menu)
    math_menu.add_command(label='addition', command=add)
    math_menu.add_command(label='substraction', command=substract)
    math_menu.add_command(label='multiplication', command=multiply)
    math_menu.add_command(label='division', command=divide)
    math_menu.add_command(label='ratio', command=ratio)
    math_menu.add_separator()
    math_menu.add_command(label='Home', command='')
    math_menu.add_separator()
    math_menu.add_command(label='Exit', command=root.quit)
    # Create Math Addition Frame:
    add_frame = Frame(root, width=400, height=400, bg='#457b9d')
    # Create Math Substitution Frame:
    sub_frame = Frame(root, width=400, height=400, bg='#495057')
    # Instantiate add label
    add_flash = Label(add_frame, font=('Montserrat', 32), bg='#457b9d')
    add_label_result = Label(add_frame, font=('Montserrat', 12))
    # Instantiate Math Sub Label
    sub_flash = Label(sub_frame, font=('Montserrat', 32), bg='#495057')
    sub_label_result = Label(sub_frame, font=('Montserrat', 12))

    # Instantiate add Entriy
    add_result = Entry(add_frame, font=('Montserrat', 12))
    # Instantiate sub Entry
    sub_result = Entry(sub_frame, font=('Montserrat', 12))
    # Add Button
    add_btn = Button(add_frame)
    # Sub Button
    sub_btn = Button(sub_frame)
    # Home Interface:
    # home_frame= Frame(root)
    
    # home_frame.pack()

    




    root.mainloop()


if __name__=='__main__':
    main()
from tkinter import *
from random import randint
from tkinter import font



# Create addition function
def add():
    ''''''
    current_status.set('Addition Card App')
    hide_menu_frames()
    add_clear()
    add_frame.pack(fill='both', expand=1)
    # Create two random integers
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    global res
    res = num_1 + num_2
    # Put numbers into screen
    global add_flash
    add_flash = Label(add_frame, text=str(num_1)+' + '+str(num_2)+' = ', font=('Montserrat', 32))
    add_flash.pack(pady=10)
    # Enter results - Answer Entry Box
    global add_result
    add_result = Entry(add_frame, font=('Montserrat', 12))
    add_result.pack(pady=10)
    # Answer Button
    global add_btn
    add_btn = Button(add_frame, text='Answer ', command=addition, font=('Montserrat 13 italic'))
    add_btn.pack(pady=5)
    
# Create substraction function
def substract():
    ''''''
    current_status.set('Substraction Card App')
    hide_menu_frames()
    sub_clear()
    sub_frame.pack(fill='both', expand=1)
    # Create two random integers
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    num_1, num_2 = check_numbers(num_1, num_2)
    global sub_res
    sub_res = num_1 - num_2
    # Put numbers into screen
    global sub_flash
    sub_flash = Label(sub_frame, text=str(num_1)+' - '+str(num_2)+' =', font=('Montserrat', 32))
    sub_flash.pack(pady=10)
    # Enter results
    global sub_result
    sub_result = Entry(sub_frame, font=('Montserrat', 12))
    sub_result.pack(pady=10)
    # Answer Button
    global sub_btn
    sub_btn = Button(sub_frame, text='Answer ', command=substraction, font=('Montserrat 13 italic'))
    sub_btn.pack(pady=5)
# Create multiplication function
def multiply():
    ''''''
    current_status.set('Multiplication Card App')
    hide_menu_frames()
    mult_clear()
    mult_frame.pack(fill='both', expand=1)
    # Create two random integers
    num_1 = randint(0, 10)
    num_2 = randint(0, 10)
    global mult_res
    mult_res = num_1 * num_2
    # Put numbers into screen
    global mult_flash
    mult_flash = Label(mult_frame, text=str(num_1)+' X '+str(num_2)+' =', font=('Montserrat', 32))
    mult_flash.pack(pady=10)
    # Enter results
    global mult_result
    mult_result = Entry(mult_frame, font=('Montserrat', 12))
    mult_result.pack(pady=10)
    # Answer Button
    global mult_btn
    mult_btn = Button(mult_frame, text='Answer ', command=multiplication, font=('Montserrat 13 italic'))
    mult_btn.pack(pady=5)
# Create division function
def divide():
    ''''''
    current_status.set('Division Card App')
    hide_menu_frames()
    div_clear()
    div_frame.pack(fill='both', expand=1)
    # Create two random integers
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    num_1, num_2 = check_numbers(num_1, num_2)
    global div_res
    div_res = round(num_1 / num_2, 1)
    # Put numbers into screen
    global div_flash
    div_flash = Label(div_frame, text=str(num_1)+' / '+str(num_2)+' =', font=('Montserrat', 32))
    div_flash.pack(pady=10)
    # Enter results
    global div_result
    div_result = Entry(div_frame, font=('Montserrat', 12))
    div_result.pack(pady=10)
    # Answer Button
    global div_btn
    div_btn = Button(div_frame, text='Answer ', command=division, font=('Montserrat 13 italic'))
    div_btn.pack(pady=5)
# Create ratio function
def ratio():
    ''''''
    current_status.set('Ratio Card App')
    hide_menu_frames()
    ratio_clear()
    ratio_frame.pack(fill='both', expand=1)
    # Create two random integers
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    num_1, num_2 = check_numbers(num_1, num_2)
    global ratio_res
    ratio_res = num_1 % num_2
    # Put numbers into screen
    global ratio_flash
    ratio_flash = Label(ratio_frame, text=str(num_1)+' % '+str(num_2)+' =', font=('Montserrat', 32))
    ratio_flash.pack(pady=10)
    # Enter results
    global ratio_result
    ratio_result = Entry(ratio_frame, font=('Montserrat', 12))
    ratio_result.pack(pady=10)
    # Answer Button
    global ratio_btn
    ratio_btn = Button(ratio_frame, text='Answer ', command=ratio_func, font=('Montserrat 13 italic'))
    ratio_btn.pack(pady=5)


# Hide Frame function
def hide_menu_frames():
    add_frame.pack_forget()
    sub_frame.pack_forget()
    mult_frame.pack_forget()
    div_frame.pack_forget()
    ratio_frame.pack_forget()

# Clear frames
def add_clear():
    add_flash.pack_forget()
    add_result.pack_forget()
    add_btn.pack_forget()
    add_label_result.pack_forget()
    add_frame['bg'] = '#457b9d'


def sub_clear():
    sub_flash.pack_forget()
    sub_result.pack_forget()
    sub_btn.pack_forget()
    sub_label_result.pack_forget()
    sub_frame['bg'] = '#495057'

def mult_clear():
    mult_flash.pack_forget()
    mult_result.pack_forget()
    mult_btn.pack_forget()
    mult_label_result.pack_forget()
    mult_frame['bg'] = '#fcbf49'

def div_clear():
    div_flash.pack_forget()
    div_result.pack_forget()
    div_btn.pack_forget()
    div_label_result.pack_forget()
    div_frame['bg'] = '#e5989b'

def ratio_clear():
    ratio_flash.pack_forget()
    ratio_result.pack_forget()
    ratio_btn.pack_forget()
    ratio_label_result.pack_forget()
    ratio_frame['bg'] = '#936639'

# Check num_1 and num_2
def check_numbers(num_1, num_2):
    while num_1 < num_2:
        num_1 = randint(1,10)
        if num_1 >= num_2:
            break
    return num_1, num_2

# Addition funtion
def addition():
    ''''''
    
    global add_label_result
    add_label_result.pack_forget()
    if add_result.get() == str(res):
        result = 'Correct'
        color = '#008000'
        add_frame['bg'] = color
        add_label_result = Label(add_frame, text=result + ' ' + str(res),
             bg=color, font=('Roboto bold', 18),
             width=50 )
    else:
        result = 'Incorrect'
        color = '#ff0000'
        add_frame['bg'] = color
        add_label_result = Label(add_frame, text='"'+add_result.get()+'"' +' is '+ result,
             bg=color, font=('Roboto bold', 18),
             width=50 )

    
    add_label_result.pack(pady=5)

# Substraction funtion
def substraction():
    ''''''
    
    global sub_label_result
    sub_label_result.pack_forget()
    if sub_result.get() == str(sub_res):
        result = 'Correct'
        color = '#008000'
        sub_frame['bg'] = color
        sub_label_result = Label(sub_frame, text=result +' '+ str(sub_res),
                bg=color, font=('Roboto bold', 18),
                width=50 )
    else:
        result = 'Bad Answer'
        color = '#ff0000'
        sub_frame['bg'] = color
        sub_label_result = Label(sub_frame, text=result,bg=color, 
                font=('Roboto bold', 18),
                width=50 )

    
    sub_label_result.pack(pady=5)

# Multiplication funtion
def multiplication():
    ''''''
    
    global mult_label_result
    mult_label_result.pack_forget()
    if mult_result.get() == str(mult_res):
        result = 'Correct'
        color = '#008000'
        mult_frame['bg'] = color
        mult_label_result = Label(mult_frame, text=result +' '+ str(mult_res),
                bg=color, font=('Roboto bold', 18),
                width=50 )
    else:
        result = 'Bad Answer'
        color = '#ff0000'
        mult_frame['bg'] = color
        mult_label_result = Label(mult_frame, text=result,
                bg=color, font=('Roboto bold', 18),
                width=50 )

   
    mult_label_result.pack(pady=5)

# Division funtion
def division():
    ''''''
    
    global div_label_result
    div_label_result.pack_forget()
    if div_result.get() == str(div_res):
        result = 'Correct'
        color = '#008000'
        div_frame['bg'] = color
        div_label_result = Label(div_frame, text=result +' '+ str(div_res),
                bg=color, font=('Roboto bold', 18),
                width=50 )
    else:
        result = 'Bad Answer'
        color = '#ff0000'
        div_frame['bg'] = color
        div_label_result = Label(div_frame, text=result,
                bg=color, font=('Roboto bold', 18),
                width=50)

    div_label_result.pack(pady=5)

# Ratio funtion
def ratio_func():
    ''''''
    
    global ratio_label_result
    ratio_label_result.pack_forget()
    if ratio_result.get() == str(ratio_res):
        result = 'Correct'
        color = '#008000'
        ratio_frame['bg'] = color
        ratio_label_result = Label(ratio_frame, text=result +' '+ str(ratio_res),
                bg=color, font=('Roboto bold', 18),
                width=50)
    else:
        result = 'Bad Answer'
        color = '#ff0000'
        ratio_frame['bg'] = color
        ratio_label_result = Label(ratio_frame, text=result,
                bg=color, font=('Roboto bold', 18),
                width=50)

    ratio_label_result.pack(pady=5)
    
    


root = Tk()
root.geometry('400x400')
root.title('Flashcard App')
# root.iconbitmap('../../img/favicon.ico')

# Define main Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Menu Items
math_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='MathCards', menu=math_menu)
math_menu.add_command(label='Add', command=add)
math_menu.add_command(label='Substract', command=substract)
math_menu.add_command(label='Multiply', command=multiply)
math_menu.add_command(label='Divide', command=divide)
math_menu.add_command(label='Ratio', command=ratio)
math_menu.add_separator()
math_menu.add_command(label='Exit', command=root.quit)

# Create Math Frames
add_frame = Frame(root, width=400, height=400, bg='#457b9d')
sub_frame = Frame(root, width=400, height=400, bg='#495057')
mult_frame = Frame(root, width=400, height=400, bg='#fcbf49')
div_frame = Frame(root, width=400, height=400, bg='#e5989b')
ratio_frame = Frame(root, width=400, height=400, bg='#936639')

# Instantiate labels
add_flash = Label(add_frame)
sub_flash = Label(sub_frame)
mult_flash = Label(mult_frame)
div_flash = Label(div_frame)
ratio_flash = Label(ratio_frame)

add_label_result = Label(add_frame)
sub_label_result = Label(sub_frame)
mult_label_result = Label(mult_frame)
div_label_result = Label(div_frame)
ratio_label_result = Label(ratio_frame)


# Instantiate Entries
add_result = Entry(add_frame)
sub_result = Entry(sub_frame)
mult_result = Entry(mult_frame)
div_result = Entry(div_frame)
ratio_result = Entry(ratio_frame)

# Add Buttons
add_btn = Button(add_frame)
sub_btn = Button(sub_frame)
mult_btn = Button(mult_frame)
div_btn = Button(div_frame)
ratio_btn = Button(ratio_frame)

# Status Bar
current_status = StringVar()
current_status.set('Waiting')
my_status = Label(root, textvariable=current_status, bd=2, relief='sunken',
             width=57, anchor=E)
my_status.pack(side=BOTTOM)



root.mainloop()
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
# from tkinter import PhotoImage

import random
import string

def generate_password(min_length, numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
        
    return pwd 

def main_function():
    min_lenth = entry_int.get()
    numbers = number_checkbutton.get()
    special_characters = special_checkbutton.get()
    pwd = generate_password(min_lenth,numbers,special_characters)
    
    output_string.set(pwd)
    # print("number: ",number_checkbutton.get())
    # print("special: ",special_checkbutton.get())
    

#window
window = ttk.Window(themename = 'cosmo')
window.title("Password Generator")
window.iconphoto(False, ttk.PhotoImage(file="padlock_1.png"))
window.geometry('600x450')

#title
title_label = ttk.Label(master=window, text = "👾Generate Password👾" , font = 'Calibri 21 bold')
title_label.pack()

#input
input_frame1 = ttk.Frame(master=window)
input_frame2 = ttk.Frame(master=window)

entry_label = ttk.Label(master=input_frame1, text = "Enter password length ", font = 'Calibri 15')
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame1,
                  textvariable = entry_int
                  )
button = ttk.Button(master=window,
                    text='Generate',
                    command = main_function,
                    bootstyle="success-outline",
                    padding=(40,16)
                    )
number_checkbutton = tk.BooleanVar(value=True)
checkbutton_num = ttk.Checkbutton(master=input_frame2,
                                  text="numbers",
                                  variable = number_checkbutton,
                                  bootstyle="success-round-toggle"
                                  )
special_checkbutton = tk.BooleanVar(value=True)
checkbutton_special = ttk.Checkbutton(master=input_frame2,
                                  text="special character",
                                  variable = special_checkbutton,
                                  bootstyle="success-round-toggle"
                                  )

entry_label.pack()
entry.pack(pady=20)
checkbutton_num.pack(side='left',padx=6)
checkbutton_special.pack(side='left',padx=6)
input_frame1.pack(pady=20)
input_frame2.pack(pady=10)
button.pack(pady=10)

# output label
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text='Output',
    font = 'Calibri 21', 
    textvariable = output_string,
    wraplength=600
    )
output_label.pack()


# run
window.mainloop()
from tkinter import *
import math

def button_click(number):
    current_text = entry_var.get()
    entry_var.set(current_text + str(number))

def clear_display():
    entry_var.set("")

def calculate_result():
    try:
        expression = entry_var.get()
        result = eval(expression)
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def calculate_square_root():
    try:
        expression = entry_var.get()
        result = math.sqrt(float(expression))
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def calculate_factorial():
    try:
        expression = entry_var.get()
        result = math.factorial(int(expression))
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def add_decimal_point():
    current_text = entry_var.get()
    entry_var.set(current_text + ".")

def backspace():
    current_text = entry_var.get()
    entry_var.set(current_text[:-1])

def create_button(root, text, row, col, command):
    return Button(root, text=text, padx=15, pady=15, font=('Arial', 12), command=command)

root = Tk()
root.title("Calculator")
root.geometry('300x400')
root.minsize(300,75)
root.maxsize(500,600)
entry_var = StringVar()
entry_var.set("")

# Entry widget for displaying input and result
entry = Entry(root, textvariable=entry_var, font=('Arial', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Create and place the buttons in the grid
buttons_data = [
    ('7', 2, 0, lambda: button_click('7')), ('8', 2, 1, lambda: button_click('8')), ('9', 2, 2, lambda: button_click('9')), ('/', 1, 2, lambda: button_click('/')),
    ('4', 3, 0, lambda: button_click('4')), ('5', 3, 1, lambda: button_click('5')), ('6', 3, 2, lambda: button_click('6')), ('*', 2, 3, lambda: button_click('*')),
    ('1', 4, 0, lambda: button_click('1')), ('2', 4, 1, lambda: button_click('2')), ('3', 4, 2, lambda: button_click('3')), ('-', 3, 3, lambda: button_click('-')),
    ('0', 5, 1, lambda: button_click('0')), ('C', 1, 0, clear_display), ('=', 5, 3, calculate_result), ('+', 4, 3, lambda: button_click('+')),
    ('√', 1, 1, calculate_square_root), ('.', 5, 2, add_decimal_point), ('<-', 1, 3, backspace), ('!', 5, 0, calculate_factorial)
]

for data in buttons_data:
    button_text, row_val, col_val, button_command = data
    button = create_button(root, button_text, row_val, col_val, button_command)
    button.grid(row=row_val, column=col_val, padx=2, pady=2)

root.mainloop()

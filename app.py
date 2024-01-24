from tkinter import *

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

def create_button(root, text, row, col, command):
    return Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=command)

root = Tk()
root.title("Calculator")
root.geometry('350x400')
root.minsize(350, 400)
root.maxsize(500, 600)

entry_var = StringVar()
entry_var.set("")

# Entry widget for displaying input and result
entry = Entry(root, textvariable=entry_var, font=('Arial', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Create and place the buttons in the grid
buttons_data = [
    ('7', 1, 0, lambda: button_click('7')), ('8', 1, 1, lambda: button_click('8')), ('9', 1, 2, lambda: button_click('9')), ('/', 1, 3, lambda: button_click('/')),
    ('4', 2, 0, lambda: button_click('4')), ('5', 2, 1, lambda: button_click('5')), ('6', 2, 2, lambda: button_click('6')), ('*', 2, 3, lambda: button_click('*')),
    ('1', 3, 0, lambda: button_click('1')), ('2', 3, 1, lambda: button_click('2')), ('3', 3, 2, lambda: button_click('3')), ('-', 3, 3, lambda: button_click('-')),
    ('0', 4, 0, lambda: button_click('0')), ('C', 4, 1, clear_display), ('=', 4, 2, calculate_result), ('+', 4, 3, lambda: button_click('+'))
]

for data in buttons_data:
    button_text, row_val, col_val, button_command = data
    button = create_button(root, button_text, row_val, col_val, button_command)
    button.grid(row=row_val, column=col_val)

root.mainloop()

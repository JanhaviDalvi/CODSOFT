import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        # Combine uppercase letters, lowercase letters, numbers, and special characters
        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        # Ensure at least one character from each category
        password = random.choice(string.ascii_uppercase) + \
                   random.choice(string.ascii_lowercase) + \
                   random.choice(string.digits) + \
                   random.choice(string.punctuation)
        # Add the remaining characters randomly
        password += ''.join(random.choice(characters) for _ in range(length - len(password)))
        
        # Shuffle the password to make the order random
        password_list = list(password)
        random.shuffle(password_list)
        generated_password = ''.join(password_list)

        password_display.config(state=tk.NORMAL)
        password_display.delete(1.0, tk.END)
        password_display.insert(tk.END, generated_password)
        password_display.config(state=tk.DISABLED)
    except ValueError as e:
        messagebox.showwarning("Error", str(e))

def accept_password():
    username = username_entry.get()
    generated_password = password_display.get(1.0, tk.END).strip()

    if username and generated_password:
        messagebox.showinfo("Accepted", f"Username: {username}\nPassword: {generated_password}")
    else:
        messagebox.showwarning("Warning", "Please generate a password first.")

def reset_fields():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_display.config(state=tk.NORMAL)
    password_display.delete(1.0, tk.END)
    password_display.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry('400x320')
root.resizable(False, False)

# Heading
heading_label = tk.Label(root, text="Password Generator", font=('Helvetica 15 underline'), foreground="blue")
heading_label.grid(row=0, column=0, columnspan=2, pady=10)

# Username input
username_label = tk.Label(root, text="Enter Username:")
username_label.grid(row=1, column=0, sticky="e", pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.grid(row=1, column=1, pady=5, columnspan=2)

# Password length input
length_label = tk.Label(root, text="Enter Password Length:")
length_label.grid(row=2, column=0, sticky="e", pady=5)
length_entry = tk.Entry(root, width=30)
length_entry.grid(row=2, column=1, pady=5, columnspan=2)

# Generated password display
password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=3, column=0, sticky="e", pady=5)
password_display = tk.Text(root, height=1, width=30, state=tk.DISABLED)
password_display.grid(row=3, column=1, pady=5, columnspan=2)

# Generate button
generate_button = tk.Button(root, text="GENERATE PASSWORD", command=generate_password, width=15)
generate_button.grid(row=4, column=0, padx=120, pady=10, columnspan=2, sticky="ew")

# Accept button
accept_button = tk.Button(root, text="ACCEPT", command=accept_password, width=15)
accept_button.grid(row=5, column=0, padx=150, pady=10, columnspan=2, sticky="ew")

# Reset button
reset_button = tk.Button(root, text="RESET", command=reset_fields, width=15)
reset_button.grid(row=6, column=0, padx=150, pady=10, columnspan=2, sticky="ew")

# Center the buttons
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Run the Tkinter event loop
root.mainloop()

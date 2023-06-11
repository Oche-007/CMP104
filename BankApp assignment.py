from tkinter import Tk, Label, Entry, Button, messagebox
import sqlite3

def register():
    username = username_entry.get()
    password = password_entry.get()

    # Perform registration logic here
    # ...

    # Show a message box with the registration result
    messagebox.showinfo("Registration", "Registration successful!")

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Perform login logic here
    # ...

    # Show a message box with the login result
    messagebox.showinfo("Login", "Login successful!")

# Create the main window
window = Tk()
window.title("Bank App")

# Create labels
username_label = Label(window, text="Username:")
password_label = Label(window, text="Password:")

# Create entry fields
username_entry = Entry(window)
password_entry = Entry(window, show="*")

# Create buttons
register_button = Button(window, text="Register", command=register)
login_button = Button(window, text="Login", command=login)

# Position the widgets using grid layout
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)
register_button.grid(row=2, column=0, padx=10, pady=10)
login_button.grid(row=2, column=1, padx=10, pady=10)

# Start the main event loop
window.mainloop()
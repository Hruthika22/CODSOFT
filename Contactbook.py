
import tkinter as tk
from tkinter import messagebox

# Contact book dictionary to store contacts
contacts = {}

def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    if name in contacts:
        messagebox.showerror("Error", "Contact already exists.")
        return
    contacts[name] = {'phone': phone, 'email': email}
    messagebox.showinfo("Success", f"Contact {name} added successfully.")
    clear_fields()
    update_contact_list()

def view_contacts():
    contact_list.delete(0, tk.END)
    for name, info in contacts.items():
        contact_list.insert(tk.END, f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def search_contact():
    name = name_var.get()
    if name in contacts:
        info = contacts[name]
        contact_list.delete(0, tk.END)
        contact_list.insert(tk.END, f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        messagebox.showerror("Error", "Contact not found.")

def update_contact():
    name = name_var.get()
    if name in contacts:
        phone = phone_var.get()
        email = email_var.get()
        contacts[name] = {'phone': phone, 'email': email}
        messagebox.showinfo("Success", f"Contact {name} updated successfully.")
        clear_fields()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Contact not found.")

def delete_contact():
    name = name_var.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"Contact {name} deleted successfully.")
        clear_fields()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Contact not found.")

def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for name in contacts:
        contact_list.insert(tk.END, name)

# Create the main window
root = tk.Tk()
root.title("Contact Book")

# Create StringVar variables to hold form input data
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()

# Create and place labels and entry widgets for contact details
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=phone_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=email_var).grid(row=2, column=1, padx=10, pady=5)

# Create and place buttons for contact operations
tk.Button(root, text="Add Contact", command=add_contact).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Search Contact", command=search_contact).grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=4, column=0, padx=10, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=4, column=1, padx=10, pady=5)

# Create and place a listbox to display contacts
contact_list = tk.Listbox(root, width=50)
contact_list.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Populate the listbox with contacts initially
update_contact_list()

# Run the main event loop
root.mainloop()

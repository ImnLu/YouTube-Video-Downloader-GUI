import tkinter as tk
import customtkinter as ctk


# Function to create the context menu
def create_context_menu(event):
    try:
        context_menu.tk_popup(event.x_root, event.y_root)
    finally:
        context_menu.grab_release()


# Function to copy selected text
def copy():
    textbox.event_generate("<<Copy>>")


# Function to cut selected text
def cut():
    textbox.event_generate("<<Cut>>")


# Function to paste text from clipboard
def paste():
    textbox.event_generate("<<Paste>>")


# Function to select all text
def select_all():
    textbox.event_generate("<<SelectAll>>")


# Main application
app = ctk.CTk()

# Create a CTkTextbox
textbox = ctk.CTkTextbox(app, width=300, height=200)
textbox.pack(padx=20, pady=20)

# Create a context menu
context_menu = tk.Menu(app, tearoff=0)
context_menu.add_command(label="Copy", command=copy)
context_menu.add_command(label="Cut", command=cut)
context_menu.add_command(label="Paste", command=paste)
context_menu.add_command(label="Select All", command=select_all)

# Bind right-click event to the context menu
textbox.bind("<Button-3>", create_context_menu)

# Run the application
app.mainloop()

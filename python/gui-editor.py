# Notepad clone with Tkinter

from tkinter import *
from tkinter import filedialog
from tkinter import font

# ROOT
root = Tk()

# DESIGN
root.geometry("300x300")
root.minsize(height=400, width=600)
root.title("Python Notepad")

# Main frame
frame = Frame(root)
frame.pack(pady=5)

# Text scrollbar
text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Main text widget
text = Text(frame, width=100, height=25, font=("Consolas", 12), selectbackground="yellow",
            selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
text.pack()

text_scroll.config(command=text.yview)

# Main menu
menu = Menu(root)
root.config(menu=menu)

# File Menu
file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Status bar
status_bar = Label(root, text='Ready    ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# EXECUTE
root.mainloop()

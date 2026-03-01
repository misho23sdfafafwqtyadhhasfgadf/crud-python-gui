import tkinter as tk
import crud

def add_item():
    item = entry.get()
    if item:
        crud.create(item)
        refresh_list()

def refresh_list():
    listbox.delete(0, tk.END)
    for i, item in enumerate(crud.read()):
        listbox.insert(tk.END, f"{i}: {item}")

root = tk.Tk()
root.title("CRUD Básico en Python")

entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Agregar", command=add_item)
add_button.pack()

listbox = tk.Listbox(root)
listbox.pack()

refresh_list()
root.mainloop()
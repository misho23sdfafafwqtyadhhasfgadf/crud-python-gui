import tkinter as tk
import crud

def add_item():
    item = entry.get()
    if item:
        crud.create(item)
        entry.delete(0, tk.END)
        refresh_list()

def update_item():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        new_item = entry.get()
        if new_item:
            crud.update(index, new_item)
            entry.delete(0, tk.END)
            refresh_list()

def delete_item():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        crud.delete(index)
        entry.delete(0, tk.END)
        refresh_list()

def select_item(event):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        entry.delete(0, tk.END)
        entry.insert(0, crud.read()[index])

def refresh_list():
    listbox.delete(0, tk.END)
    for i, item in enumerate(crud.read()):
        listbox.insert(tk.END, f"{i}: {item}")

# Configuración ventana
root = tk.Tk()
root.title("CRUD Completo en Python")
root.geometry("300x400")

# Campo de texto
entry = tk.Entry(root)
entry.pack(pady=5)

# Botones
add_button = tk.Button(root, text="Agregar", command=add_item)
add_button.pack(fill="x")

update_button = tk.Button(root, text="Actualizar", command=update_item)
update_button.pack(fill="x")

delete_button = tk.Button(root, text="Eliminar", command=delete_item)
delete_button.pack(fill="x")

# Lista
listbox = tk.Listbox(root)
listbox.pack(fill="both", expand=True, pady=10)

listbox.bind("<<ListboxSelect>>", select_item)

refresh_list()

root.mainloop()
import tkinter as tki
from tkinter import messagebox
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "todos.json"

def load_todos():
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []

def save_todos(todos):
    DATA_FILE.write_text(json.dumps(todos, indent=2), encoding="utf-8")

def refresh_listbox():
    listbox.delete(0, tki.END)
    for t in todos:
        status = "✓" if t["done"] else " "
        listbox.insert(tki.END, f"[{status}] {t['title']}")

def add_task():
    title = entry.get().strip()
    if title == "":
        messagebox.showwarning("Empty Task", "Please enter a task.")
        return
    todos.append({"id": len(todos)+1, "title": title, "done": False})
    save_todos(todos)
    entry.delete(0, tki.END)
    refresh_listbox()

def mark_done():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("No selection", "Select a task First to mark as done.")
        return
    index = selection[0]
    todos[index]["done"] = True
    save_todos(todos)
    refresh_listbox()

def remove_task():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("No selection", "First Select a task to remove.")
        return
    index = selection[0]
    del todos[index]
    save_todos(todos)
    refresh_listbox()


todos = load_todos()


root = tki.Tk()
root.title("To-Do List")

frame = tki.Frame(root)
frame.pack(pady=10)

listbox = tki.Listbox(frame, width=80, height=25)
listbox.pack(side=tki.LEFT, fill=tki.BOTH)

scrollbar = tki.Scrollbar(frame)
scrollbar.pack(side=tki.RIGHT, fill=tki.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tki.Entry(root, width=50)
entry.pack(pady=5)

btn_frame = tki.Frame(root)
btn_frame.pack(pady=5)

add_btn = tki.Button(btn_frame, text="Add Task", command=add_task)
add_btn.pack(side=tki.LEFT, padx=5)

done_btn = tki.Button(btn_frame, text="Mark Done", command=mark_done)
done_btn.pack(side=tki.LEFT, padx=5)

remove_btn = tki.Button(btn_frame, text="Remove Task", command=remove_task)
remove_btn.pack(side=tki.LEFT, padx=5)

refresh_listbox()

root.mainloop()

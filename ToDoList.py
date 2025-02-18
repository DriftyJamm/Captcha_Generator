import tkinter as tk
from tkinter import messagebox
import json

task_file = "tasks.json"

def load_tasks():
    try:
        with open(task_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks():
    with open(task_file, "w") as file:
        json.dump(tasks, file)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        tasks.pop(selected_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

for task in tasks:
    listbox.insert(tk.END, task)

root.mainloop()

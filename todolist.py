import tkinter as tk
from tkinter import messagebox
import json

class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
        self.status = 'Incomplete'

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'priority': self.priority,
            'status': self.status
        }

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []
        self.load_tasks()
        self.create_widgets()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                tasks = json.load(file)
                self.tasks = [Task(**task) for task in tasks]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry_name = tk.Entry(self.root, width=40)
        self.entry_name.pack(pady=5)
        self.entry_name.insert(0, "Task Name")
        
        self.entry_description = tk.Entry(self.root, width=40)
        self.entry_description.pack(pady=5)
        self.entry_description.insert(0, "Description")

        self.entry_priority = tk.Entry(self.root, width=40)
        self.entry_priority.pack(pady=5)
        self.entry_priority.insert(0, "Priority (Low, Medium, High)")

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Complete", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.refresh_listbox()

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = f"{task.name} ({task.priority}) - {task.status}"
            self.task_listbox.insert(tk.END, status)

    def add_task(self):
        name = self.entry_name.get()
        description = self.entry_description.get()
        priority = self.entry_priority.get()
        if name and description and priority:
            task = Task(name, description, priority)
            self.tasks.append(task)
            self.save_tasks()
            self.refresh_listbox()
            self.entry_name.delete(0, tk.END)
            self.entry_description.delete(0, tk.END)
            self.entry_priority.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please fill all fields")

    def complete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            self.tasks[index].status = 'Complete'
            self.save_tasks()
            self.refresh_listbox()
        else:
            messagebox.showwarning("Selection Error", "No task selected")

    def delete_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            del self.tasks[index]
            self.save_tasks()
            self.refresh_listbox()
        else:
            messagebox.showwarning("Selection Error", "No task selected")

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
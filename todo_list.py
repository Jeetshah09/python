import tkinter as tk
from tkinter import messagebox
import time

# Colors
BG_COLOR = "#2c3e50"  # Dark blue-gray
TEXT_COLOR = "#ecf0f1"  # Light gray
BUTTON_COLOR = "#3498db"  # Soft blue
HIGHLIGHT_COLOR = "#1abc9c"  # Teal
COMPLETED_COLOR = "#2ecc71"  # Soft green

# Animated Add Task
def add_task():
    task = task_entry.get().strip()
    if task:
        for i in range(3):  # Small animation effect
            task_listbox.insert(tk.END, "Adding...")
            root.update()
            time.sleep(0.1)
            task_listbox.delete(tk.END)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Animated Remove Task
def remove_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        for _ in range(3):  # Fade effect before deletion
            task_listbox.itemconfig(selected_task[0], {'fg': BG_COLOR})
            root.update()
            time.sleep(0.1)
        task_listbox.delete(selected_task[0])
    else:
        messagebox.showwarning("Warning", "Please select a task to remove!")

# Animated Mark Completed
def mark_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        task = task_listbox.get(selected_task[0])
        task_listbox.delete(selected_task[0])
        for _ in range(3):
            task_listbox.insert(tk.END, "✔ " + task)
            root.update()
            time.sleep(0.1)
            task_listbox.delete(tk.END)
        task_listbox.insert(tk.END, f"✔ {task}")
        task_listbox.itemconfig(tk.END, {'fg': COMPLETED_COLOR})
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("1500x1000")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# Widgets
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40, fg=TEXT_COLOR, bg=BG_COLOR, insertbackground=TEXT_COLOR)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(frame, text="Add", command=add_task, bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=HIGHLIGHT_COLOR)
add_button.pack(side=tk.RIGHT)

task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE, fg=TEXT_COLOR, bg=BG_COLOR, highlightbackground=HIGHLIGHT_COLOR)
task_listbox.pack(pady=10)

button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack()

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task, bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=HIGHLIGHT_COLOR)
remove_button.pack(side=tk.LEFT, padx=10)

complete_button = tk.Button(button_frame, text="Mark Completed", command=mark_completed, bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=HIGHLIGHT_COLOR)
complete_button.pack(side=tk.RIGHT, padx=10)

# Run the app
root.mainloop()

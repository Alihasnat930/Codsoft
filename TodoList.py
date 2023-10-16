import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()
root.title("To-Do List")
def display_message(message, alert_type="warning"):
    message_label = ttk.Label(root, text=message, style=f"{alert_type}.Label")
    message_label.grid(row=0, column=1, columnspan=3, sticky="ew", padx=10, pady=5)
    root.after(3000, lambda: message_label.destroy())  # Remove message after 3 seconds
def add_task():
    task = entry.get()
    if task:
        task_list.insert('', ttk.END, values=(task,))
        entry.delete(0, ttk.END)
    else:
        display_message("Please enter a task", "warning")
def remove_task():
    selected_task_index = task_list.selection()
    if selected_task_index:
        task_list.delete(selected_task_index)
def edit_task():
    selected_task_index = task_list.selection()
    if selected_task_index:
        updated_task = entry.get()
        if updated_task:
            task_list.item(selected_task_index, values=(updated_task,))
            entry.delete(0, ttk.END)
frame = ttk.Frame(root, style="info.")
frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

entry = ttk.Entry(frame, text="Enter tasks", style="Dark.")
entry.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
entry.columnconfigure(0, weight=1)  # Allow the entry widget to expand horizontally

Add_task_button = ttk.Button(frame, text='Add Task', command=add_task, bootstyle="outline", style="success-outline")
Add_task_button.grid(row=0, column=1, padx=5, pady=5)

Remove_task_button = ttk.Button(frame, text='Remove Task', command=remove_task,bootstyle="outline", style="danger-outline")
Remove_task_button.grid(row=0, column=2, padx=5, pady=5)

Edit_task_button = ttk.Button(frame, text='Edit Task', command=edit_task, bootstyle="outline", style="warning-outline")
Edit_task_button.grid(row=0, column=3, padx=5, pady=5)

task_list_label = ttk.Label(root, text="Task List", style="primary")
task_list_label.grid(row=2, column=0, columnspan=4, pady=5)

task_list = ttk.Treeview(root, columns="Tasks", show="headings", selectmode=ttk.BROWSE)
task_list.heading("Tasks", text="Tasks")
task_list.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
task_list.tag_configure("helvetica", font=("Helvetica", 14))

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
root.grid_rowconfigure(3, weight=1)

root.mainloop()

import tkinter as tk



class Task:
    def __init__(self,name,priority="Low",due_date=None, completed=False):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.completed = completed




    def __str__(self):
        return f"{self.name} - Priority: {self.priority} - Due: {self.due_date} - Completed: {self.completed}"


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To Do list")


        self.task = []


        self.task_name_label = tk.Label(root, text="Task Name:")
        self.task_name_label.pack()
        self.task_name_entry = tk.Entry(root)
        self.task_name_entry.pack()

        self.priority_label = tk.Label(root, text="Priority(Low, Medium, High):")
        self.priority_label.pack()
        self.priority_entry = tk.Entry(root)
        self.priority_entry.pack()

        self.due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
        self.due_date_label.pack()
        self.due_date_entry = tk.Entry(root)
        self.due_date_entry.pack()


        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)


        self.task_listbox = tk.Listbox(root, width=70, height=70)
        self.task_listbox.pack(pady=10)

        self.update_task_list()



    def add_task(self):
        task_name = self.task_name_entry.get()
        priority = self.priority_entry.get()
        due_date = self.due_date_entry.get()

        if task_name and priority and due_date:
            new_task = Task(task_name, priority, due_date)
            self.task.append(new_task)
            self.update_task_list()
            self.clear_entries()


    def mark_complete(self):
        selected_task_index = self.task_listbox_curseselection()
        if selected_task_index:
            task = self.task[selected_task_index[0]]
            task.completed = True
            self.update_task_list()


    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.task[selected_task_index[0]]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0,tk.END)
        for task in self.task:
            task_display = task.name
            if task.completed:
                task_display += "(Completed)"
            task_display +=f"-Priority:{task.priority} -Due:{task.due_date}"
            self.task_listbox.insert(tk.END, task_display)

    def clear_entries(self):
        self.task_name_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)


root=tk.Tk()
app = ToDoApp(root)
root.mainloop()






import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import datetime
import openpyxl

class TaskEntry:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Entry")
        self.date_var = tk.StringVar(value=datetime.date.today().strftime("%d-%m-%y"))
        self.create_widgets()
        self.filename = "task_entries.xlsx"
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.sheet.append(["Date", "Task", "Company", "Self"])

    def create_widgets(self):
        ttk.Label(self.master, text="Date:").grid(column=0, row=0, padx=5, pady=5)
        Calendar(self.master, selectmode="day", year=datetime.date.today().year, month=datetime.date.today().month, day=datetime.date.today().day, date_pattern="dd-mm-yy", textvariable=self.date_var).grid(column=1, row=0, padx=5, pady=5)
        ttk.Label(self.master, text="Task:").grid(column=0, row=1, padx=5, pady=5)
        self.task_entry = ttk.Entry(self.master, width=20)
        self.task_entry.grid(column=1, row=1, padx=5, pady=5)
        ttk.Label(self.master, text="Company:").grid(column=0, row=2, padx=5, pady=5)
        self.company_entry = ttk.Entry(self.master, width=20)
        self.company_entry.grid(column=1, row=2, padx=5, pady=5)
        ttk.Label(self.master, text="Self:").grid(column=0, row=3, padx=5, pady=5)
        self.self_entry = ttk.Entry(self.master, width=20)
        self.self_entry.grid(column=1, row=3, padx=5, pady=5)
        ttk.Button(self.master, text="Submit", command=self.get_input).grid(column=0, row=4, padx=5, pady=5)

    def get_input(self):
        values = [self.date_var.get(), self.task_entry.get(), self.company_entry.get(), self.self_entry.get()]
        self.sheet.append(values)
        self.workbook.save(self.filename)

def main():
    root = tk.Tk()
    TaskEntry(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    

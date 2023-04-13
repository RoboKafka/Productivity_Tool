# Task_comp_Persona
A measure of productivity in this world of chaos

This is a Python code for a simple GUI program that allows the user to enter task information and save it to an Excel spreadsheet using the openpyxl library. Here's a detailed breakdown of the code:

First, the required modules are imported:

python

    import tkinter as tk
    from tkinter import ttk
    from tkcalendar import Calendar
    import datetime
    import openpyxl

tkinter is the standard Python interface for creating graphical user interfaces (GUIs).
ttk is an extension module for tkinter that provides themed widgets.
tkcalendar is a widget library that provides a date picker widget.
datetime is a module that supplies classes for working with dates and times.
openpyxl is a library for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.

Next, a class TaskEntry is defined:

python

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

The __init__ method is called when a new instance of the class is created. It initializes various attributes such as the master window (the root window for the GUI), the date_var variable (a tkinter variable to store the selected date), and the filename for the Excel file.
The create_widgets method creates the various GUI widgets using ttk and tkcalendar widgets.
An Excel workbook is created using the openpyxl library and a new worksheet is added to it. The first row of the worksheet contains column headings.

The create_widgets method is defined as follows:

python

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

Several labels, entry boxes, and a button are created using ttk widgets and grid layout.

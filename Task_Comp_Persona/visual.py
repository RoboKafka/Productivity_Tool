import openpyxl
import matplotlib.pyplot as plt
import math

class TaskVisualizer:
    def __init__(self, filename):
        self.workbook = openpyxl.load_workbook(filename=filename)
        self.sheet = self.workbook.active

        # Get the number of rows in the sheet
        self.num_rows = self.sheet.max_row - 1

        # Create the figure and axes
        self.fig = plt.figure(figsize=(5, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim([-0.5, 1.5])
        self.ax.set_ylim([-0.5, 1.5])

        # Add the circles to the axes
        self.task_circle = plt.Circle((0, 0), 0, color="red")
        self.company_circle = plt.Circle((0, 0), 0, color="green")
        self.self_circle = plt.Circle((0, 0), 0, color="blue")
        self.ax.add_artist(self.task_circle)
        self.ax.add_artist(self.company_circle)
        self.ax.add_artist(self.self_circle)

    def set_circle_sizes(self, task_size, company_size, self_size):
        self.task_circle.set_radius(task_size)
        self.company_circle.set_radius(company_size)
        self.self_circle.set_radius(self_size)

    def set_circle_positions(self, task_pos, company_pos, self_pos):
        self.task_circle.center = task_pos
        self.company_circle.center = company_pos
        self.self_circle.center = self_pos

    def add_labels(self, task_label, company_label, self_label):
        self.ax.annotate(task_label, self.task_circle.center, ha="center", va="center")
        self.ax.annotate(company_label, self.company_circle.center, ha="center", va="center")
        self.ax.annotate(self_label, self.self_circle.center, ha="center", va="center")

        # Show the figure
        plt.show()

# Example usage:
filename = "task_entries.xlsx"
visualizer = TaskVisualizer(filename)
task_size = 0.1 + (visualizer.num_rows * 0.03)
company_size = 0.1 + (visualizer.num_rows * 0.03)
self_size = 0.1 + (visualizer.num_rows * 0.03)
task_pos = (0.5, math.sqrt(3)/2)
company_pos = (1, 0)
self_pos = (0, 0)
visualizer.set_circle_sizes(task_size, company_size, self_size)
visualizer.set_circle_positions(task_pos, company_pos, self_pos)
visualizer.add_labels("Task", "Company", "Self")

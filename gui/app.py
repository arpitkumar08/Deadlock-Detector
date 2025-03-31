import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from core.deadlock_detector import DeadlockDetector
from core.logger import DeadlockLogger
from core.resolve import resolve_deadlock

class DeadlockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Detection Tool")

        self.detector = DeadlockDetector()
        self.logger = DeadlockLogger()
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg="#1E1E1E")

        # Header
        header_label = tk.Label(root, text="Automated Deadlock Detection Tool", font=("Helvetica", 32, "bold"), fg="#00BFFF", bg="#1E1E1E")
        header_label.pack(pady=40)

        # Input Frame
        input_frame = tk.Frame(root, bg="#1E1E1E")
        input_frame.pack(pady=20)

        tk.Label(input_frame, text="Process 1:", fg="#FFFFFF", bg="#1E1E1E", font=("Helvetica", 16)).grid(row=0, column=0, padx=20, pady=10)
        tk.Label(input_frame, text="Process 2:", fg="#FFFFFF", bg="#1E1E1E", font=("Helvetica", 16)).grid(row=1, column=0, padx=20, pady=10)

        self.p1_entry = tk.Entry(input_frame, width=20, font=("Helvetica", 14))
        self.p1_entry.grid(row=0, column=1, padx=20)
        self.p2_entry = tk.Entry(input_frame, width=20, font=("Helvetica", 14))
        self.p2_entry.grid(row=1, column=1, padx=20)

        # Buttons Frame
        button_frame = tk.Frame(root, bg="#1E1E1E")
        button_frame.pack(pady=20)

        button_style = {"font": ("Helvetica", 16), "bg": "#007ACC", "fg": "#FFFFFF", "activebackground": "#005F99", "width": 20, "height": 2, "bd": 0, "relief": "flat"}

        self.add_button = tk.Button(button_frame, text="Add Dependency", command=self.add_dependency, **button_style)
        self.add_button.grid(row=0, column=0, padx=20, pady=10)

        self.detect_button = tk.Button(button_frame, text="Detect Deadlock", command=self.detect_deadlock, **button_style)
        self.detect_button.grid(row=0, column=1, padx=20, pady=10)

        self.resolve_button = tk.Button(button_frame, text="Resolve Deadlock", command=self.resolve_deadlock, **button_style)
        self.resolve_button.grid(row=1, column=0, padx=20, pady=10)

        self.show_graph_button = tk.Button(button_frame, text="Show Graph", command=self.show_graph, **button_style)
        self.show_graph_button.grid(row=1, column=1, padx=20, pady=10)

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", command=self.root.destroy, font=("Helvetica", 16), bg="#E74C3C", fg="#FFFFFF", width=20, height=2, bd=0, relief="flat")
        self.exit_button.pack(pady=40)

    def add_dependency(self):
        p1 = self.p1_entry.get()
        p2 = self.p2_entry.get()
        if p1 and p2:
            self.detector.add_dependency(p1, p2)
            messagebox.showinfo("Success", f"Dependency added: {p1} → {p2}")
        else:
            messagebox.showwarning("Error", "Enter valid process names!")

    def detect_deadlock(self):
        cycle = self.detector.detect_deadlock()
        if cycle:
            self.logger.log_deadlock(cycle)
            formatted_cycle = ' → '.join([f"{a} to {b}" for a, b, _ in cycle])
            messagebox.showerror("Deadlock Detected", f"Deadlock detected in the following cycle: {formatted_cycle}")
        else:
            messagebox.showinfo("No Deadlock", "No cycles detected!")

    def resolve_deadlock(self):
        result = resolve_deadlock(self.detector.graph)
        messagebox.showinfo("Deadlock Resolution", result)

    def show_graph(self):
        plt.figure(figsize=(8, 8))
        nx.draw(self.detector.graph, with_labels=True, node_color='lightblue', edge_color='black')
        plt.show()

root = tk.Tk()
app = DeadlockGUI(root)
root.mainloop()

from gui.app import DeadlockGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = DeadlockGUI(root)
    root.mainloop()
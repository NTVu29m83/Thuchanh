import tkinter as tk
from tkinter import ttk
from sympy import *
from sympy.parsing.mathematica import parse_mathematica

def calculate():
    try:
        expression = parse_mathematica(entry.get())
        result = str(simplify(expression))  # Simplify and convert to string
        result_label.config(text=f"Kết quả: {result}")
    except Exception as e:
        result_label.config(text=f"Lỗi: {e}")

# Create the main window
root = tk.Tk()
root.title("Máy tính Giải tích")

# Create input label
input_label = tk.Label(root, text="Nhập biểu thức:")
input_label.pack()

# Create input field
entry = tk.Entry(root)
entry.pack()

# Create Calculate button
calculate_button = tk.Button(root, text="Tính toán", command=calculate)
calculate_button.pack()

# Create result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the main event loop
root.mainloop()
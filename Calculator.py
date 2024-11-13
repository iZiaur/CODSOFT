import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid Operation")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=5)
operation_var = tk.StringVar(root)
operation_var.set('+')
operation_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operation_menu.grid(row=2, column=1, padx=10, pady=5)

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=2, pady=5)

root.mainloop()

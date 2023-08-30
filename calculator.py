import tkinter as tk

def append_value(value):
    current_text = entry_result.get()
    entry_result.delete(0, tk.END)
    entry_result.insert(0, current_text + value)

def clear():
    entry_result.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry_result.get())
        entry_result.delete(0, tk.END)
        entry_result.insert(0, result)
    except:
        entry_result.delete(0, tk.END)
        entry_result.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x600")
root.config(bg="#333")

entry_result = tk.Entry(root, font=("Arial", 32), justify="right")
entry_result.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root, bg="#333")
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

for btn_text in buttons:
    if btn_text == '=':
        tk.Button(button_frame, text=btn_text, font=("Arial", 18, "bold"), command=calculate, bg="#f39c12", fg="white").grid(row=buttons.index(btn_text) // 4, column=buttons.index(btn_text) % 4, padx=5, pady=5, sticky="nsew")
    else:
        tk.Button(button_frame, text=btn_text, font=("Arial", 18, "bold"), command=lambda value=btn_text: append_value(value), bg="#34495e", fg="white").grid(row=buttons.index(btn_text) // 4, column=buttons.index(btn_text) % 4, padx=5, pady=5, sticky="nsew")

clear_button = tk.Button(button_frame, text="C", font=("Arial", 18, "bold"), command=clear, bg="#e74c3c", fg="white")
clear_button.grid(row=4, column=0, padx=5, pady=5, columnspan=2, sticky="nsew")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(3, weight=1)

root.mainloop()

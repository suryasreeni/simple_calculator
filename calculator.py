from tkinter import *
from tkinter import ttk  # Import ttk for themed widgets

root = Tk()
root.title("Calculator")

# Style configuration
style = ttk.Style()
style.configure("TButton", padding=(10, 10), font=('Helvetica', 14))

# Entry widget
display = Entry(root, font=('Helvetica', 16), justify='right')
display.grid(row=1, columnspan=6, sticky=W+E)

i = 0

def get_variable(num):
    global i
    display.insert(i, num)
    i += 1

def clear_all():
    display.delete(0, END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "error")

def get_operation(opr):
    global i
    length = len(opr)
    display.insert(i, opr)
    i += length

def calculate():
    entire_string = display.get()
    try:
        result = eval(entire_string)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "error")

# Buttons with styling
Button(root, text="1", command=lambda: get_variable(1)).grid(row=2, column=0, sticky=NSEW)
Button(root, text="2", command=lambda: get_variable(2)).grid(row=2, column=1, sticky=NSEW)
Button(root, text="3", command=lambda: get_variable(3)).grid(row=2, column=2, sticky=NSEW)
Button(root, text="4", command=lambda: get_variable(4)).grid(row=3, column=0, sticky=NSEW)
Button(root, text="5", command=lambda: get_variable(5)).grid(row=3, column=1, sticky=NSEW)
Button(root, text="6", command=lambda: get_variable(6)).grid(row=3, column=2, sticky=NSEW)
Button(root, text="7", command=lambda: get_variable(7)).grid(row=4, column=0, sticky=NSEW)
Button(root, text="8", command=lambda: get_variable(8)).grid(row=4, column=1, sticky=NSEW)
Button(root, text="9", command=lambda: get_variable(9)).grid(row=4, column=2, sticky=NSEW)
Button(root, text="0", command=lambda: get_variable(0)).grid(row=5, column=0, sticky=NSEW)
Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=1, sticky=NSEW)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2, sticky=NSEW)
Button(root, text="+", command=lambda: get_operation('+')).grid(row=2, column=3, sticky=NSEW)
Button(root, text="-", command=lambda: get_operation('-')).grid(row=3, column=3, sticky=NSEW)
Button(root, text="x", command=lambda: get_operation('*')).grid(row=4, column=3, sticky=NSEW)
Button(root, text="/", command=lambda: get_operation('/')).grid(row=5, column=3, sticky=NSEW)
Button(root, text="%", command=lambda: get_operation('%')).grid(row=2, column=4, sticky=NSEW)
Button(root, text="pi", command=lambda: get_operation('*3.14')).grid(row=3, column=4, sticky=NSEW)
# ... (similar styling for other buttons)

# Configure row and column weights for resizing
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

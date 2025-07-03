from tkinter import *
from tkinter import ttk


# Root 
root = Tk()
root.title("File Organizer Project")
root.geometry("500x350")

# Configure grid expansion
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Creating a main frame that will fill up the window
main_frame = ttk.Frame(root, padding=10)
main_frame.grid(row=0, column=0, sticky="nsew")

# Configuring main_frame's columns to align widgets
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)

# --- Top Text ---
label = ttk.Label(main_frame, text="Hello, welcome to File Organizer!", foreground="blue")
label.grid(row=0, column=0, columnspan=3, pady=(10, 5), sticky="n")

paragraph = """This is just a small file organizer app to quickly sort your files into their respective data type folders. Made by rehtoe and cole831 on github. Please enter the target dictectory that you want to be sorted, then enter the dictory where these sorted files will be deposited. Thank you."""

text_widget = ttk.Label(main_frame, text=paragraph, wraplength=470, justify="left")
text_widget.grid(row=1, column=0, columnspan=3, sticky="n", pady=(0, 10))

# --- Middle Section:  Directory Input & Organize Button---
ttk.Label(main_frame, text="Target Directory:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
target_entry = ttk.Entry(main_frame, width=40).grid(row=3, column=0, columnspan=2, sticky="w", padx=10)

ttk.Label(main_frame, text="Deposit Location:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
deposit_entry = ttk.Entry(main_frame, width=40).grid(row=5, column=0, columnspan=2, sticky="w", padx=10)

ttk.Button(main_frame, text="Organize Files", width=25).grid(row=5, column=2, columnspan=2, sticky="e", padx=10)



# --- Bottom Buttons ---
main_frame.grid_rowconfigure(6, weight=1)  # pushes buttons to bottom
bottom_frame = ttk.Frame(main_frame)
bottom_frame.grid(row=7, column=2, sticky="e", pady=10, padx=10)

ttk.Button(bottom_frame, text="Configure").grid(row=0, column=0)
ttk.Button(bottom_frame, text="Quit", command=root.quit).grid(row=0, column=1)

root.mainloop()

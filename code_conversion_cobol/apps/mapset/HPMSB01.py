import tkinter as tk

def create_label(master, pos, text, **kwargs):
    label = tk.Label(master, text=text, **kwargs)
    label.grid(row=pos[0], column=pos[1], padx=5, pady=5)

def create_entry(master, pos, **kwargs):
    entry = tk.Entry(master, **kwargs)
    entry.grid(row=pos[0], column=pos[1], padx=5, pady=5)

def create_ui():
    root = tk.Tk()
    root.title("HPMS Main Menu")

    # Define the fields
    fields = [
        {"pos": (1, 1), "text": "ORACLE RESEARCH AND DEVELOPMENT", "color": "red"},
        {"pos": (1, 72), "text": "PNAME", "color": "blue"},
        {"pos": (2, 1), "text": "PROCESS MANAGEMENT SYSTEM", "color": "red"},
        {"pos": (3, 1), "text": "MAIN MENU", "color": "red"},
        {"pos": (5, 32), "text": "ACTION"},
        {"pos": (8, 27), "text": "DESC1", "width": 50}
        # Add more fields here as needed
    ]

    # Create labels and entries based on the field definitions
    for field in fields:
        color = field.get("color", "black")
        create_label(root, field["pos"], field["text"], fg=color)
        if "width" in field:
            create_entry(root, field["pos"], width=field["width"])

    root.mainloop()

create_ui()

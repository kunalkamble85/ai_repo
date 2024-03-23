import tkinter as tk

def create_label(master, pos, text, **kwargs):
    label = tk.Label(master, text=text, **kwargs)
    label.grid(row=pos[0], column=pos[1], padx=5, pady=5, sticky="w")

def create_entry(master, pos, **kwargs):
    entry = tk.Entry(master, **kwargs)
    entry.grid(row=pos[0], column=pos[1], padx=5, pady=5, sticky="w")

def create_ui():
    root = tk.Tk()
    root.title("TLOG - Experiment & Testing Log")

    # Define the fields
    fields = [
        {"pos": (3, 1), "text": "RECORD ID"},
        {"pos": (4, 1), "text": "CATEGORY"},
        {"pos": (4, 44), "text": "GROUP"},
        {"pos": (5, 1), "text": "AUTHOR"},
        {"pos": (5, 44), "text": "EMAIL"},
        {"pos": (6, 1), "text": "YEAR"},
        {"pos": (6, 18), "text": "MONTH"},
        {"pos": (6, 28), "text": "DAY"},
        {"pos": (7, 1), "text": "SUBJECT"},
        {"pos": (8, 1), "text": "----------------------------------------------"},
        {"pos": (9, 1), "text": "NOTE1"},
        {"pos": (10, 1), "text": "NOTE2"},
        {"pos": (11, 1), "text": "NOTE3"},
        {"pos": (12, 1), "text": "NOTE4"},
        {"pos": (13, 1), "text": "NOTE5"},
        {"pos": (14, 1), "text": "NOTE6"},
        {"pos": (15, 1), "text": "NOTE7"},
        {"pos": (16, 1), "text": "NOTE8"},
        {"pos": (17, 1), "text": "NOTE9"},
        {"pos": (18, 1), "text": "NOTE10"},
        {"pos": (19, 1), "text": "NOTE11"},
        {"pos": (20, 1), "text": "NOTE12"},
        {"pos": (21, 1), "text": "NOTE13"},
        {"pos": (22, 1), "text": "NOTE14"},
        {"pos": (23, 1), "text": "MSG"},
        {"pos": (24, 1), "text": "COMMAND"},
    ]

    # Create labels and entries based on the field definitions
    for field in fields:
        create_label(root, field["pos"], field["text"])

    # Create entry fields for interactive input
    create_entry(root, (3, 12), width=6)
    create_entry(root, (4, 12), width=28)
    create_entry(root, (4, 50), width=28)
    create_entry(root, (5, 12), width=28)
    create_entry(root, (5, 50), width=28)
    create_entry(root, (6, 12), width=4)
    create_entry(root, (6, 24), width=2)
    create_entry(root, (6, 32), width=2)
    create_entry(root, (7, 12), width=66)

    # Create entry fields for notes
    for i in range(1, 15):
        create_entry(root, (8 + i, 1), width=77)

    # Create message and command fields
    create_entry(root, (23, 1), width=79)
    create_entry(root, (24, 1), width=79)

    root.mainloop()

create_ui()

import tkinter as tk

# Define the menu options
menu_options = [
    {"number": "1", "label": "TEST LOG", "description": "TEST AND EXPERIMENT LOG"},
    {"number": "2", "label": "PROPELLANT INV", "description": "PROPELLANT GRAIN INVENTORY"},
    {"number": "3", "label": "INCIDENT", "description": "INCIDENT REPORTING"},
    {"number": "4", "label": "INVENTORY", "description": "INVENTORY MANAGEMENT"},
    {"number": "5", "label": "PROJECTS", "description": "PROJECT MANAGEMENT"},
    {"number": "6", "label": "ACCOUNTING", "description": "ACCOUNTING & GENERAL LEDGER"},
    {"number": "7", "label": "CRM", "description": "CUSTOMER DATABASE"},
    {"number": "8", "label": "CMMS", "description": "WORK ORDERS"},
    {"number": "9", "label": "NOTES", "description": "MISC NOTES"}
]

# Function to handle menu option selection
def handle_option(option):
    print(f"Selected option {option['number']}: {option['label']} - {option['description']}")

# Create main Tkinter window
root = tk.Tk()
root.title("Main Menu")

# Create and display menu options
for option_data in menu_options:
    option_frame = tk.Frame(root)
    option_frame.pack(fill="x", padx=10, pady=5)
    
    label = tk.Label(option_frame, text=f"{option_data['number']}  {option_data['label']}")
    label.pack(side="left")
    
    description = tk.Label(option_frame, text=option_data['description'])
    description.pack(side="left", padx=(10, 0))
    
    # Bind click event to handle_option function
    option_frame.bind("<Button-1>", lambda event, data=option_data: handle_option(data))

# Add command label
command_label = tk.Label(root, text="PF KEYS: PF12=EXIT APPLICATION")
command_label.pack(pady=10)

# Run Tkinter event loop
root.mainloop()

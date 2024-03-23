import tkinter as tk

# Function to handle menu option selection
def handle_option(option):
    if option == '1':
        print("Selected option 1: Add Project - Add New Project")
    elif option == '2':
        print("Selected option 2: Project Inquiry - Project Inquiry/Update by Project ID")
    else:
        print("Invalid option")

# Create main Tkinter window
root = tk.Tk()
root.title("Project Management Main Menu")

# Define menu options
menu_options = [
    {"number": "1", "label": "ADD PROJECT", "description": "ADD NEW PROJECT"},
    {"number": "2", "label": "PROJECT INQUIRY", "description": "PROJECT INQUIRY/UPDATE BY PROJECT ID"}
]

# Create and display menu options
for option_data in menu_options:
    option_frame = tk.Frame(root)
    option_frame.pack(fill="x", padx=10, pady=5)
    
    label = tk.Label(option_frame, text=f"{option_data['number']}  {option_data['label']}")
    label.pack(side="left")
    
    description = tk.Label(option_frame, text=option_data['description'])
    description.pack(side="left", padx=(10, 0))
    
    # Bind click event to handle_option function
    option_frame.bind("<Button-1>", lambda event, num=option_data['number']: handle_option(num))

# Add command label
command_label = tk.Label(root, text="PF KEYS: PF3=MAIN MENU PF12=EXIT APPLICATION")
command_label.pack(pady=10)

# Run Tkinter event loop
root.mainloop()

import tkinter as tk

class NoteApplication:
    def __init__(self, master):
        self.master = master
        master.title("Add Note Record")

        self.lbl_title = tk.Label(master, text="MISCELLANEOUS NOTES")
        self.lbl_title.grid(row=0, column=0, columnspan=2)

        self.lbl_author = tk.Label(master, text="Author:")
        self.lbl_author.grid(row=1, column=0, sticky="w")
        self.entry_author = tk.Entry(master)
        self.entry_author.grid(row=1, column=1)

        self.lbl_email = tk.Label(master, text="Email:")
        self.lbl_email.grid(row=2, column=0, sticky="w")
        self.entry_email = tk.Entry(master)
        self.entry_email.grid(row=2, column=1)

        self.lbl_subject = tk.Label(master, text="Subject:")
        self.lbl_subject.grid(row=3, column=0, sticky="w")
        self.entry_subject = tk.Entry(master)
        self.entry_subject.grid(row=3, column=1)

        self.lbl_notes = tk.Label(master, text="Notes:")
        self.lbl_notes.grid(row=4, column=0, sticky="w")
        self.text_notes = tk.Text(master, width=40, height=10)
        self.text_notes.grid(row=4, column=1)

        self.btn_add = tk.Button(master, text="Add Record", command=self.add_record)
        self.btn_add.grid(row=5, column=0, columnspan=2)

        self.lbl_message = tk.Label(master, text="")
        self.lbl_message.grid(row=6, column=0, columnspan=2)

    def add_record(self):
        author = self.entry_author.get()
        email = self.entry_email.get()
        subject = self.entry_subject.get()
        notes = self.text_notes.get("1.0", tk.END)

        if author and email and subject and notes:
            # Logic to save the note record
            print("Note record added successfully.")
            self.lbl_message.config(text="Note record added successfully.")
            self.clear_fields()
        else:
            self.lbl_message.config(text="Please fill in all fields.")

    def clear_fields(self):
        self.entry_author.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_subject.delete(0, tk.END)
        self.text_notes.delete("1.0", tk.END)

def main():
    root = tk.Tk()
    app = NoteApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk
from tkinter import *
import os


window = tk.Tk()
window.title("Final Verification Folder Creator")
frame = tk.Frame(master=window, width=1250, height=750)
search_item = StringVar()
batch = StringVar()
first_letter = StringVar()
last_letter = StringVar()

frame.pack()
location = os.path.join("C:\\Users", os.getenv('username'),
                        "Deltex Medical\Shared No Security - Documents\Manufacturing\Daily probe log", "")
# C:\Users\BrianFleming\Deltex Medical\Shared No Security - Documents\Manufacturing\Daily probe log


canvas_back = Canvas(bg='#FAEAB1', width=1220, height=750)
canvas_back.place(x=5, y=5)


def generate():
    pass


def display():
    tk.Label(canvas_back, text='Final Verification Folder Creation Tool', background='#FAEAB1', font=("Courier", 20, "bold")).place(
        relx=0.2, rely=0.1, anchor='w')
    names = ["Choose", "DP240", "DP12", "DP6", "I2C", "I2P", "I2S", "KDP72"]
    tk.Label(canvas_back, text="Deltex", background="#FAEAB1", foreground="#003865",
             font=('Helvetica', 28, 'bold'), width=12).place(relx=0.78, rely=0.05)
    tk.Label(canvas_back, text="medical", background="#FAEAB1", foreground="#A2B5BB",
             font=('Helvetica', 18)).place(relx=0.85, rely=0.11)
    canvas_entry = Canvas(bg="#C58940", width=1150, height=400)
    canvas_entry.place(x=30, y=300)
    tk.Label(canvas_back, text="To create a series of folders for the final verification results to be recorded in\n"
                               "this tool will create these folders in the correct place.\n"
                               f"\n[ {location} ]", background="#FAEAB1", font=("Courier", 14)).place(relx=0.05, rely=0.2)
    tk.Label(canvas_entry, text="Probe Type: ", background="#C58940", font=("Courier", 16)).place(relx=0.1, rely=0.2)
    someStyle = ttk.Style()
    someStyle.configure('my.TMenubutton', font=('Futura', 16))
    search_name = ttk.OptionMenu(canvas_entry, search_item, *names, style='my.TMenubutton')
    search_name['menu'].configure(font=('Futura', 16))
    search_name.place(relx=0.3, rely=0.2)
    search_item.set("Choose")
    tk.Label(canvas_entry, text="Select probe type from list ", background="#C58940",
             font=("Courier", 16)).place(relx=0.6, rely=0.2)
    tk.Label(canvas_entry, text="Batch Number without any letters: ", background="#C58940",
             font=("Courier", 16)).place(relx=0.1, rely=0.4)
    tk.Entry(canvas_entry, textvariable=batch, font=("Courier", 18), relief=SUNKEN, width=10).place(relx=0.5, rely=0.4)
    tk.Label(canvas_entry, text="Batch Number letters (first) ", background="#C58940",
             font=("Courier", 16)).place(relx=0.1, rely=0.55)
    tk.Entry(canvas_entry, textvariable=first_letter, font=("Courier", 18),
             relief=SUNKEN, width=4).place(relx=0.5, rely=0.55)
    tk.Label(canvas_entry, text="(last) ", background="#C58940",
             font=("Courier", 16)).place(relx=0.6, rely=0.55)
    tk.Entry(canvas_entry, textvariable=last_letter, font=("Courier", 18), relief=SUNKEN, width=4).place(relx=0.7, rely=0.55)
    tk.Button(canvas_entry, text="Generate Folders ", background="#2C74B3",
              font=("Courier", 18), command=generate).place(relx=0.7, rely=0.8)


display()


def search_data_path(self):
    name = "Deltex Medical"
    file = "Shared No Security - Documents"
    location = "Manufacturing"
    endpoint = "Daily probe log"
    for root, dirs, files in os.walk(self.base_path):
        self.increase_total(0.01)
        if name in root:
            if file in root:
                if location in root:
                    if endpoint in root:
                        return root



window.mainloop()

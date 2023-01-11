import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import *
import os
import json


try:
    import pyi_splash

    pyi_splash.update_text('UI Loaded ...')
    pyi_splash.close()
except:
    pass


window = tk.Tk()
window.title("Final Verification Folder Creator")
frame = tk.Frame(master=window, width=1250, height=750)
frame.pack()

search_item = StringVar()
batch = StringVar()
first_letter = StringVar()
last_letter = StringVar()


base_path = os.path.join("C:\\Users", os.getenv('username'), "Deltex Medical", "")

file_data = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
test_location = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Deltex Medical\Shared No Security - Documents\Brian Fleming\Training Database')
data_path = StringVar()


canvas_back = Canvas(bg='#FAEAB1', width=1220, height=750)
canvas_back.place(x=5, y=5)
warning_name = canvas_back.create_text(550, 260, text=" ", fill="black", font=("Arial", 20, "bold"))


def generate():
    exist = False
    if not batch.get() or not first_letter.get() or not last_letter.get():
        canvas_back.itemconfig(warning_name, text="Please complete the form.")
        Tk.update(canvas_back)
        canvas_back.after(2000, canvas_back.itemconfig(warning_name, text=" "))
        Tk.update(canvas_back)
        display()
    else:
        batch_name = batch.get()
        first = first_letter.get().upper()
        last = last_letter.get().upper()
        if not batch_name[-1].isdigit():
            canvas_back.itemconfig(warning_name, text="Please remove the last letter")
            Tk.update(canvas_back)
            canvas_back.after(2000, canvas_back.itemconfig(warning_name, text=" "))
            Tk.update(canvas_back)
        else:
            batch_title = batch_name + " " + search_item.get()
            mainPath = os.path.join(data_path.get(), f"{batch_title}", "")
            letters = [chr(item) for item in range(ord(first), ord(last) + 1)]
            if not os.path.exists(mainPath):
                os.makedirs(mainPath, 0o777)
                for letter in letters:
                    inside_titles = os.path.join(mainPath, f"{batch_name}{letter} {search_item.get()}")
                    if not os.path.exists(inside_titles):
                        os.makedirs(inside_titles, 0o777)
                filedialog.askdirectory(initialdir=data_path.get(), title="Select file")
            else:
                for letter in letters:
                    inside_titles = os.path.join(mainPath, f"{batch_name}{letter} {search_item.get()}")
                    if not os.path.exists(inside_titles):
                        os.makedirs(inside_titles, 0o777)
                else:
                    exist = True
        if exist:
            canvas_back.itemconfig(warning_name, text="Some folders already exist, updating..")
            Tk.update(canvas_back)
            canvas_back.after(3000, canvas_back.itemconfig(warning_name, text=" "))
            Tk.update(canvas_back)
            filedialog.askdirectory(initialdir=data_path.get(), title="Select file")


def search_data_path():
    name = "Deltex Medical"
    file = "Shared No Security - Documents"
    location1 = "Manufacturing"
    endpoint = "Daily probe log"
    for root, dirs, files in os.walk(base_path):
        if name in root:
            if file in root:
                if location1 in root:
                    if endpoint in root:
                        return root


def write_data_file_locations():
    raw_path = os.path.join(file_data, "FolderLocation.json")
    data_file = search_data_path()
    file_obj = {
        "location2": data_file
    }
    data_path.set(data_file)
    with open(raw_path, 'w') as user_file:
        json.dump(file_obj, user_file, indent=4)


def display():
    raw_path = os.path.join(file_data, "FolderLocation.json")
    flag = os.path.exists(raw_path)
    if flag:
        with open(raw_path, 'r') as load_user_file:
            load_data = json.load(load_user_file)
        data_path.set(load_data['location2'])
    else:
        write_data_file_locations()

    tk.Label(canvas_back, text='Final Verification Folder Creation Tool', background='#FAEAB1', font=("Courier", 20, "bold")).place(
        relx=0.2, rely=0.1, anchor='w')
    names = ["", "DP240", "DP12", "DP6", "I2C", "I2P", "I2S", "KDP72"]
    tk.Label(canvas_back, text="Deltex", background="#FAEAB1", foreground="#003865",
             font=('Helvetica', 28, 'bold'), width=12).place(relx=0.78, rely=0.05)
    tk.Label(canvas_back, text="medical", background="#FAEAB1", foreground="#A2B5BB",
             font=('Helvetica', 18)).place(relx=0.85, rely=0.11)
    canvas_entry = Canvas(bg="#C58940", width=1150, height=400)
    canvas_entry.place(x=30, y=300)
    tk.Label(canvas_back, text="To create a series of folders for the final verification results to be recorded in\n"
                               "this tool will create these folders in the correct place.\n"
                               f"\n[ {data_path.get()} ]", background="#FAEAB1", font=("Courier", 14)).place(relx=0.05, rely=0.2)
    tk.Label(canvas_entry, text="Probe Type: ", background="#C58940", font=("Courier", 16)).place(relx=0.1, rely=0.2)
    someStyle = ttk.Style()
    someStyle.configure('my.TMenubutton', font=('Futura', 16))
    search_name = ttk.OptionMenu(canvas_entry, search_item, *names, style='my.TMenubutton')
    search_name['menu'].configure(font=('Futura', 16))
    search_name.place(relx=0.25, rely=0.2)
    search_item.set("Choose")
    tk.Label(canvas_entry, text="Select probe type from list ", background="#C58940",
             font=("Courier", 16)).place(relx=0.38, rely=0.2)
    tk.Label(canvas_entry, text="Batch Number without any letters: ", background="#C58940",
             font=("Courier", 16)).place(relx=0.1, rely=0.4)
    tk.Entry(canvas_entry, textvariable=batch, font=("Courier", 18), relief=SUNKEN, width=8).place(relx=0.5, rely=0.4)
    tk.Label(canvas_entry, text="Batch Number letters (first) ", background="#C58940",
             font=("Courier", 16)).place(relx=0.1, rely=0.55)
    tk.Entry(canvas_entry, textvariable=first_letter, font=("Courier", 18),
             relief=SUNKEN, width=1).place(relx=0.45, rely=0.55)
    tk.Label(canvas_entry, text="(last) ", background="#C58940",
             font=("Courier", 16)).place(relx=0.5, rely=0.55)
    tk.Entry(canvas_entry, textvariable=last_letter, font=("Courier", 18),
             relief=SUNKEN, width=1).place(relx=0.6, rely=0.55)
    tk.Button(canvas_entry, text="Generate Folders ", background="#2C74B3",
              font=("Courier", 18), command=generate).place(relx=0.7, rely=0.8)
    Tk.update(canvas_back)


display()


window.mainloop()

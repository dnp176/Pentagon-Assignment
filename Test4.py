import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path
import os
import time

my_w = tk.Tk()
my_w.geometry("400x200")  # Size of the window 
my_w.title("Upload File")  #  title
my_dir='' # string to hold directory path


class BackendProcess:
    def __init__(self):
        self.finished = False

    def run(self):
        time.sleep(10)
        self.finished = True

def my_fun(): 
    f_types = [('Pdf Files', '*.pdf')]
    my_dir = filedialog.askopenfilename(filetypes=f_types) # select directory 
    # update the text of Label with directory path
    e1.delete(0,tk.END)
    e1.insert(0,my_dir)
    # e1.config(state=tk.DISABLED)

def submit_evt():
    try:
        # print("Write Your Logic")
        pages = convert_from_path(e1.get(),500)
        saving_folder = r'C:\Users\Acer\OneDrive\Desktop\Python Project'
        c=1
        BackendProcess()
        for page in pages:
            l1.config(text="Extraction file",fg="green")
            img_name=f"img-{c}.jpg"
            page.save(os.path.join(saving_folder,img_name),"JPEG")
            c+=1
        l1.config(text="Extraction DONE....",fg="green")
    except:
        l1.config(text="Something Error",fg= "red")
        print("Something Error")

#Define Label
text = tk.Label(text = "Select Your File")
text.grid(row=0,column=0,padx=10,pady=10)

#Define Button
b1=tk.Button(my_w,text='Browse',
    command=lambda:my_fun())
b1.grid(row=1,column=0)

#Define File Path Label
e1 = tk.Entry(width = 30)
e1.grid(row=1,column=1,padx=2)  

#Submit Button Code
b2=tk.Button(my_w,text='Submit',
    command=lambda:submit_evt())
b2.grid(row=2,column=0,pady=10)

#Label for Display Import Msg or Error
l1 = tk.Label()
l1.grid(row=2,column=1)

my_w.mainloop()  # Keep the window open

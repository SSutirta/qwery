import os
from tkinter import filedialog
from tkinter import *

root = Tk()
path = StringVar()

def browse_button():
    global path
    global filename
    filename = filedialog.askdirectory()
    path.set(filename)
    print(filename)

# r=root, d=directories, f = files
def search(path):
    files = []
    print(path)
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))

    for f in files:
        print(f)

e1 = Entry(master=root)
e1.insert(0, 'keyword')
e1.grid(row=0, columnspan=4)
lbl1 = Label(master=root,textvariable=path)
lbl1.grid(row=2, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=2, column=3)
button1 = Button(text="Search", command= lambda: search(filename))
button1.grid(row=4, columnspan=4)

mainloop()
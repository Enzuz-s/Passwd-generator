from random import randint
from tkinter import LabelFrame, Entry, Frame, Button, END, Tk

root = Tk()
root.title("Password Generator")
root.geometry("500x300")


def new_rand():
    pwd_entry.delete(0, END)

    pw_length = int(my_entry.get())

    my_password = ''

    for _ in range(pw_length):
        my_password += chr(randint(33, 126))

    pwd_entry.insert(0, my_password)


def clip():
    root.clipboard_clear()
    root.clipboard_append(pwd_entry.get())


lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

pwd_entry = Entry(root, text='', font=("Helvetica", 24), bd=0)
pwd_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clip)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()

# import file
from tkinter import *

text = "Hi there what is going on?"
split_text = [x for x in text]


def check_text(sv, key, label):
    print(sv.get(), key)

    split_key = [x for x in sv.get()]

    # print(split_key)

    for x in range(0, len(split_key)):
        if split_key[x] == split_text[x]:
            print("CORRECT")
            word_label.config(bg='green')


window = Tk()
window.title("Speed Test")
window.config(padx=20, pady=10, bg="grey")

for x in range(0, len(split_text)):

    word_label = Label(
        text=f"{split_text[x]}", bg="red", font=("Arial", 20, 'bold'))
    word_label.grid(row=0, column=x)

sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv, key=split_text,
         label=word_label: check_text(sv, key, label))
word_enter = Entry(textvariable=sv, width=len(split_text))
word_enter.grid(row=1, column=0, columnspan=len(split_text) + 1)

window.mainloop()

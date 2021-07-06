from tkinter import *
import time
import math

text = 'A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea. A paragraph consists of one or more sentences. Though not required by the syntax of any language, paragraphs are usually an expected part of formal writing, used to organize longer prose'
# text_array = [x for x in text]
text_array = text.split(" ")

window = Tk()
window.title("Speed Test")
window.config(padx=20, pady=10, bg="grey")

counter_row = 0
counter_column = 0
for x in range(0, len(text_array)):
    letter_label = Label(text=text_array[x], bg="grey", justify=RIGHT)
    if x % 11 == 0:
        counter_row += 1
        counter_column = 0
        letter_label.grid(column=counter_column, row=counter_row)
        # counter_row += 1
        # input_entry = Entry()
        # input_entry.grid(column=counter_column, row=counter_row, columnspan=11)
    else:
        counter_column += 1
        letter_label.grid(column=counter_column, row=counter_row)

window.mainloop()

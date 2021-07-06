from tkinter import *
import time
import math

game_on = True
total_seconds = 0


def start_timer():
    global total_seconds, game_on
    total_seconds += 1
    time.sleep(1)
    format_timer()
    window.after(100, start_timer)


def format_timer():
    print(total_seconds)
    minutes = math.floor(total_seconds / 60)
    seconds = total_seconds - (minutes * 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    time_label.config(text=f"{minutes}:{seconds}")


################################# UI #####################################
window = Tk()
window.title("Speed Test")
window.config(padx=20, pady=10, bg="grey", width=500, height=500,
              cursor="hand2")

time_label = Label(text=f"0:00", bg="grey")
time_label.grid(row=0, column=0)

canvas = Canvas(width=500, height=500)
canvas.grid(column=0, row=1)

time_button = Button(text="Start", bg="grey", command=start_timer)
time_button.grid(column=0, row=2, padx=5, pady=5)

window.mainloop()

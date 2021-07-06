from tkinter import *
import time
import math

game_on = True
total_seconds = 0
add_second = ""

needed_text = "THIS IS THE FIRST TIME TO TEST TYPING"


def start_game():
    user_input.config(state=NORMAL)
    user_input.focus()

    def start_timer():
        global total_seconds, game_on, add_second
        # user_input.config(state=NORMAL)
        total_seconds += 1
        time.sleep(1)
        format_timer()
        add_second = window.after(10, start_timer)
    start_timer()


def format_timer():
    print(total_seconds)
    minutes = math.floor(total_seconds / 60)
    seconds = total_seconds - (minutes * 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    time_label.config(text=f"{minutes}:{seconds}")


def cancel_timer(event=None):
    global add_second
    print("CANCEL")
    window.after_cancel(add_second)
    final = user_input.get()
    final_array = [x for x in final]
    print(final_array)

    result_label.config(
        text=f"{len(final_array)} characters / {total_seconds} total seconds")


################################# UI #####################################
window = Tk()
window.title("Speed Test")
window.config(padx=20, pady=10, bg="grey", width=500, height=500,
              cursor="hand2")

time_label = Label(text=f"0:00", bg="grey", font=("Arial", 25))
time_label.grid(row=0, column=0, columnspan=2)

test_text = Label(text=needed_text,
                  font=("Arial", 35, 'bold'), wraplength=500, justify=LEFT, bg='grey')
test_text.grid(column=0, row=1, columnspan=2, pady=5, padx=5)

user_input = Entry(font=("Arial", 20), width=50, state=DISABLED)
user_input.grid(column=0, row=2, padx=5, pady=5, columnspan=2)


# time_button = Button(text="Start", bg="grey", command=start_timer)
time_button = Button(text="Start", bg="grey", command=start_game)
time_button.grid(column=0, row=3, padx=5, pady=5, columnspan=2)

result_label = Label(bg="grey", font=("Arial", 25))
result_label.grid(row=4, column=0, columnspan=2)


window.bind('<Return>', cancel_timer)

window.mainloop()

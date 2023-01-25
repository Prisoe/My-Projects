from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

"""Start Button initiated when the button is clicked, Imported global Reps and added the timer function """
def start():
    global REPS
    REPS += 1

    work_secs = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60


    # if it the 8th repetition
    if REPS % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Long Break", fg=RED)
    # if its the 2nd/4th/6th rep
    elif REPS % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Short Break", fg=PINK)
    # if its the 1st/3rd/5th/7th rep
    else:
        count_down(work_secs)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    mins = math.floor(count/60)
    secs = count % 60
    if secs < 10:
        secs = f"0{secs}"

    # How to configure a canvas item
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")

    if count > 0:
        global timer
        # 1000 is 1 sec delay using window.after
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Label
# fg for foreground to color a piece of text
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
# timer_label.place(x=55, y=-45)


checkmark_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

# Button


start_button = Button(text="Start", command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2, row=2)


window.mainloop()

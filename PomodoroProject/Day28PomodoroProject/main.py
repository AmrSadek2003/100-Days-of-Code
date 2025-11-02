import time
from tkinter import *

from tkinter import PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
SIXTY = 60

STOP_TIMER = False
REPS = 0


# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global STOP_TIMER
    global WORK_MIN
    global SHORT_BREAK_MIN
    global LONG_BREAK_MIN
    global SIXTY
    canvas.itemconfig(timer_text, text="00:00")
    WORK_MIN = 3
    SHORT_BREAK_MIN = 1
    LONG_BREAK_MIN = 2
    SIXTY = 60
    STOP_TIMER = True


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global STOP_TIMER
    global REPS
    global timer_label

    REPS +=1

    STOP_TIMER = False

    if REPS != 8 and REPS % 2 == 1:
        timer_label.config(text="Work", font=(FONT_NAME, 50, "bold"))
        work_timer_countdown(WORK_MIN)
        REPS += 1
    elif REPS % 2 == 0:
        timer_label.config(text="Short Break", font=(FONT_NAME, 30, "bold"))
        work_timer_countdown(SHORT_BREAK_MIN)
        REPS += 1
    else:
        timer_label.config(text="Long Break", font=(FONT_NAME, 30, "bold"))
        work_timer_countdown(LONG_BREAK_MIN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def work_timer_countdown(minutes):  # minutes = 15
    global SIXTY  # SIXTY = 60

    if minutes > 0 and STOP_TIMER == False:
        if SIXTY != 0:
            if minutes > 10:
                if SIXTY > 10:
                    canvas.itemconfig(timer_text, text=str(minutes - 1) + ":" + str(SIXTY - 1))
                    SIXTY -= 1
                    window.after(1000, work_timer_countdown, minutes)
                else:
                    canvas.itemconfig(timer_text, text=str(minutes - 1) + ":0" + str(SIXTY - 1))
                    SIXTY -= 1
                    window.after(1000, work_timer_countdown, minutes)
            else:
                if SIXTY > 10:
                    canvas.itemconfig(timer_text, text="0" + str(minutes - 1) + ":" + str(SIXTY - 1))
                    SIXTY -= 1
                    window.after(1000, work_timer_countdown, minutes)
                else:
                    canvas.itemconfig(timer_text, text="0" + str(minutes - 1) + ":0" + str(SIXTY - 1))
                    SIXTY -= 1
                    window.after(1000, work_timer_countdown, minutes)
        else:
            minutes -= 1
            SIXTY = 60
            window.after(1000, work_timer_countdown, minutes)
    else:
        canvas.itemconfig(timer_text, text="00:00")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# Tomato + Canvas UI
window = Tk()

window.title("Pomodoro")

window.config(padx=100, pady=100, bg=YELLOW)

fg = GREEN
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_image)
timer_text = canvas.create_text(122, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer UI
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"))
timer_label.config(foreground=GREEN, background=YELLOW)
timer_label.grid(column=1, row=0)
# work_timer_countdown(WORK_MIN)

# Checkmark Label

checkmark = Label(text="✔", foreground=GREEN, background=YELLOW, font=(24))
checkmark.grid(column=1, row=3)

# Start Button
start_button = Button(text="Start Button", font=(FONT_NAME, 10), command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset Button", font=(FONT_NAME, 10), command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()

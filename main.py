from tkinter import *
import math

# --------------------------- CONSTANT  --------------------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# --------------------------- TIMER RESET  -----------------------------
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(width=222, height=227, bg=YELLOW, highlightthickness=0)
    timer_text.config(text="Timer")
    check_label.config(text="")
# --------------------------- TIMER MECHANISM -----------------------------
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN

    if REPS % 8 == 0:
        start_count(long_break_sec)
        timer_label.config(fg=RED, text="Break")
    elif REPS % 2 == 0:
        start_count(short_break_sec)
        timer_label.config(fg=PINK, text="Break")
    else:
        start_count(work_sec)
        timer_label.config(fg=GREEN, text="Work")
    # if REPS % 8 == 0:
    #     set_timer = LONG_BREAK_MIN
    # elif REPS % 2 == 0:
    #     set_timer = SHORT_BREAK_MIN
    # else:
    #     set_timer = WORK_MIN
    # start_count(set_timer * 60)


# --------------------------- COUNTDOWN MECHANISM -----------------------------
def start_count(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, start_count, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(REPS / 2)
        for _ in range(work_session):
            marks += "✓"
            check_label.config(text=marks)

        # --------------------------- UI SETUP -----------------------------


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=222, height=227, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pngtree.png")
canvas.create_image(100, 114, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()

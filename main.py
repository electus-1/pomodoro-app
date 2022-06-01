import tkinter as t


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    greeting_label.config(text="Timer", fg=GREEN)
    global checkmarks
    checkmarks = ""
    checkmark_label.config(text=checkmarks)


def start_timer():
    global reps
    global checkmarks
    if reps == 0:
        greeting_label.config(text="Timer", fg=GREEN)
        checkmarks = ""
        checkmark_label.config(text=checkmarks)
    reps += 1
    if reps % 2 == 1:
        count = WORK_MIN * 60
        greeting_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count = LONG_BREAK_MIN * 60
        greeting_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count = SHORT_BREAK_MIN * 60
        greeting_label.config(text="Break", fg=PINK)

    count_down(count=count)


def count_down(count):
    global reps
    global checkmarks
    minutes = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    new_text = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=new_text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            checkmarks += CHECKMARK
            checkmark_label.config(text=checkmarks)

        if reps == 8:
            reps = 0
            window.after_cancel(timer)
            canvas.itemconfig(timer_text, text="00:00")

        else:
            start_timer()




window = t.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = t.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
domates = t.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=domates)
timer_text = canvas.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 32, "bold"), fill="white"
)
canvas.grid(row=1, column=1)

start_button = t.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = t.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)
greeting_label = t.Label(
    text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW
)
greeting_label.grid(row=0, column=1)
checkmarks = ""
checkmark_label = t.Label(
    text=checkmarks, font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW
)
checkmark_label.grid(row=3, column=1)

window.mainloop()

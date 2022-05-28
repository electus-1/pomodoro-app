import tkinter as t

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = t.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

start_button = t.Button(text="Start")
start_button.grid(row=2, column=0)
reset_button = t.Button(text="Reset")
reset_button.grid(row=2, column=2)
greeting_label = t.Label(
    text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW
)
greeting_label.grid(row=0, column=1)
checkmark_label = t.Label(
    text=CHECKMARK, font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW
)
checkmark_label.grid(row=3, column=1)

canvas = t.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
domates = t.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=domates)
canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 32, "bold"), fill="white")
canvas.grid(row=1, column=1)

window.mainloop()

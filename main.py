from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    print(count)
    window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, background=YELLOW)
count_down(5)

lbl_timer = Label(text='Timer', font=(FONT_NAME, 30, 'normal'), fg=GREEN, bg=YELLOW)
lbl_timer.grid(row=0, column=1)

btn_start = Button(text='Start')
btn_start.grid(row=2, column=0)

lbl_tick = Label(text='✓', fg=GREEN, bg=YELLOW)
lbl_tick.grid(row=2, column=1)

btn_start = Button(text='Reset')
btn_start.grid(row=2, column=2)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

window.mainloop()

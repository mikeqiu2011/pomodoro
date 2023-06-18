from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def conv_sec_to_min(seconds):
    min = str(seconds // 60)
    sec = str(seconds % 60)

    if len(min) == 1:
        min = '0' + min

    if len(sec) == 1:
        sec = '0' + sec

    return f'{min}:{sec}'


def count_down(count):
    canvas.itemconfig(txt_timer, text=conv_sec_to_min(count))

    if count >= 1:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        lbl_timer.config(fg=RED, text='Long break')
        count_down(long_break_sec)
    elif reps % 2 == 0:
        lbl_timer.config(fg=GREEN, text='Short break')
        count_down(short_break_sec)
    else:
        lbl_timer.config(fg=PINK, text='Work hard')
        count_down(work_sec)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, background=YELLOW)

lbl_timer = Label(text='Timer', font=(FONT_NAME, 30, 'normal'), fg=GREEN, bg=YELLOW)
lbl_timer.grid(row=0, column=1)

btn_start = Button(text='Start', command=start_timer)
btn_start.grid(row=2, column=0)

lbl_tick = Label(text='✓', fg=GREEN, bg=YELLOW)
lbl_tick.grid(row=2, column=1)

btn_reset = Button(text='Reset', bg=YELLOW, highlightthickness=0)
btn_reset.grid(row=2, column=2)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
txt_timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

window.mainloop()

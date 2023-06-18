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
    # txt_timer['text'] = count
    # print(count)
    window.after(1000, count_down, count-1)

def start_countdown():
    seconds = WORK_MIN * 60
    count_down(seconds)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, background=YELLOW)


lbl_timer = Label(text='Timer', font=(FONT_NAME, 30, 'normal'), fg=GREEN, bg=YELLOW)
lbl_timer.grid(row=0, column=1)

btn_start = Button(text='Start', command=start_countdown)
btn_start.grid(row=2, column=0)

lbl_tick = Label(text='✓', fg=GREEN, bg=YELLOW)
lbl_tick.grid(row=2, column=1)

btn_start = Button(text='Reset')
btn_start.grid(row=2, column=2)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
txt_timer = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


window.mainloop()

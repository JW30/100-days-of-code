from tkinter import *
import time

# Constants
BEIGE = "#F1DDBF"
NAVY = "#525E75"
GREEN = "#369B46"
PINK = "#F8A89D"
RED = "#F26849"
FONT_TEXT = ("Courier", 35, "bold")
FONT_TITLE = ("Courier", 45)
WORK = 25
SHORT_BREAK = 5
LONG_BREAK = 20
INTERVALS_AMNT = 4

# Variables
mode = WORK
secs = WORK * 60
clock_is_active = False
intervals_finished = 0


# Logic
def switch_mode():
    global mode
    global intervals_finished
    window.lift()
    window.call('wm', 'attributes', '.', '-topmost', True)
    window.focus_force()
    window.call( 'wm', 'attributes', '.', '-topmost', False)
    if mode == SHORT_BREAK or mode == LONG_BREAK:
        title.config(text="Timer", fg=NAVY)
        mode = WORK
        if intervals_finished == INTERVALS_AMNT:
            intervals_finished = 0
            intervals.config(text="")
    elif mode == WORK:
        intervals_finished += 1
        checkmarks = intervals.cget("text") + u"\u2713"
        intervals.config(text=checkmarks)
        title.config(text="Break", fg=PINK)
        if intervals_finished == INTERVALS_AMNT:
            mode = LONG_BREAK
        elif intervals_finished < INTERVALS_AMNT:
            mode = SHORT_BREAK


def format_secs():
    global secs
    return time.strftime('%M:%S', time.gmtime(secs))


def update_clock():
    global secs
    global clock_is_active
    global mode
    if clock_is_active:
        if secs == 0:
            switch_mode()
            reset_pressed()
        else:
            secs -= 1
        clock.itemconfig(timer_text, text=format_secs())
        window.after(1000, update_clock)


def start_pressed():
    global clock_is_active
    if clock_is_active:
        clock_is_active = False
        start_btn.config(text="Start")
    else:
        clock_is_active = True
        start_btn.config(text="Stop")
        update_clock()


def reset_pressed():
    global clock_is_active
    global secs
    clock_is_active = False
    secs = mode * 60
    start_btn.config(text="Start")
    clock.itemconfig(timer_text, text=format_secs())


# Window
window = Tk()
window.title("Pomodoro")
window.config(bg=BEIGE)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(5, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(4, weight=1)
window.minsize(400, 400)

# Labels
title = Label(text="Timer", bg=BEIGE, fg=NAVY, font=FONT_TITLE)
title.grid(row=1, column=2)

intervals = Label(text=u"", bg=BEIGE, fg=GREEN, font=FONT_TEXT)
intervals.grid(row=4, column=2)

# Canvas
clock = Canvas(width=200, height=224, bg=BEIGE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
clock.create_image(100, 112, image=tomato_img)
timer_text = clock.create_text(100, 130, text=f"{format_secs()}", font=FONT_TEXT)
clock.grid(row=2, column=2)

# Buttons
start_btn = Button(text="Start", highlightbackground=BEIGE, width=4, height=1, command=start_pressed)
start_btn.grid(row=3, column=1)

reset_btn = Button(text="Reset", highlightbackground=BEIGE, width=4, height=1, command=reset_pressed)
reset_btn.grid(row=3, column=3)


window.mainloop()

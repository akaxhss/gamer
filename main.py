from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F3E99F"
RED = "#FF6D60"
GREEN = "#98D8AA"
YELLOW = "#F7D060"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# comment for git


# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    print(count)
    if count > 0:
        window.after(1000,count_down,count-1)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Timer for 25")
window.config(padx=100,pady=50,bg=YELLOW)
count_down(5)
title_label = Label(text="Timer",fg= GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(row=0,column=1)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
canvas.create_text(100,130,text="00:00",fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)



start_button = Button(text="Start",highlightthickness=0)
start_button.grid(row=2,column=0)
reset_button = Button(text="Reset",highlightthickness=0)
reset_button.grid(row=2,column=2)

check_marks = Label(text="✔︎")


window.mainloop()

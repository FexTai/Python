import time
from tkinter import *

sec = -1
min = 0
std = 0
x = 1

def zeit():
    global sec, min
    sec += 1
    if sec == 60:
        sec = 0
        min += 1
    lb1["text"] = str(min) + ":" + str(sec)
    lb1.after(1000, zeit)


def start():
    zeit()


main = Tk()
main.geometry("600x400")
lb1 = Label(main, text="gogo")
lb1.pack()
#lb1.after(1000, update)

bt1 = Button(main, text="start", command=start)
bt1.pack()

main.mainloop()


start()
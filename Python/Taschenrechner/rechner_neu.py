import tkinter as tk

# Main fenster
main = tk.Tk()
main.geometry("500x700")
main.title("Calculator")
main.config(bg="black")
main.resizable(False, False)

lst = []
lst2 = []
lst3 = []
lst4 = []
lst5 = []
operator = 0
st = 0
nd = 0
percent = 0

# Zahlenfunktionen

print("hello world")


def pz():
    global lst, lst2, lst3, lst4, lst5, operator, st, nd, percent
    bt1['state'] = 'disabled'
    bt2['state'] = 'disabled'
    bt3['state'] = 'disabled'
    bt4['state'] = 'disabled'
    bt5['state'] = 'disabled'
    bt6['state'] = 'disabled'
    bt7['state'] = 'disabled'
    bt8['state'] = 'disabled'
    bt9['state'] = 'disabled'
    bt0['state'] = 'disabled'
    if lst == []:
        print()
    elif operator != 0:
        if lst3 == []:
            print()
        else:
            lst5.append("%")
            lb["text"] = lst + lst4 + lst2 + lst3 + lst5
            pzt['state'] = 'disabled'
    else:
        lst4.append("%")
        lb["text"] = lst + lst4 + lst2 + lst3
        pzt['state'] = 'disabled'


def ac():
    global lst, lst2, lst3, lst4, lst5, operator
    lb["text"] = "0"
    lst = []
    lst2 = []
    lst3 = []
    lst4 = []
    lst5 = []
    operator = 0
    btcomma['state'] = 'normal'
    minus['state'] = 'normal'
    mult['state'] = 'normal'
    divide['state'] = 'normal'
    plus['state'] = 'normal'
    pm['state'] = 'normal'
    pzt['state'] = 'normal'
    bt1['state'] = 'normal'
    bt2['state'] = 'normal'
    bt3['state'] = 'normal'
    bt4['state'] = 'normal'
    bt5['state'] = 'normal'
    bt6['state'] = 'normal'
    bt7['state'] = 'normal'
    bt8['state'] = 'normal'
    bt9['state'] = 'normal'
    bt0['state'] = 'normal'


def x0():
    global lst
    if operator != 0:
        lst3.append(0)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5
    else:
        lst.append(0)
        lb["text"] = lst


def x1():
    global lst
    if operator != 0:
        lst3.append(1)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5
    else:
        lst.append(1)
        lb["text"] = lst


def x2():
    global lst
    if operator != 0:
        lst3.append(2)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5
    else:
        lst.append(2)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5


def x3():
    global lst
    if operator != 0:
        lst3.append(3)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5
    else:
        lst.append(3)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5


def x4():
    global lst
    if operator != 0:
        lst3.append(4)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5
    else:
        lst.append(4)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5


def x5():
    global lst
    if operator != 0:
        lst3.append(5)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5
    else:
        lst.append(5)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5


def x6():
    global lst
    if operator != 0:
        lst3.append(6)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5
    else:
        lst.append(6)
        lb["text"] = lst


def x7():
    global lst
    if operator != 0:
        lst3.append(7)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5
    else:
        lst.append(7)
        lb["text"] = lst


def x8():
    global lst
    if operator != 0:
        lst3.append(8)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5
    else:
        lst.append(8)
        lb["text"] = lst


def x9():
    global lst
    if operator != 0:
        lst3.append(9)
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5
    else:
        lst.append(9)
        lb["text"] = lst


def plu():
    global lst2, operator
    if lst == []:
        print()
    else:
        lst2.append("+")
        lb["text"] = lst + lst4 + lst2
        operator = 1
        btcomma['state'] = 'normal'
        minus['state'] = 'disabled'
        mult['state'] = 'disabled'
        divide['state'] = 'disabled'
        plus['state'] = 'disabled'
        pm['state'] = 'disabled'
        pzt['state'] = 'normal'
        bt1['state'] = 'normal'
        bt2['state'] = 'normal'
        bt3['state'] = 'normal'
        bt4['state'] = 'normal'
        bt5['state'] = 'normal'
        bt6['state'] = 'normal'
        bt7['state'] = 'normal'
        bt8['state'] = 'normal'
        bt9['state'] = 'normal'
        bt0['state'] = 'normal'


def minu():
    global lst2, operator
    if lst == []:
        print()
    else:
        lst2.append("-")
        lb["text"] = lst + lst4 + lst2
        operator = 2
        btcomma['state'] = 'normal'
        minus['state'] = 'disabled'
        mult['state'] = 'disabled'
        divide['state'] = 'disabled'
        plus['state'] = 'disabled'
        pm['state'] = 'disabled'
        pzt['state'] = 'normal'
        bt1['state'] = 'normal'
        bt2['state'] = 'normal'
        bt3['state'] = 'normal'
        bt4['state'] = 'normal'
        bt5['state'] = 'normal'
        bt6['state'] = 'normal'
        bt7['state'] = 'normal'
        bt8['state'] = 'normal'
        bt9['state'] = 'normal'
        bt0['state'] = 'normal'


def div():
    global lst2, operator
    if lst == []:
        print()
    else:
        lst2.append(":")
        lb["text"] = lst + lst4 + lst2
        operator = 3
        btcomma['state'] = 'normal'
        minus['state'] = 'disabled'
        mult['state'] = 'disabled'
        divide['state'] = 'disabled'
        plus['state'] = 'disabled'
        pm['state'] = 'disabled'
        pzt['state'] = 'normal'
        bt1['state'] = 'normal'
        bt2['state'] = 'normal'
        bt3['state'] = 'normal'
        bt4['state'] = 'normal'
        bt5['state'] = 'normal'
        bt6['state'] = 'normal'
        bt7['state'] = 'normal'
        bt8['state'] = 'normal'
        bt9['state'] = 'normal'
        bt0['state'] = 'normal'


def multi():
    global lst2, operator
    if lst == []:
        print()
    else:
        lst2.append("x")
        lb["text"] = lst + lst4 + lst2
        operator = 4
        btcomma['state'] = 'normal'
        minus['state'] = 'disabled'
        mult['state'] = 'disabled'
        divide['state'] = 'disabled'
        plus['state'] = 'disabled'
        pm['state'] = 'disabled'
        pzt['state'] = 'normal'
        bt1['state'] = 'normal'
        bt2['state'] = 'normal'
        bt3['state'] = 'normal'
        bt4['state'] = 'normal'
        bt5['state'] = 'normal'
        bt6['state'] = 'normal'
        bt7['state'] = 'normal'
        bt8['state'] = 'normal'
        bt9['state'] = 'normal'
        bt0['state'] = 'normal'


def comma():
    global lst, lst2, lst3, operator
    if lst == []:
        print()
    elif operator != 0:
        if lst3 == []:
            print()
        else:
            lst3.append(".")
            lb["text"] = lst + lst4 + lst2 + lst3 + lst5
            btcomma['state'] = 'disabled'
    else:
        lst.append(".")
        lb["text"] = lst + lst4 + lst2 + lst3 + lst5
        btcomma['state'] = 'disabled'


def equals():
    global lst, lst2, lst3, lst4, lst5, st, nd, operator
    st = float(''.join(map(str, lst)))
    nd = float(''.join(map(str, lst3)))

    if operator == 1:
        lb["text"] = str(st + nd)
        if lst4 != [] and lst5 == []:
            lb["text"] = str(st/100 + nd)
        elif lst5 != [] and lst4 == []:
            lb["text"] = str(st + nd/100)
        elif lst4 != [] and lst5 != []:
            lb["text"] = str(st/100 + nd/100)

    elif operator == 2:
        lb["text"] = str(st - nd)
        if lst4 != [] and lst5 == []:
            lb["text"] = str(st/100 - nd)
        elif lst5 != [] and lst4 == []:
            lb["text"] = str(st - nd/100)
        elif lst4 != [] and lst5 != []:
            lb["text"] = str(st/100 - nd/100)

    elif operator == 3:
        lb["text"] = str(st / nd)
        if lst4 != [] and lst5 == []:
            lb["text"] = str((st/100) / nd)
        elif lst5 != [] and lst4 == []:
            lb["text"] = str(st / (nd/100))
        elif lst4 != [] and lst5 != []:
            lb["text"] = str((st/100) / (nd/100))

    elif operator == 4:
        lb["text"] = str(st * nd)
        if lst4 != [] and lst5 == []:
            lb["text"] = str((st/100) * nd)
        elif lst5 != [] and lst4 == []:
            lb["text"] = str(st * (nd/100))
        elif lst4 != [] and lst5 != []:
            lb["text"] = str((st/100) * (nd/100))

    elif operator == 5:
        lb["text"] = str(st ** nd)
        if lst4 != [] and lst5 == []:
            lb["text"] = str((st/100) ** nd)
        elif lst5 != [] and lst4 == []:
            lb["text"] = str(st ** (nd/100))
        elif lst4 != [] and lst5 != []:
            lb["text"] = str((st/100) ** (nd/100))
    operator = 0
    lst = []
    lst2 = []
    lst3 = []
    lst4 = []
    lst5 = []
    btcomma['state'] = 'normal'
    minus['state'] = 'normal'
    mult['state'] = 'normal'
    divide['state'] = 'normal'
    plus['state'] = 'normal'
    pm['state'] = 'normal'
    pzt['state'] = 'normal'
    bt1['state'] = 'normal'
    bt2['state'] = 'normal'
    bt3['state'] = 'normal'
    bt4['state'] = 'normal'
    bt5['state'] = 'normal'
    bt6['state'] = 'normal'
    bt7['state'] = 'normal'
    bt8['state'] = 'normal'
    bt9['state'] = 'normal'
    bt0['state'] = 'normal'


def noname():
    global lst2, operator
    if lst == []:
        print()
    else:
        lst2.append("^")
        lb["text"] = lst + lst4 + lst2
        operator = 5
        btcomma['state'] = 'normal'
        minus['state'] = 'disabled'
        mult['state'] = 'disabled'
        divide['state'] = 'disabled'
        plus['state'] = 'disabled'
        pm['state'] = 'disabled'
        pzt['state'] = 'normal'
        bt1['state'] = 'normal'
        bt2['state'] = 'normal'
        bt3['state'] = 'normal'
        bt4['state'] = 'normal'
        bt5['state'] = 'normal'
        bt6['state'] = 'normal'
        bt7['state'] = 'normal'
        bt8['state'] = 'normal'
        bt9['state'] = 'normal'
        bt0['state'] = 'normal'


lb = tk.Label(main, text="0", font=("Arial", 25, "bold"), bg="black", fg="white")
lb.place(x=50, y=60)

bt1 = tk.Button(main, text="7", font=("Arial", 40, "bold"), bg="#484848", fg="white", activebackground="#484848",
                activeforeground="white", command=x7)
bt1.place(x=0, y=210)

bt2 = tk.Button(main, text="8",  font=("Arial", 40, "bold"), bg="#484848", fg="white", activebackground="#484848",
                activeforeground="white", command=x8)
bt2.place(x=80, y=210)

bt3 = tk.Button(main, text="9",  font=("Arial", 40, "bold"), bg="#484848", fg="white", activebackground="#484848",
                activeforeground="white", command=x9)
bt3.place(x=160, y=210)

bt4 = tk.Button(main, text="4",  font=("Arial", 40, "bold"), bg="#484848", fg="white", activebackground="#484848",
                activeforeground="white", command=x4)
bt4.place(x=0, y=322)

bt5 = tk.Button(main, text="5",  font=("Arial", 40, "bold"), bg="#484848", fg="white", activebackground="#484848",
                activeforeground="white", command=x5)
bt5.place(x=80, y=322)

bt6 = tk.Button(main, text="6",  font=("Arial", 40, "bold"), bg="#484848", fg="white", activebackground="#484848",
                activeforeground="white", command=x6)
bt6.place(x=160, y=322)

bt7 = tk.Button(main, text="1",  font=("Arial", 40, "bold"), bg="#484848", fg="white", activebackground="#484848",
                activeforeground="white", command=x1)
bt7.place(x=0, y=434)

bt8 = tk.Button(main, text="2",  font=("Arial", 40, "bold"), bg="#484848", fg="white", activebackground="#484848",
                activeforeground="white", command=x2)
bt8.place(x=80, y=434)

bt9 = tk.Button(main, text="3",  font=("Arial", 40, "bold"), bg="#484848", fg="white", activebackground="#484848",
                activeforeground="white", command=x3)
bt9.place(x=160, y=434)

bt0 = tk.Button(main, text="0",  font=("Arial", 40, "bold"), bg="#484848", fg="white", activebackground="#484848",
                activeforeground="white", width=5, command=x0)
bt0.place(x=0, y=546)

btcomma = tk.Button(main, text=",",  font=("Arial", 14, "bold"), bg="#484848", fg="white", activebackground="#484848",
                    activeforeground="white", width=5, height=4, command=comma)
btcomma.place(x=172, y=549)

ac = tk.Button(main, text="AC", font=("Arial", 30, "bold"), bg="#878787", fg="white", activebackground="#878787",
               activeforeground="white", width=3, height=1, command=ac)
ac.place(x=0, y=126)

pm = tk.Button(main, text="^x", font=("Arial", 30, "bold"), bg="#878787", fg="white", activebackground="#878787",
               activeforeground="white", width=3, height=1, command=noname)
pm.place(x=85, y=126)

pzt = tk.Button(main, text="%", font=("Arial", 30, "bold"), bg="#878787", fg="white", activebackground="#878787",
                activeforeground="white", command=pz)
pzt.place(x=170, y=126)

divide = tk.Button(main, text="÷", font=("Arial", 30, "bold"), bg="orange", fg="white", activebackground="orange",
                   activeforeground="white", command=div)
divide.place(x=240, y=126)

mult = tk.Button(main, text="x", font=("Arial", 26, "bold"), bg="orange", fg="white", activebackground="orange",
                 activeforeground="white", height=2, command=multi)
mult.place(x=246, y=210)

minus = tk.Button(main, text="-", font=("Arial", 17, "bold"), bg="orange", fg="white", activebackground="orange",
                  activeforeground="white", height=3, width=3, command=minu)
minus.place(x=246, y=326)

plus = tk.Button(main, text="+", font=("Arial", 26, "bold"), bg="orange", fg="white", activebackground="orange",
                 activeforeground="white", height=2, command=plu)
plus.place(x=246, y=430)

equals = tk.Button(main, text="=", font=("Arial", 26, "bold"), bg="orange", fg="white", activebackground="orange",
                   activeforeground="white", height=2, command=equals)
equals.place(x=246, y=546)

main.mainloop()

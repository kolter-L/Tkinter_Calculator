from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def b_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def b_delete():
    e.delete(0, END)


def b_plus():
    global math
    global fnum
    first = e.get()
    fnum = int(first)
    e.delete(0, END)
    math = "add"


def b_minus():
    global math
    global fnum
    first = e.get()
    fnum = int(first)
    e.delete(0, END)
    math = "sub"


def b_mult():
    global math
    global fnum
    first = e.get()
    fnum = int(first)
    e.delete(0, END)
    math = "mult"


def b_div():
    global math
    global fnum
    first = e.get()
    fnum = int(first)
    e.delete(0, END)
    math = "div"


def b_equal():
    second = e.get()
    e.delete(0, END)

    if math == "add":
        e.insert(0, int(second) + fnum)

    if math == "sub":
        e.insert(0, fnum - int(second))

    if math == "div":
        e.insert(0, fnum / int(second))

    if math == "mult":
        e.insert(0, int(second) * fnum)


def saveit():
    global saved_num
    saved_num = e.get()
    e.delete(0, END)


def recallit():
    e.insert(0, saved_num)


b1 = Button(root, text="1", padx=40, pady=10, command=lambda: b_add(1))
b2 = Button(root, text="2", padx=40, pady=10, command=lambda: b_add(2))
b3 = Button(root, text="3", padx=40, pady=10, command=lambda: b_add(3))
b4 = Button(root, text="4", padx=40, pady=10, command=lambda: b_add(4))
b5 = Button(root, text="5", padx=40, pady=10, command=lambda: b_add(5))
b6 = Button(root, text="6", padx=40, pady=10, command=lambda: b_add(6))
b7 = Button(root, text="7", padx=40, pady=10, command=lambda: b_add(7))
b8 = Button(root, text="8", padx=40, pady=10, command=lambda: b_add(8))
b9 = Button(root, text="9", padx=40, pady=10, command=lambda: b_add(9))
b0 = Button(root, text="0", padx=40, pady=10, command=lambda: b_add(0))
b_clear = Button(root, text="clear", padx=40, pady=10, command=b_delete)

add = Button(root, text="+", padx=40, pady=10, command=b_plus)
minus = Button(root, text="-", padx=40, pady=10, command=b_minus)
div = Button(root, text="/", padx=40, pady=10, command=b_div)
mult = Button(root, text="x", padx=40, pady=10, command=b_mult)

equals = Button(root, text="=", padx=40, pady=10, command=b_equal)
remember = Button(root, text="memory +", padx=40, pady=10, command=saveit)
recall = Button(root, text="memory r", padx=40, pady=10, command=recallit)

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b0.grid(row=4, column=0)
b_clear.grid(row=4, column=1)

add.grid(row=4, column=2)

equals.grid(row=5, column=0)
remember.grid(row=6, column=1)
recall.grid(row=6, column=2)

minus.grid(row=5, column=1)
div.grid(row=5, column=2)
mult.grid(row=6, column=0)


root.mainloop()


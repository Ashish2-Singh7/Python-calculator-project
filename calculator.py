from tkinter import *

root = Tk()

def Click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "C":
        scvalue.set("")
        screen.update()

    elif text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())

        else:
            try:
                value = eval(scvalue.get())

            except Exception as e:
                print(e)
                value = "ERROR"

        scvalue.set(value)
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root.geometry("390x400")

root.title("Calculator by ASHISH SINGH")

# root.wm_iconbitmap("3.ico")

root.maxsize(390,400)
root.minsize(390,400)

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="roboto 21 bold")
screen.pack(padx="32", pady="13", fill="x")

f = Frame(root,)
b1 = Button(f, text="3", font="Roboto 19 bold", padx=12)
b1.pack(side="right", padx=22)
b1.bind("<Button-1>", Click)

b2 = Button(f, text="2", font="Roboto 19 bold", padx=12)
b2.pack(side="right", padx=22)
b2.bind("<Button-1>", Click)

b3 = Button(f, text="1", font="Roboto 19 bold", padx=12)
b3.pack(side="right", padx=22)
b3.bind("<Button-1>", Click)

# OPERATORS
oper1 = Button(f, text="+", font="Roboto 19 bold", padx=12)
oper1.pack(side="right", padx=2)
oper1.bind("<Button-1>", Click)

f.pack()

f2 = Frame(root)

b4= Button(f2, text="6", font="Roboto 19 bold", padx=12)
b4.pack(side="right", padx=22, pady=32)
b4.bind("<Button-1>", Click)

b5= Button(f2, text="5", font="Roboto 19 bold", padx=12)
b5.pack(side="right", padx=22, pady=32)
b5.bind("<Button-1>", Click)

b6= Button(f2, text="4", font="Roboto 19 bold", padx=12)
b6.pack(side="right", padx=22, pady=32)
b6.bind("<Button-1>", Click)

# OPERATORS
oper2 = Button(f2, text="-", font="Roboto 19 bold", padx=12)
oper2.pack(side="right", padx=2)
oper2.bind("<Button-1>", Click)

f2.pack()

f3 = Frame(root)
b9 = Button(f3, text="9", font="Roboto 19 bold", padx=12)
b9.pack(side="right", padx=22, pady=4)
b9.bind("<Button-1>", Click)

b8 = Button(f3, text="8", font="Roboto 19 bold", padx=12)
b8.pack(side="right", padx=22, pady=4)
b8.bind("<Button-1>", Click)

b7 = Button(f3, text="7", font="Roboto 19 bold", padx=12)
b7.pack(side="right", padx=22, pady=4)
b7.bind("<Button-1>", Click)

# OPERATORS
oper3 = Button(f3, text="/", font="Roboto 19 bold", padx=12)
oper3.pack(side="right", padx=2)
oper3.bind("<Button-1>", Click)

f3.pack()

f4 = Frame(root)

op = Button(f4, text="=", font="Roboto 19 bold", padx=12)
op.pack(side="right", pady=22, padx=22)
op.bind("<Button-1>", Click)

b0 = Button(f4, text="0", font="Roboto 19 bold", padx=13)
b0.pack(side="right", padx=22)
b0.bind("<Button-1>", Click)

op = Button(f4, text="C", font="Roboto 19 bold", padx=12)
op.pack(side="right", pady=22, padx=15)
op.bind("<Button-1>", Click)

oper4 = Button(f4, text="*", font="Roboto 19 bold", padx=13)
oper4.pack(side="right", padx=0)
oper4.bind("<Button-1>", Click)

f4.pack()

root.mainloop()
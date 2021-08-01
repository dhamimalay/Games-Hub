from tkinter import *

c1, c2, c3 = 0, 0, 0


def start():

    def inner():
        final = 0
        c = 1
        s1 = StringVar()
        s2 = StringVar()
        s3 = StringVar()
        s.config(state=DISABLED)

        b1 = Button(root, text="", fg="white", bg="black", font=8, width=20, height=5, command=lambda: play(b1, p1, p2))
        b1.grid(row=4, column=1)
        b2 = Button(root, text="", fg="white", bg="black", font=8, width=20, height=5, command=lambda: play(b2, p1, p2))
        b2.grid(row=4, column=2)
        b3 = Button(root, text="", fg="white", bg="black", font=8, width=20, height=5, command=lambda: play(b3, p1, p2))
        b3.grid(row=4, column=3)
        b4 = Button(root, text="", fg="white", bg="black", font=8, width=20, height=5, command=lambda: play(b4, p1, p2))
        b4.grid(row=5, column=1)
        b5 = Button(root, text="", fg="white", bg="black", font=8, width=20, height=5, command=lambda: play(b5, p1, p2))
        b5.grid(row=5, column=2)
        b6 = Button(root, text="", fg="white", bg="black", font=8, width=20, height=5, command=lambda: play(b6, p1, p2))
        b6.grid(row=5, column=3)
        b7 = Button(root, text="", fg="white", bg="black", font=8, width=20, height=5, command=lambda: play(b7, p1, p2))
        b7.grid(row=6, column=1)
        b8 = Button(root, text="", fg="white", bg="black", font=8, width=20, height=5, command=lambda: play(b8, p1, p2))
        b8.grid(row=6, column=2)
        b9 = Button(root, text="", fg="white", bg="black", font=8, width=20, height=5, command=lambda: play(b9, p1, p2))
        b9.grid(row=6, column=3)

        def play(b, x1, x2):
            nonlocal final
            if final == 0:
                nonlocal c
                global c1, c2, c3

                if b["text"] == "":
                    c = c + 1
                    if c % 2 == 0:
                        b["text"] = "O"
                    else:
                        b["text"] = "X"

                if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
                    b1.config(fg="red", bg="black")
                    b2.config(fg="red", bg="black")
                    b3.config(fg="red", bg="black")
                    v.set("Congratulations! " + x1.get() + ".")
                    c1 += 1
                    final = 1

                elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
                    b4.config(fg="red", bg="black")
                    b5.config(fg="red", bg="black")
                    b6.config(fg="red", bg="black")
                    v.set("Congratulations! " + x1.get() + ".")
                    c1 += 1
                    final = 1
                elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
                    b7.config(fg="red", bg="black")
                    b8.config(fg="red", bg="black")
                    b9.config(fg="red", bg="black")
                    v.set("Congratulations! " + x1.get() + ".")
                    c1 += 1
                    final = 1
                elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
                    b1.config(fg="red", bg="black")
                    b4.config(fg="red", bg="black")
                    b7.config(fg="red", bg="black")
                    v.set("Congratulations! " + x1.get() + ".")
                    c1 += 1
                    final = 1
                elif b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
                    b1.config(fg="red", bg="black")
                    b2.config(fg="red", bg="black")
                    b3.config(fg="red", bg="black")
                    v.set("Congratulations! " + x2.get() + ".")
                    c2 += 1
                    final = 1
                elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
                    b4.config(fg="red", bg="black")
                    b5.config(fg="red", bg="black")
                    b6.config(fg="red", bg="black")
                    v.set("Congratulations! " + x2.get() + ".")
                    c2 += 1
                    final = 1
                elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
                    b7.config(fg="red", bg="black")
                    b8.config(fg="red", bg="black")
                    b9.config(fg="red", bg="black")
                    v.set("Congratulations! " + x2.get() + ".")
                    c2 += 1
                    final = 1
                elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
                    b1.config(fg="red", bg="black")
                    b4.config(fg="red", bg="black")
                    b7.config(fg="red", bg="black")
                    v.set("Congratulations! " + x2.get() + ".")
                    c2 += 1
                    final = 1
                elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
                    b2.config(fg="red", bg="black")
                    b5.config(fg="red", bg="black")
                    b8.config(fg="red", bg="black")
                    v.set("Congratulations! " + x1.get() + ".")
                    c1 += 1
                    final = 1
                elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
                    b2.config(fg="red", bg="black")
                    b5.config(fg="red", bg="black")
                    b8.config(fg="red", bg="black")
                    v.set("Congratulations! " + x2.get() + ".")
                    c2 += 1
                    final = 1
                elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
                    b3.config(fg="red", bg="black")
                    b6.config(fg="red", bg="black")
                    b9.config(fg="red", bg="black")
                    v.set("Congratulations! " + x1.get() + ".")
                    c1 += 1
                    final = 1
                elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
                    b3.config(fg="red", bg="black")
                    b6.config(fg="red", bg="black")
                    b9.config(fg="red", bg="black")
                    v.set("Congratulations! " + x2.get() + ".")
                    c2 += 1
                    final = 1
                elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
                    b1.config(fg="red", bg="black")
                    b5.config(fg="red", bg="black")
                    b9.config(fg="red", bg="black")
                    v.set("Congratulations! " + x1.get() + ".")
                    c1 += 1
                    final = 1
                elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
                    b1.config(fg="red", bg="black")
                    b5.config(fg="red", bg="black")
                    b9.config(fg="red", bg="black")
                    v.set("Congratulations! " + x2.get() + ".")
                    c2 += 1
                    final = 1
                elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
                    b3.config(fg="red", bg="black")
                    b5.config(fg="red", bg="black")
                    b7.config(fg="red", bg="black")
                    v.set("Congratulations! " + x1.get() + ".")
                    c1 += 1
                    final = 1
                elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
                    b3.config(fg="red", bg="black")
                    b5.config(fg="red", bg="black")
                    b7.config(fg="red", bg="black")
                    v.set("Congratulations! " + x2.get() + ".")
                    c2 += 1
                    final = 1

                if c == 10 and final == 0:
                    v.set("It's Tie!")
                    c3 += 1

        def res():
            v.set("")
            s1.set("")
            s2.set("")
            s3.set("")
            inner()

        def result():
            s1.set(str(e1.get()) + ': ' + str(c1))
            lr1 = Label(root, textvariable=s1, fg="white", bg="black", font=8)
            lr1.grid(row=8, column=1, columnspan=3)

            s2.set(str(e2.get()) + ': ' + str(c2))
            lr2 = Label(root, textvariable=s2, fg="white", bg="black", font=8)
            lr2.grid(row=9, column=1, columnspan=3)

            s3.set('Tie: ' + str(c3))
            lr3 = Label(root, textvariable=s3, fg="white", bg="black", font=8)
            lr3.grid(row=10, column=1, columnspan=3)

        v = StringVar()
        label = Label(root, textvariable=v, fg="white", bg="black", font=("TkDefaultFont", 12))
        label.grid(row=7, column=2, pady=15)
        rs = Button(root, font=2, text="Restart", fg="white", bg="red", command=res)
        rs.grid(row=7, column=1, pady=10)
        result = Button(root, font=2, text="Result", fg="white", bg="red", command=result)
        result.grid(row=7, column=3, pady=10)

    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d' % (width, height))
    root.title("Tic Tac Toe")
    root.config(bg="black")
    extra = Label(root, text="", fg="black", bg="black")
    extra.grid(row=0, column=0, rowspan=10, padx=200)
    name = Label(root, text="Tic Tac Toe", fg="red", bg="black", font=("Berlin Sans FB", 40))
    name.grid(row=0, column=1, columnspan=3, pady=10)
    l1 = Label(root, font=5, text="Enter first player(o): ", fg="white", bg="black")
    l1.grid(row=1, column=1, pady=8)
    p1 = StringVar(value="First player")
    e1 = Entry(root, textvariable=p1, width=75)
    e1.grid(row=1, column=2, columnspan=2)
    l1 = Label(root, font=5, text="Enter second player(x): ", fg="white", bg="black")
    l1.grid(row=2, column=1, pady=8)
    p2 = StringVar(value="Second player")
    e2 = Entry(root, textvariable=p2, width=75)
    e2.grid(row=2, column=2, columnspan=2)
    s = Button(root, font=2, text="Let's Play!", fg="white", bg="red", command=inner)
    s.grid(row=3, column=2, pady=8)
    root.mainloop()


if __name__ == '__main__':
    start()
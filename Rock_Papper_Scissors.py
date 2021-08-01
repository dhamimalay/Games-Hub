import tkinter as tk
from tkinter import *
import random
from PIL import ImageTk, Image

us = 0
cs = 0


def main():
    def start():
        pr = StringVar()
        c = StringVar()
        r = StringVar()
        x = StringVar()

        def play(u):
            global us, cs
            n = random.randint(0, 2)
            decide = ["Stone", "Paper", "Scissor"]
            o = decide[n]
            if o == "Stone":
                opponent.config(image=stoneImage)
            elif o == "Paper":
                opponent.config(image=paperImage)
            else:
                opponent.config(image=scissorImage)

            if u == stone:
                if o == "Stone":
                    x.set("Round tied")
                elif o == "Paper":
                    cs += 1
                    x.set("You lost the round")
                else:
                    us += 1
                    x.set("You won the round")
            elif u == paper:
                if o == "Stone":
                    us += 1
                    x.set("You won the round")
                elif o == "Paper":
                    x.set("Round tied")
                else:
                    cs += 1
                    x.set("You lost the round")
            else:
                if o == "Stone":
                    cs += 1
                    x.set("You lost the round")
                elif o == "Paper":
                    us += 1
                    x.set("You won the round")
                else:
                    x.set("Round tied")

            pr.set(str(pname.get()) + " : " + str(us))
            score = Label(root, textvariable=pr, font=("Berlin Sans FB", 22), fg="white", bg="black", borderwidth=0)
            score.place(x=1090, y=330)
            c.set("Computer" + " : " + str(cs))
            computerScore = Label(root, textvariable=c, font=("Berlin Sans FB", 22), fg="white",
                                  bg="black", borderwidth=0)
            computerScore.place(x=1090, y=370)

        def reset():
            global us, cs
            us = 0
            cs = 0
            pr.set("")
            c.set("")
            r.set("")
            x.set("")
            start()

        def end():
            if (us > cs):
                r.set("Congratulations you won the game...")
            elif (cs > us):
                r.set("You lost the game you may try again...")
            else:
                r.set("Match tied...")
            winnerDisplay = Label(root, textvariable=r, font=("Berlin Sans FB", 22), fg="white", bg="black")
            winnerDisplay.place(x=420, y=360)


        computerImage = Image.open(r".\Image\comp.jpg")
        computerImage = ImageTk.PhotoImage(computerImage.resize((100, 100)))
        opponent = Label(root, image=computerImage, width=100, height=100)
        opponent.place(x=850, y=460)
        opponent.image = computerImage

        tempWin = Label(root, textvariable=x, borderwidth=0, font=("Berlin Sans FB", 22), fg="white", bg="black")
        tempWin.place(x=520, y=490)

        stoneImage = Image.open(r".\Image\stone.png")
        stoneImage = ImageTk.PhotoImage(stoneImage.resize((100, 100)))
        stone = Button(root, image=stoneImage, width=100, height=100, command=lambda: play(stone))
        stone.place(x=290, y=330)
        stone.image = stoneImage

        paperImage = Image.open(r".\Image\paper.png")
        paperImage = ImageTk.PhotoImage(paperImage.resize((100, 100)))
        paper = Button(root, image=paperImage, width=100, height=100, command=lambda: play(paper))
        paper.place(x=290, y=460)
        paper.image = paperImage

        scissorImage = Image.open(r".\Image\scissors.png")
        scissorImage = ImageTk.PhotoImage(scissorImage.resize((100, 100)))
        scissor = Button(root, image=scissorImage, command=lambda: play(scissor))
        scissor.place(x=290, y=590)
        scissor.image = scissorImage

        reset = Button(root, text="Reset", font=("Berlin Sans FB", 20), fg="white", bg="black", command=reset)
        reset.place(x=1250, y=630)
        end = Button(root, text="End the game", font=("Berlin Sans FB", 20), fg="white", bg="black", command=end)
        end.place(x=1050, y=630)

    root = tk.Tk()
    root.title("Rock Paper Scissor")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d' % (width, height))
    root.config(bg="black")
    H = Label(root, text="Rock Paper Scissor", font=("Berlin Sans FB", 40), fg="red", bg="black")
    H.place(x=570, y=20)
    name = Label(root, width=25, text="Enter your name : ", font=("Berlin Sans FB", 25), fg="white", bg="black")
    name.place(x=430, y=110)
    pname = StringVar(value="Player")
    e = Entry(root, textvariable=pname, width=10, font=("Berlin Sans FB", 25), fg="white", bg="black")
    e.place(x=800, y=110)
    b = Button(root, text="Let's Play!!!", command=start, font=("Berlin Sans FB", 23), fg="white", bg="black")
    b.place(x=700, y=180)
    root.mainloop()


if __name__ == '__main__':
    main()
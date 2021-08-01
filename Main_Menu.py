from tkinter import *
from PIL import ImageTk, Image


def main():
    def g1():
        root.destroy()
        import Hangman
        Hangman.main()

    def g2():
        root.destroy()
        import Tic_Tac_Toe
        Tic_Tac_Toe.start()

    def g3():
        root.destroy()
        import Rock_Papper_Scissors
        Rock_Papper_Scissors.main()

    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d' % (width, height))
    root.config(bg="black")

    head = Label(root, text="Games Hub", font=("Berlin Sans FB", 50), fg="red", bg="black")
    head.pack()

    l0 = Label(root, text="Click on any of the below games to play!!!", font=("Berlin Sans FB", 48), fg="white", bg="black")
    l0.place(x=190, y=250)
    
    game1 = Image.open(".\Image\Hangman.png")
    game1 = ImageTk.PhotoImage(game1.resize((300, 220)))
    b1 = Button(root, image=game1, width=300, height=220, border=0, command=g1)
    b1.place(x=180, y=400)
    l1 = Label(root, text="Hangman", font=("Berlin Sans FB", 25), fg="white", bg="black")
    l1.place(x=270, y=630)

    game2 = Image.open(r".\Image\TicTacToe.png")
    game2 = ImageTk.PhotoImage(game2.resize((300, 220)))
    b2 = Button(root, image=game2, width=300, height=220, border=0, command=g2)
    b2.place(x=610, y=400)
    l2 = Label(root, text="Tic Tac Toe", font=("Berlin Sans FB", 25), fg="white", bg="black")
    l2.place(x=680, y=630)

    game3 = Image.open(r".\Image\rps.png")
    game3 = ImageTk.PhotoImage(game3.resize((300, 220)))
    b3 = Button(root, image=game3, width=300, height=220, border=0, command=g3)
    b3.place(x=1030, y=400)
    l3 = Label(root, text="Rock Paper Scissors", font=("Berlin Sans FB", 25), fg="white", bg="black")
    l3.place(x=1050, y=630)

    by = Label(root, text="Developer contact", font=("Berlin Sans FB", 18), fg="white", bg="black")
    by.pack()
    s1 = Label(root, text="Malay Dhami", font=("Berlin Sans FB", 20), fg="white", bg="black")
    s1.pack()
    root.mainloop()


if __name__ == '__main__':
    main()

from tkinter import messagebox
from tkinter import *
import random
from string import ascii_uppercase


def main():
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d' % (width, height))
    root.config(bg="black")
    root.title("Hangman")
    words = ["RAJKOT", "AHMEDABAD", "DELHI", "MUMBAI", "JAIPUR", "SURAT", "VADODARA", "CHENNAI", "BENGALURU", "KOLKATA", "HYDERABAD", "INDORE", "LUCKNOW", "NAGPUR", "UDAIPUR", "AMRITSAR"]

    images = [PhotoImage(file='.\Image\hang0.png'), PhotoImage(file='.\Image\hang1.png'), PhotoImage(file='.\Image\hang2.png'),
              PhotoImage(file='.\Image\hang3.png'), PhotoImage(file='.\Image\hang4.png'), PhotoImage(file='.\Image\hang5.png'),
              PhotoImage(file='.\Image\hang6.png'), PhotoImage(file='.\Image\hang7.png'), PhotoImage(file='.\Image\hang8.png'),
              PhotoImage(file='.\Image\hang9.png'), PhotoImage(file='.\Image\hang10.png'), PhotoImage(file='.\Image\hang11.png')]

    Label(root, text="Hello", fg="black", bg="black").grid(row=0, column=0, rowspan=6, padx=225)
    Label(root, text="Hangman", fg="red", bg="black", font=("Berlin Sans FB", 32)).grid(row=0, column=1, columnspan=9, pady=10)
    img = Label(root)
    img.grid(row=1, column=1, columnspan=3, padx=10, pady=40)
    img.config(image=images[0])

    lblWord = StringVar()
    Label(root, textvariable=lblWord, font=("Arial 24 bold"), bg='black', fg='red').grid(row=1, column=4, columnspan=6, padx=10)
    v = StringVar()

    def msg():
        v.set("It's a city")
        l = Label(root, textvariable=v, font=("TkDefaultFont", 18), fg="white", bg="black")
        l.grid(row=8, column=1, columnspan=9)

    def newGame():
        global word_temp
        global count
        global final
        v.set("")
        count = 0
        img.config(image=images[0])
        org_word = random.choice(words)
        final = org_word
        word_temp = " ".join(org_word)
        lblWord.set(" ".join("_" * len(org_word)))

    def guess(letter):
        global count
        global final
        if count < 11:
            txt = list(word_temp)
            guessed = list(lblWord.get())
            if word_temp.count(letter) > 0:
                for c in range(len(txt)):
                    if txt[c] == letter:
                        guessed[c] = letter
                    lblWord.set("".join(guessed))
                    if lblWord.get() == word_temp:
                        messagebox.showinfo("Hangman", "Congratulations! You guessed the word...")
                        newGame()

            else:
                count += 1
                img.config(image=images[count])
                if count == 11:
                    str = "Game Over. The correct word was '" + final + "'"
                    messagebox.showwarning("Hangman", str)
                    newGame()

    r = 2
    col = 1
    count = 1
    for c in ascii_uppercase:
        Button(root, text=c, command=lambda c=c: guess(c), font=("Arial 18"), width=4, bg='black', fg='white').grid(row=r, column=col)
        col += 1
        if count == 9:
            r = 3
            col = 1
        if count == 18:
            r = 4
            col = 1
        count += 1
    Button(root, text="Hint", font=("TkDefaultFont", 12), width=6, height=2, command=msg).grid(row=4, column=9)
    Button(root, text="New\nGame", command=lambda: newGame(), font=("TkDefaultFont", 12), bg='red', fg='white').grid(row=7, column=5, pady=20)
    newGame()
    root.mainloop()


if __name__ == '__main__':
    main()

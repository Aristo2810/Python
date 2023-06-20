import random
import tkinter as tk


class Front:

    def __init__(self, fen):
        self.fen = fen
        self.back = Back(fen)
        self.rgbtohex = lambda r, g, b: f'#{r:02x}{g:02x}{b:02x}'
        self.entry = tk.Entry(self.fen, width=40)
        self.entry.pack(pady=100)
        self.button = tk.Button(
            self.fen,
            text="Valider",
            command=self.back.getentry,
        )
        self.button.pack()
        self.setup()

    def setup(self):
        self.fen.configure(bg=self.rgbtohex(36, 68, 92))
        self.fen.geometry("1080x720")
        self.fen.mainloop()


class Back:

    def __init__(self, fen):
        self.front = Front(fen)
        self.max_chance = 6
        self.chance = 6
        self.nb_hasard = random.randint(1, 6)

    def getentry(self):
        print(self.front.entry.get())

    def plus_ou_moins(self, nb_a_tester: int) -> int:
        if nb_a_tester == self.nb_hasard:
            return 1
        else:
            if nb_a_tester > self.nb_hasard:
                return 2
            else:
                return 0


def main():
    fen = tk.Tk()
    Back(fen)


if __name__ == "__main__":
    main()

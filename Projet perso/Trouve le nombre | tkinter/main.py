import tkinter as tk
import random


class Front:

    def __init__(self, fen):
        self.rgbtohex = lambda r, g, b: f'#{r:02x}{g:02x}{b:02x}'
        self.fen = fen
        self.setup_display()
        self.back = Back(self.fen)

    def setup_display(self) -> None:
        self.fen.configure(bg=self.rgbtohex(36, 68, 92))
        self.fen.geometry("1080x720")
        self.entry = tk.Entry(self.fen, width=40)
        self.var = tk.StringVar()
        self.entry.pack(pady=100)
        self.label = tk.Label(
            self.fen, bg=self.rgbtohex(36, 68, 92), textvariable=self.var
        )
        self.label.pack()
        # self.btn = tk.Button(self.fen, command=self.back.get_entry, width=15, text="Valider")
        # self.btn.pack()


class Back:

    def __init__(self, fen):
        self.front = Front(fen)
        self.random_numbers = random.randint(1, 100)
        self.max_chance = 6
        self.chance = 6

    def plus_ou_moins(self, nb_a_tester: int) -> int:
        if nb_a_tester == self.random_numbers:
            return 1
        else:
            if nb_a_tester > self.random_numbers:
                return 2
            else:
                return 0

    def get_entry(self):
        print(1)


def main():
    fen = tk.Tk()
    Back(fen)
    fen.mainloop()


if __name__ == '__main__':
    main()

import tkinter as tk
import random



class Front:

    def __init__(self, fen):
        self.rgbtohex = lambda r, g, b: f'#{r:02x}{g:02x}{b:02x}'
        self.fen = fen
        self.setup_display()

    def setup_display(self):
        self.fen.configure(bg=self.rgbtohex(36, 68, 92))
        self.fen.geometry("1080x720")
        self.entry = tk.Entry(self.fen, width=40)
        self.entry.pack(pady=100)

    def get_entry(self):
        pass


class Back:

    def __init__(self, fen):
        self.front = Front(fen)
        self.random_numbers = random.randint(1, 100)
        self.max_chance = 6
        self.chance = 6


def main():
    fen = tk.Tk()
    Back(fen)
    fen.mainloop()


if __name__ == '__main__':
    main()

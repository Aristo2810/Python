import random
import tkinter as tk


class Game:

    def __init__(self, fen):
        self.fen = fen
        self.vie = 6
        self.proposition = 0
        self.rgbtohex = lambda r, g, b: f'#{r:02x}{g:02x}{b:02x}'
        self.fen.configure(bg=self.rgbtohex(36, 68, 92))
        self.fen.geometry("1080x720")
        self.var = tk.StringVar()
        self.entry = tk.Entry(self.fen, width=40)
        self.entry.pack(pady=60)
        self.label = tk.Label(self.fen, bg=self.rgbtohex(36, 68, 92), textvariable=self.var)
        self.label.pack()
        self.btn = tk.Button(self.fen, width=15, text="Valider", command=self.get_entry)
        self.btn.pack()

    def get_entry(self):
        self.proposition = int(self.entry.get())

    @staticmethod
    def generate_random_numbers():
        return random.randint(1, 100)

    def ingame(self):
        while self.vie > 0:
            random_numbers = self.generate_random_numbers()
            if random_numbers == self.proposition:




def main():
    fen = tk.Tk()
    Game(fen)
    fen.mainloop()


if __name__ == '__main__':
    main()

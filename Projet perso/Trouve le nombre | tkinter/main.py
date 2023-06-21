import random
import tkinter as tk


class Game:

    def __init__(self, fen):
        self.fen = fen
        self.vie = 6
        self.rgbtohex = lambda r, g, b: f'#{r:02x}{g:02x}{b:02x}'
        self.fen.configure(bg=self.rgbtohex(36, 68, 92))
        self.fen.geometry("1080x720")
        self.var = tk.StringVar()
        self.entry = tk.Entry(self.fen, width=40)
        self.entry.pack(pady=60)
        self.label = tk.Label(self.fen, bg=self.rgbtohex(36, 68, 92), textvariable=self.var)
        self.label.pack()
        self.btn = tk.Button(self.fen, width=15, text="Valider", command=self.check_guess)
        self.btn.pack()
        self.btn_restart = tk.Button(self.fen, width=15, text="Rejouer ?", command=self.reset_game)
        self.btn_restart.pack_forget()
        self.start_game()

    def start_game(self):
        self.target_number = self.generate_random_number()
        self.vie = 6
        self.var.set("Devinez un nombre entre 1 et 100")
        self.btn.config(state=tk.NORMAL)

    @staticmethod
    def generate_random_number():
        return random.randint(1, 100)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.var.set("Veuillez entrer un nombre valide.")

        if guess == self.target_number:
            self.var.set("Félicitations ! Vous avez deviné le nombre.")
            self.btn.config(state=tk.DISABLED)
            self.btn_restart.pack(pady=10)
        elif guess < self.target_number:
            self.var.set("Le nombre à deviner est plus grand.")
            self.vie -= 1
        else:
            self.var.set("Le nombre à deviner est plus petit.")
            self.vie -= 1

        if self.vie == 0:
            self.var.set(f"Vous avez perdu. Le nombre était {self.target_number}.")
            self.btn.config(state=tk.DISABLED)
            self.btn_restart.pack(pady=10)

    def reset_game(self):
        self.start_game()


def main():
    fen = tk.Tk()
    Game(fen)
    fen.mainloop()


if __name__ == '__main__':
    main()

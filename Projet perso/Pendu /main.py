from faker import Faker
from os import system
faker = Faker('fr_FR')


def create_word():
    return faker.word()


def main():
    mot = create_word()
    guessed_letters = []
    print(''.join(['_' if lettre not in guessed_letters else lettre for lettre in mot]))
    tentative = 5
    while tentative != 0 and not all(lettre in guessed_letters for lettre in mot):
        lettre_proposee = input("Quelle lettre proposez-vous?\n==> ")
        if lettre_proposee in mot and lettre_proposee not in guessed_letters:
            guessed_letters.append(lettre_proposee)
        else:
            tentative -= 1
        system('clear')
        print(''.join(['_' if lettre not in guessed_letters else lettre for lettre in mot]))

    if len(guessed_letters) == len(mot):
        print("Bravo !")
    else:
        print(f"Dommage ! le mot a trouver était {mot}")
    replay = input("Voulez-vous rejouer (oui/non)\n==> ")
    if replay.lower() == "oui":
        main()


if __name__ == '__main__':
    main()
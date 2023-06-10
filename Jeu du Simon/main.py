import random


def main():
    perdu = False
    suite = []
    while not perdu:
        print('\033[H\033[J')
        nb_random = random.randint(1, 9)
        suite.append(str(nb_random))
        print(nb_random)
        proposition = input()
        if ''.join(suite) != proposition:
            perdu = True
    print(f"Perdu !\nVous avez réussi {len(suite) - 1}")


if __name__ == '__main__':
    main()

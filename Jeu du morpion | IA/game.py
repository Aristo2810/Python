import copy, pygame, numpy as np


BG_COULEUR = (7, 42, 64)
LINE_COULEUR = (0, 0, 0)
CIRC_COULEUR = (239, 231, 200)
CROSS_COULEUR = (239, 231, 200)
LARGEUR = 800
LONGUEUR = 800
ROWS, COLS = 3, 3
TAILLE = LARGEUR // COLS
LARGEUR_LIGNE = 15
CERCLE_LARGEUR = 15
CROIX_TAILLE = 20
RAYON = TAILLE // 4
OFFSET = 50


pygame.init()
screen = pygame.display.set_mode((LARGEUR, LONGUEUR))
screen.fill(BG_COULEUR)


class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def final_state(self, show=False):
        '''
            @renvoie 0 s'il n'y a pas encore de gain
            @renvoie 1 si le joueur 1 gagne
            @renvoie 2 si le joueur 2 gagne
        '''

        # verif vertical
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    COULEUR = CIRC_COULEUR if self.squares[0][col] == 2 else CROSS_COULEUR
                    iPos = (col * TAILLE + TAILLE // 2, 20)
                    fPos = (col * TAILLE + TAILLE // 2, LONGUEUR - 20)
                    pygame.draw.line(screen, COULEUR, iPos, fPos, LARGEUR_LIGNE)
                return self.squares[0][col]

        # verif horizontal
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    COULEUR = CIRC_COULEUR if self.squares[row][0] == 2 else CROSS_COULEUR
                    iPos = (20, row * TAILLE + TAILLE // 2)
                    fPos = (LARGEUR - 20, row * TAILLE + TAILLE // 2)
                    pygame.draw.line(screen, COULEUR, iPos, fPos, LARGEUR_LIGNE)
                return self.squares[row][0]

        # verif diagonal
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                COULEUR = CIRC_COULEUR if self.squares[1][1] == 2 else CROSS_COULEUR
                iPos = (20, 20)
                fPos = (LARGEUR - 20, LONGUEUR - 20)
                pygame.draw.line(screen, COULEUR, iPos, fPos, CROIX_TAILLE)
            return self.squares[1][1]

        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                COULEUR = CIRC_COULEUR if self.squares[1][1] == 2 else CROSS_COULEUR
                iPos = (20, LONGUEUR - 20)
                fPos = (LARGEUR - 20, 20)
                pygame.draw.line(screen, COULEUR, iPos, fPos, CROIX_TAILLE)
            return self.squares[1][1]

        return 0

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row, col))
        return empty_sqrs

    def isfull(self):
        return self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0


class AI:

    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    def minimax(self, board, maximizing): #IA
        case = board.final_state()
        if case == 1: return 1, None
        if case == 2: return -1, None
        elif board.isfull(): return 0, None

        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move

    def eval(self, main_board):

        eval, move = self.minimax(main_board, False)
        return move

class Game:

    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1  # 1-cross  #2-circles
        self.gamemode = 'ai'  # pvp ou ai
        self.running = True
        self.show_lines()


    def show_lines(self):
        screen.fill(BG_COULEUR)
        pygame.draw.line(screen, LINE_COULEUR, (TAILLE, 0), (TAILLE, LONGUEUR), LARGEUR_LIGNE)
        pygame.draw.line(screen, LINE_COULEUR, (LARGEUR - TAILLE, 0), (LARGEUR - TAILLE, LONGUEUR), LARGEUR_LIGNE)
        pygame.draw.line(screen, LINE_COULEUR, (0, TAILLE), (LARGEUR, TAILLE), LARGEUR_LIGNE)
        pygame.draw.line(screen, LINE_COULEUR, (0, LONGUEUR - TAILLE), (LARGEUR, LONGUEUR - TAILLE), LARGEUR_LIGNE)

    def draw_fig(self, row, col):
        if self.player == 1:
            start_desc = (col * TAILLE + OFFSET, row * TAILLE + OFFSET)
            end_desc = (col * TAILLE + TAILLE - OFFSET, row * TAILLE + TAILLE - OFFSET)
            pygame.draw.line(screen, CROSS_COULEUR, start_desc, end_desc, CROIX_TAILLE)
            start_asc = (col * TAILLE + OFFSET, row * TAILLE + TAILLE - OFFSET)
            end_asc = (col * TAILLE + TAILLE - OFFSET, row * TAILLE + OFFSET)
            pygame.draw.line(screen, CROSS_COULEUR, start_asc, end_asc, CROIX_TAILLE)

        elif self.player == 2:
            center = (col * TAILLE + TAILLE // 2, row * TAILLE + TAILLE // 2)
            pygame.draw.circle(screen, CIRC_COULEUR, center, RAYON, CERCLE_LARGEUR)

    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()

    def next_turn(self):
        self.player = self.player % 2 + 1

    def change_gamemode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'

    def isover(self):
        return self.board.final_state(show=True) != 0 or self.board.isfull()

    def reset(self):
        self.__init__()


def main():
    game = Game()
    board = game.board
    ai = game.ai

    while True: #boucle pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    game.change_gamemode()

                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

                if event.key == pygame.K_i:
                    ai.level = 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // TAILLE
                col = pos[0] // TAILLE
                if board.empty_sqr(row, col) and game.running:
                    game.make_move(row, col)
                    if game.isover():
                        game.running = False

        if game.gamemode == 'ai' and game.player == ai.player and game.running:
            pygame.display.update()
            row, col = ai.eval(board)
            game.make_move(row, col)
            if game.isover():
                game.running = False

        pygame.display.update()


main()
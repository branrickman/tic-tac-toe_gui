# tic tac toe
import pygame
import time
from sys import exit
from random import randint

class Board(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.spaces = [0, 0, 0,
                       0, 0, 0,
                       0, 0, 0]
        self.image = pygame.image.load("assets/images/#.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (900, 900))
        self.rect = self.image.get_rect(center=(500 + randint(-20, 20), 500 + randint(-20, 20)))
        self.player = 1
        self.game_state = 0

    def player_input(self):
        square_positions = [(x, y) for y in [15, 340, 1000] for x in [50, 400, 730]]

        def determine_clicked_square(pos, self, positions):
            for position in square_positions:
                print(position)
                if pos[0] <= position[0] + 300:
                    if pos[1] <= position[1] + 300:
                        square = positions.index(position)
                        if self.spaces[square] == 0:  # check if position is already taken
                            return square
                        else:
                            return -1

        def make_move(pos, self, positions):
            square = determine_clicked_square(pos, self, positions)
            if square != -1:  # determine squares returns an index for the board (self.spaces). -1 is out of bounds, so we use it to indicate a move is invalid
                self.spaces[square] = self.player
                self.player *= -1
                square = -1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.game_state == 1:
                pos = pygame.mouse.get_pos()
                make_move(pos, self, square_positions)

    def print_board(self):
        # reversing the x, y like this means that the spaces are numbered across rows first
        if self.game_state == 1:
            pos = [(x, y) for y in [15+ randint(-20, 20), 340+ randint(-20, 20), 690+ randint(-20, 20)] for x in [50+ randint(-20, 20), 400+ randint(-20, 20), 730+ randint(-20, 20)]]
            spaces = self.spaces
            for i in range(9):
                time.sleep(0.005)
                if spaces[i] == 1:
                    screen.blit(x_surf, pos[i])
                if spaces[i] == -1:
                    screen.blit(o_surf, pos[i])

    def reset(self):
        self.spaces = [0, 0, 0,
                       0, 0, 0,
                       0, 0, 0]
        self.player *= -1

    def check_if_winner(self):
        def detect_win(self):
            for p in [-1, 1]:
                if self.spaces[0] == p and self.spaces[1] == p and self.spaces[2] == p:
                    return 'win'
                if self.spaces[3] == p and self.spaces[4] == p and self.spaces[5] == p:
                    return 'win'
                if self.spaces[6] == p and self.spaces[7] == p and self.spaces[8] == p:
                    return 'win'
                if self.spaces[0] == p and self.spaces[4] == p and self.spaces[8] == p:
                    return 'win'
                if self.spaces[2] == p and self.spaces[4] == p and self.spaces[6] == p:
                    return 'win'
                if self.spaces[0] == p and self.spaces[3] == p and self.spaces[6] == p:
                    return 'win'
                if self.spaces[1] == p and self.spaces[4] == p and self.spaces[7] == p:
                    return 'win'
                if self.spaces[2] == p and self.spaces[5] == p and self.spaces[8] == p:
                    return 'win'
            count = 0
            for i in range(9):
                if self.spaces[i] == 0:
                    count =+ 1
            if count == 0:
                return 'draw'
            else:
                return 'in progress'

        win = detect_win(self)

        if win == 'draw':
            board.draw(screen)
            pygame.display.update()
            print(f'{"Round is a DRAW"}')
            time.sleep(5)
            print(f'{"Game Resetting"}')
            self.reset()

        if win == 'win':
            board.draw(screen)
            pygame.display.update()
            if self.player * -1 == 1:
                winner = 'x'
            else:
                winner = 'o'
            print(f'{winner, "wins!"}')
            time.sleep(3)
            print(f'{"Game Resetting"}')
            self.reset()
            self.game_state = 2

    def update_game_state(self):
        if self.game_state == 1:
            return 0
        if self.game_state != 1:
            if self.game_state == 0:
                screen.blit(game_start_surf, game_start_rect)
            if self.game_state == 2:
                screen.fill((194, 229, 255))
                screen.blit(game_over_surf, game_over_rect)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.game_state = 1

    def update(self):
        self.player_input()
        self.print_board()
        self.check_if_winner()
        self.update_game_state()
        x_offset = randint(-20, 20)
        y_offset = randint(-20, 20)
        self.rect = self.image.get_rect(center=(500 + x_offset, 500 + y_offset))


# setup
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("ExTrEmE TiC tAc ToE")
clock = pygame.time.Clock()

x_surf = pygame.image.load("assets/images/x.png").convert_alpha()
x_surf = pygame.transform.scale(x_surf, (200, 200))
x_rect = x_surf.get_rect(center=(500, 500))

o_surf = pygame.image.load("assets/images/o.png").convert_alpha()
o_surf = pygame.transform.scale(o_surf, (200, 200))
o_rect = o_surf.get_rect(center=(500, 500))

game_start_surf = pygame.image.load("assets/images/eTtT_start.png").convert_alpha()
game_start_rect = game_start_surf.get_rect(topleft = (0,0))

game_over_surf = pygame.image.load("assets/images/win_screen.png").convert_alpha()
game_over_surf = pygame.transform.scale(game_over_surf, (1000, 1000))
game_over_rect = game_over_surf.get_rect(topleft = (0,0))

board = pygame.sprite.GroupSingle()
board.add(Board())

# Game Loop
while True:
    screen.fill((94, 129, 162))
    board.draw(screen)
    board.update()
    pygame.display.update()
    clock.tick(60)
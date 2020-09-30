from player.ai_player import AiPlayer
from board import Board
from player.base_player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player()
        self.player2 = AiPlayer()

    def run(self):
        pass
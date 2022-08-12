import random

from tqdm import tqdm

from game import Game
from multiplayer_game import MultiplayerGame
from player import Player


class Multiplayer:
    def __init__(self, players: list[Player], possible_words: list[str], number_of_games: int = 10):
        self.players = players
        self.possible_words = possible_words
        self.solutions = []
        self.number_of_games = number_of_games
        self.stats = [0 for _ in range(len(players))]

    def play_multi(self):
        for _ in tqdm(range(self.number_of_games)):
            solution = random.choice(self.possible_words)
            self.solutions.append(solution)
            winner = MultiplayerGame(self.players, self.possible_words, solution).play()
            self.stats[winner] += 1
            print(f"Player number {self.stats.index(max(self.stats))} is the overall winner with {max(self.stats)} wins")
import random

from tqdm import tqdm

from game import Game
from player import Player


class Comparator:
    def __init__(self, player_one: Player, player_two: Player, possible_words: list[str], number_of_games: int = 10):
        self.player_one = player_one
        self.player_two = player_two
        self.possible_words = possible_words
        self.number_of_games = number_of_games
        self.player_one_results = []
        self.player_two_results = []
        self.solutions = []

    def compare(self):
        for _ in tqdm(range(self.number_of_games)):
            solution = random.choice(self.possible_words)
            self.solutions.append(solution)
            self.player_one_results.append(Game(self.player_one, self.possible_words, solution).play())
            self.player_two_results.append(Game(self.player_two, self.possible_words, solution).play())

    def average_scores(self):
        wrong_guesses_p1 = sum([gr[1] for gr in self.player_one_results]) / len(self.player_one_results)
        guesses_p1 = sum([gr[0] for gr in self.player_one_results]) / len(self.player_one_results)

        wrong_guesses_p2 = sum([gr[1] for gr in self.player_two_results]) / len(self.player_two_results)
        guesses_p2 = sum([gr[0] for gr in self.player_two_results]) / len(self.player_two_results)

        return (wrong_guesses_p1, guesses_p1), (wrong_guesses_p2, guesses_p2)

    def win_ratio(self):
        player_one_win_ratio = len([gr[1] for gr in self.player_one_results if gr[1] <= 11]) / len(
            self.player_one_results)
        player_two_win_ratio = len([gr[1] for gr in self.player_two_results if gr[1] <= 11]) / len(
            self.player_two_results)

        return player_one_win_ratio, player_two_win_ratio

    def __str__(self):
        p1, p2 = self.average_scores()
        wr1, wr2 = self.win_ratio()

        result = f'Average wrong guesses / guesses for player one: {p1[0]}, {p1[1]}, win ratio {wr1 * 100:.2f}%\n'
        result += f'Average wrong guesses / guesses for player two: {p2[0]}, {p2[1]}, win ratio {wr2 * 100:.2f}%\n'
        result += f'Solutions: {self.solutions}\n'

        return result

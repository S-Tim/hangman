import random
import string

from player import Player


class RandomPlayer(Player):
    def guess(self, state: str, guesses: list[str], possible_words: list[str]) -> str:
        choice = random.choice([c for c in string.ascii_lowercase if c not in guesses])
        print(state)
        print(f"Randomplayer guesses: {choice}")
        return choice

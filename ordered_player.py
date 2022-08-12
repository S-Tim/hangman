import random
import string

from player import Player


class OrderedPlayer(Player):
    def guess(self, state: str, guesses: list[str], possible_words: list[str]) -> str:
        ordered_alphabet = 'enisratdhulcgmobwfkzpvjyxq'.lower()
        choice = [c for c in ordered_alphabet if c not in guesses][0]
        print(state)
        print(f"Orderedplayer guesses: {choice}")
        return choice
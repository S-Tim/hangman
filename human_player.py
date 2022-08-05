from player import Player


class HumanPlayer(Player):
    def guess(self, state: str, guesses: list[str], possible_words: list[str]) -> str:
        print(state)
        return input('Guess a character or word: ')

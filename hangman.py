from human_player import HumanPlayer
from multiplayer import Multiplayer
from ordered_player import OrderedPlayer
from random_player import RandomPlayer


def build_state(solution: str, character_guesses: list[str]) -> str:
    state = [c if c in character_guesses else '_' for c in solution]
    return ''.join(state)


if __name__ == '__main__':
    with open('hangman_words.txt') as f:
        possible_words = f.read().splitlines()

    game = Multiplayer([HumanPlayer(), OrderedPlayer()], possible_words, 1)
    game.play_multi()
    #print(comparator)
    # game = Game(HumanPlayer(), possible_words)

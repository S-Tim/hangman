from comparator import Comparator
from expected_information_gain_player import ExpectedInformationGainPlayer
from human_player import HumanPlayer
from random_player import RandomPlayer


def build_state(solution: str, character_guesses: list[str]) -> str:
    state = [c if c in character_guesses else '_' for c in solution]
    return ''.join(state)


if __name__ == '__main__':
    with open('hangman_words.txt') as f:
        possible_words = f.read().splitlines()

    comparator = Comparator(ExpectedInformationGainPlayer(), RandomPlayer(), possible_words)
    comparator.compare()
    print(comparator)
    # game = Game(HumanPlayer(), possible_words)

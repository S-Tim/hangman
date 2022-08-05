from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def guess(self, state: str, guesses: list[str], possible_words: list[str]) -> str:
        pass

    @staticmethod
    def matches(state: str, guesses: list[str], possible_words: list[str]) -> list[str]:
        possible_solutions = []
        for word in possible_words:
            if Player._matches(state, guesses, word):
                possible_solutions.append(word)

        return possible_solutions

    @staticmethod
    def _matches(state: str, guesses: list[str], word: str) -> bool:
        if len(word) != len(state):
            return False

        # guessed letters that were wrong
        for c in guesses:
            if c not in state and c in word:
                return False

        # 1. State is not blank and the characters match
        # 2. State is blank but already contains the character in another position, meaning it was guessed before and
        #    would have been filled if it were correct
        for (a, b) in zip(word, state):
            if (b != '_' and a != b) or (b == '_' and a in state):
                return False

        return True

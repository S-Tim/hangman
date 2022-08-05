from player import Player

import random


class Game:
    def __init__(self, player: Player, words: list[str], solution: str = None):
        self.player = player
        self.guesses = []
        self.wrong_guesses = 0
        self.guess_count = 0
        self.words = words
        self.solution = solution if solution in words else random.choice(words)

    def play(self):
        state = self.build_state()

        while state != self.solution:
            guess = self.player.guess(state, self.guesses, self.words)

            for c in guess:
                if c not in self.guesses:
                    self.guess_count += 1
                    self.guesses.append(c)
                    if guess not in self.solution:
                        self.wrong_guesses += 1

            state = self.build_state()

        return self.guess_count, self.wrong_guesses

    def build_state(self) -> str:
        state = [c if c in self.guesses else '_' for c in self.solution]
        return ''.join(state)

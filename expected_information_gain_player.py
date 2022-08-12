import math
import string

from player import Player


class ExpectedInformationGainPlayer(Player):
    def guess(self, state: str, guesses: list[str], possible_words: list[str]) -> str:
        possible_guesses = [c for c in string.ascii_lowercase if c not in guesses]
        remaining_solutions = self.matches(state, guesses, possible_words)
        remaining_solutions_length = len(remaining_solutions)
        remaining_entropy = math.log2(remaining_solutions_length) if remaining_solutions_length != 0 else 0
        # print(f'Remaining Entropy: {remaining_entropy} bits')

        # don't look through all words if there are too many
        # sample = random.sample(remaining_solutions, min(len(remaining_solutions), 100))

        # if len(remaining_solutions) == 1:
        #     print(remaining_solutions[0])
        #     return remaining_solutions[0]

        entropies = []
        for g in possible_guesses:
            possible_solutions = [word for word in remaining_solutions if g in word]
            if len(possible_solutions) != 0:
                information_gain = remaining_entropy - math.log2(len(possible_solutions))
                # information gain multiplied by probability of one of the possible solutions appearing
                entropies.append((g, information_gain * (len(possible_solutions) / remaining_solutions_length)))

        sorted_entropy = sorted(entropies, key=lambda item: item[1], reverse=True)
        # self.print_entropy(sorted_entropy)

        # if remaining_entropy <= 3.0:
        #     print(remaining_solutions)
        # print(state, sorted_entropy[0][0])
        return sorted_entropy[0][0]

    @staticmethod
    def print_entropy(sorted_entropy: list[tuple[str, float]]):
        for (char, entropy) in sorted_entropy:
            print(f'({char}: {entropy:.3f})', end=' ')
        print()

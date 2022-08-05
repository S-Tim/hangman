def main():
    with open('words.txt') as f:
        words = f.read().splitlines()

    words = [word.lower() for word in words]
    print_info(words)

    print()
    print('Alpha only')
    words = [word for word in words if word.isalpha()]
    print_info(words)

    print()
    print('Alpha only and at least 4 characters')
    words = [word for word in words if len(word) >= 4]
    print_info(words)

    print()
    print('Alpha only and at least 4 characters as set')
    words = list(set(words))
    print_info(words)

    with open('hangman_words.txt', 'w') as f:
        f.write('\n'.join(words))


def print_info(words):
    print('Words in list:', len(words))
    longest_word = max(words, key=lambda word: len(word))
    print('Longest word:', longest_word, len(longest_word))
    shortest_word = min(words, key=lambda word: len(word))
    print('Shortest word:', shortest_word, len(shortest_word))


if __name__ == '__main__':
    main()

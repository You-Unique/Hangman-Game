import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "kiwi", "melon", "peach",
             "python", "hangman", "computer", "keyboard", "mouse", "monitor",
             "chair", "desk", "lamp", "book", "pen", "pencil", "paper",
             "dog", "cat", "fish", "bird", "rabbit", "hamster", "turtle",
             "horse", "pig", "cow", "sheep", "goat", "chicken", "duck",
             "elephant", "giraffe", "lion", "tiger", "zebra", "bear", "wolf",
             "fox", "deer", "moose", "rhino", "hippo", "kangaroo", "koala",
             "monkey", "panda", "penguin", "snake", "crocodile", "alligator",
             "frog", "lizard", "seal", "whale", "dolphin", "shark", "octopus",
             "jellyfish", "starfish", "crab", "lobster", "snail", "bee",
             "butterfly", "ant", "spider", "scorpion", "dragonfly", "ladybug",
             "firefly", "grasshopper", "caterpillar", "beetle", "cockroach",
             "mosquito", "fly", "wasp", "hornet", "termite", "tick", "flea",
             "moth", "moth", "weevil", "aphid", "earwig", "butterfly",
             "cicada", "bedbug", "mantis", "millipede", "centipede"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def draw_hangman(num_wrong_guesses):
    stages = [  # ASCII art for hangman stages
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    print(stages[num_wrong_guesses])

def hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    stages = draw_hangman.stages  # Access the stages list from draw_hangman function
    max_wrong_guesses = len(stages) - 1

    name = input("What's your name? ")
    print(f"\n{name} Welcome to Hangman!")
    print(f"Your Word is {display_word(word, guessed_letters)}")

    while True:
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")
            draw_hangman(wrong_guesses)

        displayed_word = display_word(word, guessed_letters)
        print(displayed_word)

        if displayed_word == word:
            print(f"Congratulations {name}! You've guessed the word correctly!")
            break
        elif wrong_guesses >= max_wrong_guesses:
            print(f"Sorry {name}! You've run out of guesses. The word was: {word}")
            break

# Attach the stages list to the draw_hangman function object
draw_hangman.stages = [
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     /
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |
       -
    """,
    """
       --------
       |      |
       |      O
       |     \\|
       |      |
       |
       -
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      |
       |
       -
    """,
    """
       --------
       |      |
       |      O
       |
       |
       |
       -
    """,
    """
       --------
       |      |
       |
       |
       |
       |
       -
    """
]

hangman()

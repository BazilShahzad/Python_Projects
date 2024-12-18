import random

# Hangman art dictionary
hangman_art = {
    0: (" ", " ", " "),
    1: (" o ", " ", " "),
    2: (" o ", " | ", " "),
    3: (" o ", "/| ", " "),
    4: (" o ", "/|\\", " "),
    5: (" o ", "/|\\", "/ "),
    6: (" o ", "/|\\", "/\\ "),
}

# List of words for the game
word_list = ["python", "programming", "hangman", "developer", "algorithm"]

# Function to display the hangman
def display_hangman(tries):
    for part in hangman_art[tries]:
        print(part)

# Main game function
def play_hangman():
    print("Welcome to Hangman!")
    word = random.choice(word_list).lower()  # Choose a random word
    guessed_word = ["_"] * len(word)  # Create a display list for the guessed word
    guessed_letters = set()  # Keep track of guessed letters
    tries = 0
    max_tries = len(hangman_art) - 1

    print("\nGuess the word:")
    print(" ".join(guessed_word))
    print()

    while tries < max_tries:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed_word[idx] = guess
        else:
            print(f"'{guess}' is not in the word.")
            tries += 1

        # Display current hangman state
        display_hangman(tries)
        print("\nWord: " + " ".join(guessed_word))

        # Check if the word is fully guessed
        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nYou ran out of tries! The word was:", word)
        print("Game Over!")

# Start the game
play_hangman()

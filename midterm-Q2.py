# Author: Caleb Moura

# import system which operates the game.
import random

# define words chosen and return into system.
def choose_random_word():
    words = ["ball", "club", "spider", "team", "friend", "nominee", "host"]
    return random.choice(words)

# define and set display for letters of words guessed.
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# define and create the hangman image (progresses with incorrect guesses).
def draw_hangman(incorrect_guesses):
    hangman_display = [
                # clean slate
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """, ]
    
    print(hangman_display[incorrect_guesses])

# create limitations and rules to guesses.
def main():
    max_chances = 6
    incorrect_guesses = 0
    guessed_letters = []
    word_to_guess = choose_random_word()
    hidden_word = "_" * len(word_to_guess)

# print outputs to user inputs and results of choices made.
    print("Welcome to Caleb's Hangman!")
    print("Try to guess the word.")
    print(display_word(hidden_word, guessed_letters))

    while max_chances > 0 and hidden_word != word_to_guess:
        guess = input("Enter a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("This letter has been guessed. Try again.")
            elif guess in word_to_guess:
                print("Nice guess!")
                guessed_letters.append(guess)
            else:
                print("Guess is Incorrect. Try again.")
                guessed_letters.append(guess)
                max_chances -= 1
                incorrect_guesses += 1
        else:
            print("Invalid input. Enter only one letter.")

# hangman image reveals when an incorrect guess is made.
        draw_hangman(incorrect_guesses)
        print("Chances left:", max_chances)
        print(display_word(word_to_guess, guessed_letters))

    if hidden_word == word_to_guess:
        print("Congratulations! You have correctly guessed the word:", word_to_guess)
    else:
        print("You have no guesses left. The correct word was:", word_to_guess)

if __name__ == "__main__":
    main()
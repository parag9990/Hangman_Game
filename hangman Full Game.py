import os  # Operating System Module
import random  # Random Module
import hangman_art  # Another file
import hangman_words  # Another file
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game = False
lives = 6

print(hangman_art.logo)

# Testing code (Solution)
# print(f'Hence, the solution is {chosen_word}.')

# Create blanks
display = []
for i in range(word_length):
    display += "_"

while not game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')  # on windows
    if guess in display:
        print(f'You Have Already Guessed this Letter {guess}')

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You Guessed: {guess}, that's not in the Word, You Lose a Life")
        lives -= 1
        if lives == 0:
            game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        game = True
        print("You win.")

    print(hangman_art.stages[lives])

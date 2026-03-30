import random
from itertools import repeat

from hangman_words import word_list
from hangman_art import stages,logo
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

lives = 6

name = input("Please enter your name to begin: \n").title()
print(logo)
print(f"Hello & welcome to Hangman, {name}.\n")

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
incorrect_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

    while len(guess) != 1 or guess not in alphabets :
        print("Invalid Input. Please enter a single letter only.")
        guess = input("Guess a letter: ").lower()


    if guess in correct_letters:
        print(f"You have already guessed {guess}.")
    elif guess in incorrect_letters:
        print(f"You have already guessed {guess}, and it is incorrect. No lives lost.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word and guess not in incorrect_letters:
        lives -= 1
        incorrect_letters.append(guess)
        print(f"You guessed {guess} - Incorrect guess hence you lose a life")

        if lives == 0:
            game_over = True
            print(f"It was {chosen_word}!"
                  f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print(f"Congratulations! You guessed the word correctly, '{chosen_word}' "
              "****************************YOU WIN****************************")

    if not game_over:
        print(stages[lives])
from hangman_art import stages, logo
import os
import hangman_words
import random

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
#To check solution
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')  #<--- This might not be clearing the screen after every guess

    if guess in display:
      print(f"You've already typed {guess}. Try again.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f'The letter "{guess}" is not in the word.')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
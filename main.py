# Python program to create hangman game

# Importing module required for randomization.
import random
# Importing module that contains art for game.
import hangman_art as art
# Importing module that contains list of words.
import hangman_words as words

# Create variable for list of words
word_list = words.word_list

# Generate a random word using the random module
chosen_word = random.choice(word_list)

# Variable containing length of word generated
word_length = len(chosen_word)

# Variable containing boolean value to indicate the game is still running
end_of_game = False

# Variable containing number of lives player has at the beggining of game
lives = 6

#Print hangman logo.
print(art.logo)

# List that would contain correct guesses
display = []

#Create blanks inside display list.
for _ in range(word_length):
    display += "_"

# While loop so the game keeps running till player has won.
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #To check if letter has been guessed already.
    if guess in display:
        print(f"You entered {guess} already")

    #Check guessed letter.
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life")
        lives -= 1
        #Check if there are no more lives left.
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters and won game.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Print each stage of the hangman respective to the number of lives left.
    print(art.stages[lives])

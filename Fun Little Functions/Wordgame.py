import getpass

# Get player 1's word in a 'secret' way
word = getpass.getpass("Player 1: Enter your secret word: >>> ")
word = word.upper()

# Create a list that has the same amount of "blank spaces" as the length of Player 1's word:
blank_spaces = "_"
empty_word = []
for chars in word:
    empty_word += blank_spaces
print(empty_word)

# Initialize some helpful variables for our game
guesses = 0
guesses_left = 6
incorrect_guesses = []
 
while blank_spaces in empty_word and guesses_left > 0:
# Main loop - Game only keeps running while BOTH things are true:
# 1) There ARE blank spaces in the game board
# 2) Player 2 still has some guesses left
    
    #Player 2 guesses:
    player_2_guess = input("\nGuess a letter: ")
    player_2_guess = player_2_guess.upper()
    # Assume guess is incorrect until we find the letter
    for index, char in enumerate(word):
        if player_2_guess in char:
            empty_word[index] = player_2_guess
    print('\n',empty_word)

    if player_2_guess not in word:
        guesses_left -= 1
        incorrect_guesses.append(player_2_guess)
    print("\nYou have", guesses_left, "guesses left")
    print("\nIncorrect guesses:", incorrect_guesses)
if guesses_left == 0:
    print("\nPlayer 1 lost! The word was:", word)
else:   
    print("\nPlayer 1 wins!")


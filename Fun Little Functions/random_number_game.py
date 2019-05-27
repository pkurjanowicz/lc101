import random
print("Welcome to the random number game!" + "\n")
print("You will have 3 tries to guess a number between 1 and 10")
random_number = random.randint(1,10)
guess_count = 3
wrong_guess_string = ""
game_over = False
while guess_count != 0 and game_over == False:
    user_guess = input("Please guess a number: ")
    if user_guess.isalpha():
        print("The character must be a number")
    else:
        user_guess_int = int(user_guess)
        if user_guess_int != random_number:
            guess_count -= 1
            wrong_guess_string += "[" + str(user_guess_int) + "] "
            print("Guess count =", guess_count)
            print("Wrong guesses =", wrong_guess_string, "\n" "Please guess again!")
            if guess_count == 0:
                game_over = True
                print("Game over, you loose! The random number was", random_number)
        if user_guess_int == random_number:
            game_over = True
            print("Congrats, you won!")
        


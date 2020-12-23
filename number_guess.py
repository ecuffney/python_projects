# Number Guessing Project

import random

number_of_attempts = []

def show_score():
    if len(number_of_attempts) <= 0:
        print ("You are the first to play, good luck!")
    else:
        print ("The current high score is {} attempts" .format(min(number_of_attempts)))

def play_game():
    random_number = int(random.randint(1,20))
    print ("Greetings traveler! Welcome to the number guess game!")
    player_name = input("What is your name?")
    ask_to_play = input("Hi, {} Would you like to play? (Enter yes or no) ".format(player_name))
    attempts = 0
    show_score()
    while ask_to_play.lower() == "yes":
        try:
            guess = input ("Pick a number between 1 and 20:")
            if int(guess) < 1 or int(guess) > 20:
                raise ValueError ("Please pick a number between 1 and 20")
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                number_of_attempts.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter yes or no) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1,20))
                if play_again.lower() == "no":
                    print ("No worries, goodbye!")
                    break
            elif int(guess) > random_number:
                print ("It is lower")
                attempts += 1
            elif int(guess) < random_number:
                print ("It is higher")
                attempts += 1
        except ValueError as err:
            print("Aye dios mio! That is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print ("No worries. Maybe next time!")
if __name__ == '__main__':
    play_game()

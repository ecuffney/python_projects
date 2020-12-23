import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(3)


def intro():
    print_pause("You find yourself standing in a capitalist hellscape: a "
                "factory.")
    print_pause("Broken bodies of machinery lay like shucked "
                "caccoons over the smog-choked wasteland.")
    print_pause(' ')
    print_pause("Rumor has it there is a wicked boss around here "
                "that has been exploiting the workers in this factory:")
    print_pause("Stealing the surplus value of thier labor and pocketing the "
                "profits!")
    print_pause(' ')
    print_pause("You worry that you will also be swindled out of the full "
                "value of your work.")
    print_pause("Something must be done.")
    print_pause(' ')
    print_pause("Up the rust-eaten stairs ahead of you there is a door.")
    print_pause("Far off to your right you see a group of fellow workers "
                "huddled in a corner.")
    print_pause(' ')


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def choose_adventure(items):
    response = valid_input("Where would you like to go?\n"
                           "Press 1 to go up the stairs.\n"
                           "Press 2 to approach the workers.\n",
                           "1", "2")
    if response == '1':
        choose_stairs(items)
    elif response == '2':
        choose_workers(items)


def choose_stairs(items):
    print_pause("You start to climb the stairs.")
    print_pause("They groan beneath your weary feet.")
    print_pause("After a few moments, you find "
                "yourself in the bosses office.")
    if "solidarity" in items:
        print_pause(' ')
        print_pause("The boss is horrified!")
        print_pause("You and your fellow workers have united in solidarity.")
        print_pause("The entire factory gets a raise!")
        print_pause("You have won the game.")
        play_again(items)
    else:
        print_pause("You demand a raise.")
        print_pause("The boss laughs you out of the office.")
        print_pause(' ')
        print_pause("It seems you cant stand up to him without uniting "
                    "with your fellow workers.")
        print_pause("You head back down the stairs to the factory floor.")
        try_again(items)


def choose_workers(items):
    print_pause("You make your way over to your fellow employees.")
    print_pause("They are having a heated discussion concering how "
                "little they are paid.")
    print_pause(' ')
    print_pause("They ask you to join a union to protect everyone in the "
                "factory.")
    print_pause("But nothing can be acheived until someone confronts "
                "the boss.")
    print_pause(' ')
    confront_boss(items)


def dice_roll(items):
    roll = (random.randint(1, 6))
    print(roll)
    if roll > 3:
        engels_boss(items)
    elif roll < 4:
        print_pause("You rolled lower than Engels.")
        meet_boss(items)


def confront_boss(items):
    print_pause("No one seems willing to confront the factory owner.")
    print_pause("You roll a die to see who must confront him.")
    print_pause("If you a roll a 3 or higher your co-worker Engels must do "
                "the deed.")
    print_pause("Otherwise it will you heading up those stairs.")
    print_pause("You roll the dice:")
    print_pause(" ")
    dice_roll(items)


def engels_boss(items):
    print_pause("Engels loses. He must confront the boss.")
    print_pause("He leaves to do so.")
    print_pause("He returns shortly, looking downtrodden.")
    print_pause("It seems poor Engels doesnt have the gumption to stand up "
                "to the boss.")
    print_pause("With no one else with the sand to do the job:")
    print_pause(" ")
    meet_boss(items)


def meet_boss(items):
    print_pause("The workers elect you as the voice of the people!")
    response = valid_input("Do you agree like to join the union and confront "
                           "the boss?\n"
                           "Please say 'yes' or 'no'.\n",
                           "yes", "no")
    if "yes" in response:
        print_pause("You accept.")
        print_pause("Workers of the world, UNITE!")
        print_pause("You head back to the factory floor.")
        items.append("solidarity")
        choose_adventure(items)
    elif "no" in response:
        print_pause("Minimum wage it is!")
        print_pause("Better luck next time. Goodbye!")
        play_again(items)


def try_again(items):
    response = valid_input("Would you like to try again and keep the full "
                           "value of your labor?"
                           "Please say 'yes' or 'no'.\n",
                           "yes", "no")
    if "no" in response:
        print_pause("Minimum wage it is!")
        print_pause("Better luck next time. Goodbye!")
    elif "yes" in response:
        print_pause("Lets do it. We have nothing to lose but our chains!")
        choose_adventure(items)


def play_again(items):
    response = valid_input("Would you like to play again? "
                           "Please say 'yes' or 'no'.\n",
                           "yes", "no")
    if "no" in response:
        print_pause("What a day!")
        print_pause("Goodbye!")
    elif "yes" in response:
        print_pause("Another day, another dollar.")
        play_game()


def play_game():
    items = []
    intro()
    choose_adventure(items)

play_game()

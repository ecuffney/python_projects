#!/usr/bin/env python3

import random
import time


##This program plays a game of Rock, Paper, Scissors between two Players,
##and reports both Player's scores each round.

moves = ['rock', 'paper', 'scissors']


def print_pause(message): #adds pause when printing for better game feel
    print(message)
    time.sleep(1)


class Player:
    def move(self):
        return self.move

class RandomPlayer():
    def __init__(self):
        Player.__init__(self)
    def move(self):
        return random.choice(moves)

class HumanPlayer():
    def __init__(self):
        Player.__init__(self)
    def move(self):
        while True:
            HumanPlayer = input("Please choose 'Rock', 'Paper', or 'Scissors': ")
        #Detect invalid entry
            if HumanPlayer.lower() not in moves:
                print('Please choose Paper, Rock or Scissors: ')
            else:
                break
        return HumanPlayer

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, HumanPlayer, RandomPlayer):
        self.p1 = HumanPlayer
        self.p2 = RandomPlayer
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"You played {move1}. ")
        print_pause(f"Computer played {move2}. ")
        if move1 == move2:
            print_pause("Its's a tie.")
        elif beats(move1, move2):
            print_pause("YOU WIN!")
            self.p1_score += 1
        else:
            print_pause("COMPUTER WINS.")
            self.p2_score += 1
        print(f"Score: Player 1: {self.p1_score}). Player 2: {self.p2_score}")

    def play_game(self):
        print_pause("Game start!")
        for round in range(4):
            print(f"Round {round}:")
            self.play_round()
        print_pause("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()

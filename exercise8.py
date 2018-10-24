#!/usr/bin/env python
__author__ = 'gonzalo.sanchter@gmail.com'


def play(player1, player2):
    
    if player1 == player2:
        print("It's a TIE!")
    if player1 == "rock":
        if player2 == "scissors":
            print("Player 1 WINS!")
        elif player2 == "paper":
            print("Player 2 WINS!")
    elif player1 == "scissors":
        if player2 == "rock":
            print("Player 2 WINS!")
        elif player2 == "paper":
            print("Player 1 WINS!")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 WINS!")
        elif player2 == "scissors":
            print("Player 2 WINS!")



quit = False

while (quit != True):

    print("Player 1, enter your move (rock, paper, scissors) :")
    u1 = input("> ")
    print("Player 2, enter your move (rock, paper, scissors) :")
    u2 = input("> ")

    play(u1, u2)
    
    print("Do you want continue? (y/n)")
    r = input("> ")

    if r == "n":
        quit = True

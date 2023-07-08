"""
    File: gamble.py
    Author: Lucas Arena
    Date: 1/22/2022
    Purpose: Defines a chips class and a few functions to help with the game
"""


class Chips:
    # Starting chips is 100
    def __init__(self, total=100):
        self.total = total
        self.bet = 0
        self.winnings = 0

    def win_bet(self):
        self.total += self.bet
        self.winnings += self.bet

    def lose_bet(self):
        self.total -= self.bet
        self.winnings -= self.bet


def take_bet(chips):
    # Ask for a bet until a valid bet is given
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?: "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print(
                    f"Sorry, you do not have enough chips! You have: {chips.total}")
            else:
                break


def play_again(chips):

    print(f"You currently have {chips.total} chips.")

    # Win game if you have 500 chips, lose if you have 0 chips
    if chips.total <= 0:
        print("You have no more chips!")
        return False
    if chips.total >= 500:
        print("You have won the game!")
        return False

    # Ask if you want to play again
    print("Would you like to play again?")
    command = input("Yes or no? (y/n): ")

    if command == "y" or command == "yes":
        print(f"You have {chips.total} chips.")
        return chips
    if command == "n" or command == "no":
        return False
    else:
        print("Please enter a valid command.")
        return play_again(chips)

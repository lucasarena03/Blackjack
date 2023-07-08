"""
    File: main.py
    Author: Lucas Arena
    Date: 1/22/2022
    Purpose: Defines the main function for the game
"""

from deck import Deck
from card import Card, Suit
from hand import Hand
from gamble import Chips, take_bet, play_again
import os
import time
import random


def print_hands(dealer_hand: Hand, player_hand: Hand, reveal_dealer: bool = False) -> None:
    # only works on windows
    os.system("cls")

    print("Dealer's Hand:")
    print(dealer_hand.cards[0])

    # Dealer's hand with 1 card hidden
    if reveal_dealer:
        for card in dealer_hand.cards[1:]:
            print(card)
        print(f"Dealer hand value: {dealer_hand.get_value()}")
    else:
        print("Hidden Card")
        print(f"Dealer hand value: {dealer_hand.cards[0].get_value()}")

    print()

    print("Player's Hand:")
    for card in player_hand.cards:
        print(card)
    print(f"Player hand value: {player_hand.get_value()}")


def main(chips: Chips) -> None:
    random.seed()

    take_bet(chips)

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    # initialize player with 2 cards and dealer with 2 and 1 card hidden
    dealer_hand.add_card(deck.get_next_card())
    player_hand.add_card(deck.get_next_card())
    player_hand.add_card(deck.get_next_card())
    dealer_hand.add_card(deck.get_next_card())
    print_hands(dealer_hand, player_hand, reveal_dealer=False)

    # check for blackjack on first deal
    if player_hand.get_value() == 21:
        print_hands(dealer_hand, player_hand, reveal_dealer=True)
        print("You win!")
        chips.win_bet()
        return play_again(chips)

    if dealer_hand.get_value() == 21:
        print_hands(dealer_hand, player_hand, reveal_dealer=True)
        print("Dealer wins!")
        chips.lose_bet()
        return play_again(chips)

    # Main game loop
    while True:
        # print game system
        print_hands(dealer_hand, player_hand, reveal_dealer=False)

        # check for bust
        if player_hand.get_value() > 21:
            print_hands(dealer_hand, player_hand, reveal_dealer=True)
            print("You bust!")
            chips.lose_bet()
            return play_again(chips)
        if dealer_hand.get_value() > 21:
            print_hands(dealer_hand, player_hand, reveal_dealer=True)
            print("Dealer bust!")
            chips.win_bet()
            return play_again(chips)

        print()

        # allow player to hit or stand
        command = input("Hit or stand? (h/s/hit/stand): ")
        if command == "h" or command == "hit":
            player_hand.add_card(deck.get_next_card())
        elif command == "s" or command == "stand":
            break

    # dealer hits if value is less than 17
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.get_next_card())

        # print game status
        print_hands(dealer_hand, player_hand, reveal_dealer=True)

        time.sleep(2.5)

    # check final scores
    if dealer_hand.get_value() > 21:
        print_hands(dealer_hand, player_hand, reveal_dealer=True)
        print("Dealer bust!")
        print("You win!")
        chips.win_bet()
        return play_again(chips)
    elif dealer_hand.get_value() > player_hand.get_value():
        print_hands(dealer_hand, player_hand, reveal_dealer=True)
        print("Dealer wins!")
        print("You lose!")
        chips.lose_bet()
        return play_again(chips)
    elif dealer_hand.get_value() < player_hand.get_value():
        print_hands(dealer_hand, player_hand, reveal_dealer=True)
        print("You win!")
        print("Dealer loses!")
        chips.win_bet()
        return play_again(chips)
    else:
        print_hands(dealer_hand, player_hand, reveal_dealer=True)
        print("Tie!")
        chips.lose_bet()
        return play_again(chips)

        # Game rules ->
        # > 21 = bust
        # 21 = blackjack
        # dealers hit on < 17
        # dealer wins ties


if __name__ == "__main__":
    chips = Chips()
    print("Welcome to Blackjack!")
    print()
    print("You start with 100 chips. Good luck!")
    while main(chips):
        pass

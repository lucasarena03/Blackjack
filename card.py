"""
    File: card.py
    Author: Lucas Arena
    Date: 1/22/2022
    Purpose: Defines a card class and a suit enum
"""

from enum import Enum


class Suit(Enum):
    HEARTS = 1
    DIAMONDS = 2
    SPADES = 3
    CLUBS = 4


class Card:

    # Card rrequires a suit and a value
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value

    def get_value(self) -> int:
        # Ace is 11
        if self.value == 1:
            return 11
        if self.value >= 10:
            return 10
        return self.value

    # Convert a card object to a string to print to consoole
    def __str__(self) -> str:
        value_str = ""

        if self.value == 1:
            value_str = "Ace"
        elif self.value == 11:
            value_str = "Jack"
        elif self.value == 12:
            value_str = "Queen"
        elif self.value == 13:
            value_str = "King"
        else:
            value_str = str(self.value)

        suit_str = ""

        if self.suit == Suit.HEARTS:
            suit_str = "♥"
        elif self.suit == Suit.DIAMONDS:
            suit_str = "♦"
        elif self.suit == Suit.SPADES:
            suit_str = "♣"
        elif self.suit == Suit.CLUBS:
            suit_str = "♠"

        return f"{value_str} of {suit_str}"

"""
    File: deck.py
    Author: Lucas Arena
    Date: 4/14/2021
    Purpose: Defines a deck object and a suit enum
"""

from card import Card, Suit
import random


class Deck:

    def __init__(self) -> None:
        self.cards = []
        self.card_index = 0

        # Generate a full deck of cards
        for suit in Suit:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    # Shuffle a deck of cards
    def shuffle(self) -> None:
        self.card_index = 0
        random.shuffle(self.cards)

    def get_next_card(self) -> Card:
        card = self.cards[self.card_index]
        self.card_index += 1
        return card

    def __str__(self) -> str:
        deck = ""

        for card in self.cards:
            deck += f"{card}\n"

        return deck

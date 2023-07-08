"""
    File: hand.py
    Author: Lucas Arena
    Date: 1/22/2022
    Purpose: Stores cards and their values as a hand
"""


class Hand:
    def __init__(self) -> None:
        self.cards = []

    def add_card(self, card) -> None:
        self.cards.append(card)

    def get_value(self) -> int:
        value = 0
        for card in self.cards:
            value += card.get_value()
        return value

    def __str__(self) -> str:
        hand = ""

        for card in self.cards:
            hand += f"{card}\n"

        return hand

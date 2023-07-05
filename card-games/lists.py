"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""
JACK_VALUE = 11


def get_rounds(number):
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    average = card_average(hand)

    middle_card = get_middle_card(hand)
    first_last_average = get_first_last_average(hand)

    return average in (first_last_average, middle_card)


def get_first_last_average(hand):
    return (hand[0] + hand[-1]) / 2


def get_middle_card(hand):
    return hand[len(hand) // 2]


def average_even_is_average_odd(hand):
    even_cards = hand[::2]
    odd_cards = hand[1::2]
    return card_average(even_cards) == card_average(odd_cards)


def maybe_double_last(hand):
    if hand[-1] == JACK_VALUE:
        hand[-1] *= 2
    return hand

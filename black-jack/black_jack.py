"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

FACE_CARDS = ['J', 'Q', 'K']
ACE = 'A'
MAX_HAND_VALUE = 21
HIGH_VALUE_ACE = 11
LOW_VALUE_ACE = 1
FACE_CARD_VALUE = 10
DOUBLE_DOWN_HAND_VALUES = [9, 10, 11]


# Ace always 1 here
def value_of_card(card):
    if is_ace(card):
        return LOW_VALUE_ACE
    if is_face(card):
        return FACE_CARD_VALUE
    return int(card)


def higher_card(card_one, card_two):
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value > card_two_value:
        return card_one
    if card_two_value > card_one_value:
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    would_cause_to_bust = is_bust([card_one, card_two, HIGH_VALUE_ACE])

    if would_cause_to_bust or has_ace([card_one, card_two]):
        return LOW_VALUE_ACE
    return HIGH_VALUE_ACE


def is_blackjack(card_one, card_two):
    hand = [card_one, card_two]
    return has_ace(hand) and has_10_value(hand)


def can_split_pairs(card_one, card_two):
    return value_of_card(card_one) is value_of_card(card_two)


def can_double_down(card_one, card_two):
    return sum_of([card_one, card_two]) in DOUBLE_DOWN_HAND_VALUES


def has_ace(cards):
    return 'A' in cards


def has_face(cards):
    for card in cards:
        if is_face(card):
            return True
    return False


def is_ace(card):
    return card == 'A'


def is_face(card):
    return card in FACE_CARDS


def has_10_value(cards):
    return '10' in cards or has_face(cards)


def is_bust(cards):
    return sum_of(cards) > MAX_HAND_VALUE


def sum_of(cards):
    return sum(value_of_card(card) for card in cards)

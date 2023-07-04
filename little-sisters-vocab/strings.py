"""Functions for creating, transforming, and adding prefixes to strings."""
import re

ADJECTIVES = ['bright', 'dark', 'hard', 'soft',
              'light', 'damp', 'short', 'weak', 'black']


def add_prefix_un(word):
    return "un" + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    join_sequence = " :: "
    prefixed_words = map(lambda word: prefix + word, vocab_words[1:])

    return prefix + join_sequence + join_sequence.join(prefixed_words)


def remove_suffix_ness(word):
    with_possible_i = remove_trailing_ness(word)
    return change_trailing_i_to_y(with_possible_i)


def remove_trailing_ness(word):
    return re.sub(r"ness$", "", word)


def change_trailing_i_to_y(with_possible_i):
    return re.sub(r"i$", "y", with_possible_i)


def adjective_to_verb(sentence, index):
    raw_adjective = word_at_index(index, sentence)
    cleaned_adjective = remove_periods(raw_adjective)
    return cleaned_adjective + "en"


def word_at_index(index, sentence):
    split_sentence = sentence.split()
    return split_sentence[index]


def remove_periods(word):
    return re.sub("[.]", "", word)

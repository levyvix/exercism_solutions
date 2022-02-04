import numpy as np


def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return np.mean(hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """

    return np.mean(hand) in [np.mean(hand[::len(hand)-1]), np.median(hand[1:-1])]


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    return np.mean(hand[::2]) == np.mean(hand[1::2])


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    return hand[:-1] + [22] if hand[-1] == 11 else hand


print(approx_average_is_average([1, 2, 3]))
print(approx_average_is_average([2, 3, 4, 8, 8]))


hand = [2, 3, 4, 8, 8]
print(np.mean(hand[::len(hand)-1]))
print(np.median(hand[1:-1]))


text = 'Print only the words that start with s in this sentence'


print([word for word in text.split(' ') if word.startswith('s')])


print(list(range(0, 10, 2)))

print([x for x in range(50) if x % 3 == 0])

text2 = 'Print every word in this sentence that has an even number of letters'

print([f'{word} é Par' for word in text2.split(' ') if len(word) % 2 == 0])

print('\n')
# fizz buzz - print numbers from 1 to 100.
print(["FizzBuzz" if number % 3 == 0 and number % 5 == 0 else "Fizz" if number %
      3 == 0 else "Buzz" if number % 5 == 0 else number for number in range(1, 101)])

text3 = 'Create a list of the first letters of every word in this string'
print([word[0] for word in text3.split(' ')])

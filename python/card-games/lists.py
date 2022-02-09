
# TODO convert np mean to mean function

def mean(hand):
    """

    :param hand: list - cards in hand.
    :return: float - mean value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def median(hand):
    """

    :param hand: list - cards in hand.
    :return: float - median value of the cards in the hand.
    """

    return sorted(hand)[len(hand) // 2]


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

    return mean(hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """

    return mean(hand) in [mean(hand[::len(hand)-1]),  median(hand[1:-1])]


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    return mean(hand[::2]) == mean(hand[1::2])


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    return hand[:-1] + [22] if hand[-1] == 11 else hand

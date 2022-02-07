def get_coordinate(record):
    """
    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """
    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """

    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """

    coordinate_azara = tuple(azara_record[1])
    coordinate_rui = rui_record[1]

    return all(x == y for x, y in zip(coordinate_azara, coordinate_rui))


def create_record(azara_record, rui_record):
    """
    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """

    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    """
    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """
    return "".join(
        f"{c[:1] + c[2:]}\n" for c in combined_record_group
    )

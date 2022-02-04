code = {
    'Black': 0,
    'Brown': 1,
    'Red': 2,
    'Orange': 3,
    'Yellow': 4,
    'Green': 5,
    'Blue': 6,
    'Violet': 7,
    'Grey': 8,
    'White': 9
}


def color_code(color):
    return code[color.title()]


def colors():
    return [key.lower() for key, item in code.items()]

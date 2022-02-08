from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """

    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """

    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """

    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")

    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    """

    for alcohol in ALCOHOLS:
        if alcohol in drink_ingredients:
            return f"{drink_name} Cocktail"

    return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """

    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    """

    # check vegan
    if all(item in VEGAN for item in dish_ingredients):
        return f"{dish_name}: VEGAN"

    # check vegetarian
    if all(item in VEGETARIAN for item in dish_ingredients):
        return f"{dish_name}: VEGETARIAN"

    # check paleo
    if all(item in PALEO for item in dish_ingredients):
        return f"{dish_name}: PALEO"

    # check keto
    if all(item in KETO for item in dish_ingredients):
        return f"{dish_name}: KETO"

    # check omnivore
    if all(item in OMNIVORE for item in dish_ingredients):
        return f"{dish_name}: OMNIVORE"


def tag_special_ingredients(dish):
    """

    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
    special_ingredients = [d for d in dish[1] if d in SPECIAL_INGREDIENTS]

    return tuple([dish[0], set(special_ingredients)])


def compile_ingredients(dishes):
    """

    :param dishes: list of dish ingredient sets
    :return: set

    This function should return a `set` of all ingredients from all listed dishes.
    """

    return {ing for dish in dishes for ing in dish}


def separate_appetizers(dishes, appetizers):
    """

    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    return {d for d in dishes if d not in appetizers}


def singleton_ingredients(dishes, intersection):
    """
    :param dishes:  list of ingredient sets
    :param intersection: constant - one of (VEGAN_INTERSECTION,VEGETARIAN_INTERSECTION,PALEO_INTERSECTION,
                                            KETO_INTERSECTION,OMNIVORE_INTERSECTION)

    :return: set of singleton ingredients

    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    """

    # find the count of evey ingredient in the dishes
    ingredient_count = {}
    for dish in dishes:
        for ing in dish:
            if ing in ingredient_count:
                ingredient_count[ing] += 1
            else:
                ingredient_count[ing] = 1

    # return the intersection of the singleton ingredients and the intersection
    return {
        key for key, value in ingredient_count.items() if value == 1
    }

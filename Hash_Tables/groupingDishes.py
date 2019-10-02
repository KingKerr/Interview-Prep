"""
You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish, followed by all the ingredients used in preparing it.
You want to group the dishes by ingredients, so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

Return an array where each element is a list beginning with the ingredient name, followed by the names of all the dishes that contain this ingredient.
The dishes inside each list should be sorted lexicographically, and the result array should be sorted lexicographically by the names of the ingredients.

"""

def groupingDishes(dishes):
    results = []

    dish_ingredients = dict()

    for dish in dishes:
        main_dish = dish[0]

        for x, ingredient in enumerate(dish):
            if x:
                try:
                    dish_ingredients[ingredient].add(main_dish)
                except:
                    dish_ingredients[ingredient] = set()
                    dish_ingredients[ingredient].add(main_dish)
        for ingredient in sorted(dish_ingredients.keys()):
            entry = [ingredient]
            for main_dish in sorted(dish_ingredients[ingredient]):
                entry.append(main_dish)
            if len(entry) > 2:
                results.append(entry)
        return results

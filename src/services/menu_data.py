# # Req 3
# class MenuData:
#     def __init__(self, path: str) -> None:
#         pass

import csv
import os.path
from typing import Set
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = os.path.abspath(source_path)
        self.dishes: Set[Dish] = set()
        self._load_menu_data()

    def _load_menu_data(self):
        with open(self.source_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            current_dish = None
            for row in reader:
                dish_name = row["dish"]
                price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                if current_dish is None or current_dish.name != dish_name:
                    current_dish = Dish(dish_name, price)
                    self.dishes.add(current_dish)

                ingredient = Ingredient(ingredient_name)
                current_dish.add_ingredient_dependency(
                    ingredient, recipe_amount
                )

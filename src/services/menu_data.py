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
        dishes_dict = {}  # Dicionário para armazenar os pratos criados

        with open(self.source_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dish_name = row["dish"]
                price = float(row["price"])
                ingredient_name = row["ingredient"]
                recipe_amount = int(row["recipe_amount"])

                # Verifica se o prato já foi criado
                if dish_name in dishes_dict:
                    # Se existir o prato, adiciona novo ingrediente à receita
                    dish = dishes_dict[dish_name]
                    ingredient = Ingredient(ingredient_name)
                    dish.add_ingredient_dependency(ingredient, recipe_amount)
                else:
                    # Se o prato ainda não foi criado, cria e adiciona ao dict
                    dish = Dish(dish_name, price)
                    ingredient = Ingredient(ingredient_name)
                    dish.add_ingredient_dependency(ingredient, recipe_amount)
                    dishes_dict[dish_name] = dish

        # Ao final, adiciona os pratos do dicionário ao conjunto
        self.dishes.update(dishes_dict.values())

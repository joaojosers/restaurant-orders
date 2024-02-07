from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction=None) -> List[Dict]:
        main_menu = []

        # Obtém todos os pratos do cardápio
        dishes = self.menu_data.dishes

        # Filtra os pratos de acordo com a restrição, se houver
        if restriction:
            dishes = [
                dish
                for dish in dishes
                if restriction not in dish.get_restrictions()
            ]

        # Verifica a disponibilidade dos ingredientes em estoque
        available_dishes = [
            dish
            for dish in dishes
            if self.inventory.check_recipe_availability(dish.recipe)
        ]

        # Constrói a lista de dicionários para o cardápio
        for dish in available_dishes:
            dish_dict = {
                "dish_name": dish.name,
                "ingredients": [
                    ingredient for ingredient in dish.get_ingredients()
                ],
                "price": dish.price,
                "restrictions": [
                    restriction for restriction in dish.get_restrictions()
                ],
            }
            main_menu.append(dish_dict)

        return main_menu

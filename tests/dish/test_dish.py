import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient


def test_dish():
    # Testando a inicialização correta do prato
    dish = Dish("Lasanha", 25.99)
    assert dish.name == "Lasanha"
    assert dish.price == 25.99
    assert dish.recipe == {}

    # Testando o método __repr__
    assert repr(dish) == "Dish('Lasanha', R$25.99)"

    # Testando a adição de ingredientes na receita
    ingrediente1 = Ingredient("Queijo")
    ingrediente2 = Ingredient("Molho de Tomate")
    dish.add_ingredient_dependency(ingrediente1, 200)
    dish.add_ingredient_dependency(ingrediente2, 300)
    assert dish.recipe == {ingrediente1: 200, ingrediente2: 300}

    # Testando o método get_restrictions
    assert dish.get_restrictions() == set()

    # Testando o método get_ingredients
    assert dish.get_ingredients() == {ingrediente1, ingrediente2}

    # Testando a igualdade entre pratos
    dish2 = Dish("Lasanha", 25.99)
    assert dish == dish2

    # Testando se pratos diferentes possuem hashes diferentes
    assert hash(dish) == hash(dish2)
    dish3 = Dish("Pizza", 15.99)
    assert hash(dish2) != hash(dish3)

    # Testando se a comparação de igualdade de pratos diferentes é falsa
    dish3 = Dish("Pizza", 15.99)
    assert dish != dish3

    # Testando se a comparação de igualdade de pratos iguais é verdadeira
    assert dish == dish

    # Testando a exceção TypeError ao tentar criar um prato com preço inválido
    with pytest.raises(TypeError):
        Dish("Lasanha", "25.99")

    # Teste exceção ValueError ao criar prato com preço menor ou igual a zero
    with pytest.raises(ValueError):
        Dish("Lasanha", 0)
        Dish("Lasanha", -10.99)

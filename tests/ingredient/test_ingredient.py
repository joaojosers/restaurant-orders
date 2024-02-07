from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    # Teste para garantir que a classe pode ser instanciada corretamente
    ingredient = Ingredient("queijo mussarela")
    assert isinstance(ingredient, Ingredient)

    # Teste para garantir que restrictions é populado como esperado
    assert ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    # Teste se o método mágico __repr__ funcione como esperado
    assert repr(ingredient) == "Ingredient('queijo mussarela')"

    # Teste se o método mágico __eq__ funcione como esperado
    same_ingredient = Ingredient("queijo mussarela")
    assert ingredient == same_ingredient

    # Teste se o método mágico __hash__ funcione como esperado
    different_ingredient = Ingredient("farinha")
    assert hash(ingredient) != hash(different_ingredient)
    assert hash(same_ingredient) == hash(ingredient)

    # Teste se comparação de igualdade de dois ingredientes iguais é verdadeira
    assert ingredient == same_ingredient

    # Teste se comparação de igualdade de dois ingredientes diferentes é falsa
    assert ingredient != different_ingredient

    # Teste se atributo name de um ingrediente é igual ao passado ao construtor
    assert ingredient.name == "queijo mussarela"

    # Teste se restrictions de um ingrediente contenha os valores corretos
    assert Restriction.LACTOSE in ingredient.restrictions
    assert Restriction.ANIMAL_DERIVED in ingredient.restrictions

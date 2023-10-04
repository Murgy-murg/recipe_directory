from lib.recipe import Recipe
def test_constructor_returns_requested_values():
    recipe = Recipe(2, 'tasty risotto', 40, 4) 
    assert recipe.id == 2
    assert recipe.name == 'tasty risotto'
    assert recipe.cooking_time == 40
    assert recipe.rating == 4

def test_equality():
    recipe1 = Recipe(2, 'tasty risotto', 40, 4)
    recipe2 = Recipe(2, 'tasty risotto', 40, 4)
    assert recipe1 == recipe2

def test_format():
    recipe1 = Recipe(2, 'tasty risotto', 40, 4)
    assert str(recipe1) == 'Recipe(2, tasty risotto, 40, 4)'
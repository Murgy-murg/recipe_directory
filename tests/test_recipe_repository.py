from lib.recipe import Recipe
from lib.recipe_repository import RecipeRepository
def test_all_returns_all_values_in_table(db_connection):
    db_connection.seed('seeds/recipes.sql')
    recipe = RecipeRepository(db_connection)
    result = recipe.all()
    assert result == [
        Recipe(1,'Roast dinner', 80, 5),
        Recipe(2,'Asparagus risotto', 40, 4),
        Recipe(3,'Chilli con carne', 50, 3),
        Recipe(4,'Leek and bean stew', 45, 4),
        Recipe(5,'Loaded sweet potato', 60, 1)
        ]
    
def test_return_row_dependent_on_given_id(db_connection):
    db_connection.seed('seeds/recipes.sql')
    recipe = RecipeRepository(db_connection)
    result = recipe.find(2)
    assert result == Recipe(2,'Asparagus risotto', 40, 4)

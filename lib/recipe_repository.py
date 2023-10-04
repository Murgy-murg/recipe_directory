from lib.recipe import Recipe
class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        all_recipes = []
        rows = self._connection.execute('SELECT * FROM recipes')
        for row in rows:
            r = Recipe(row['id'], row['name'], row['cooking_time'], row['rating'] )
            all_recipes.append(r)
        return all_recipes
    
    def find(self, id):
        row = self._connection.execute('SELECT * FROM recipes WHERE id=%s', [id])[0]
        return Recipe(row['id'], row['name'], row['cooking_time'], row['rating'] )

    

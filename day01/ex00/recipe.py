

class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		assert int(cooking_lvl) >= 1 and int(cooking_lvl) <= 5, "Cooking level must be between 1 and 5"
		assert int(cooking_time) >= 0, "Cooking time can't be negative"
		assert str(recipe_type) == "lunch" or str(recipe_type) == "lunch" or str(recipe_type) == "lunch", "wrong recipe type"
		assert len(name) > 0 and len(ingredients) > 0, "empty argument"
		self.name = str(name)
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type
	
	def __str__(self):
		'''Return the string to print with the recipe info'''
		txt = ""
		txt += "recipe's name is: {}\n".format(self.name)
		txt += "recipe's coocking level is: {}\n".format(self.cooking_lvl)
		txt += "recipe's cooking time is: {}\n".format(self.cooking_time)
		txt += "recipe's ingredients are: {}\n".format(" ".join(self.ingredients))
		txt += "recipe's description is: {}\n".format(self.description)
		txt += "recipe's type is: {}\n".format(self.recipe_type)
		return txt

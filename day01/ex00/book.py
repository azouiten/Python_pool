

from datetime import datetime
from unicodedata import name

from recipe import Recipe

class Book:
	def __init__(self, name, last_update, creation_date, recipes_list):
		assert isinstance(last_update, datetime) and isinstance(creation_date, datetime), "last update and creation date need to be of type datetime"
		assert isinstance(recipes_list, dict) and "starter" in recipes_list.keys() and "lunch" in recipes_list.keys() and "desert" in recipes_list.keys(), "recipes_list needs to be a dictionary and include the keys : start, lunch and desert"
		self.name = name
		self.last_update = last_update
		self.creation_date = creation_date
		self.recipes_list = recipes_list

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		for key in self.recipes_list.keys():
			for recipe in self.recipes_list[key]:
				if recipe["name"] == name:
					pass


	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		for key in self.recipes_list.keys():
			if key == recipe_type:
				for recipe in self.recipes_list[key]:
					pass
	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		assert isinstance(recipe, Recipe), "the recipe must be of type Recipe"
		self.recipes_list[recipe.recipe_type]["name"] = recipe.name
		self.recipes_list[recipe.recipe_type]["cooking_lvl"] = recipe.cooking_lvl
		self.recipes_list[recipe.recipe_type]["cooking_time"] = recipe.cooking_time
		self.recipes_list[recipe.recipe_type]["ingredients"] = recipe.ingredients
		self.recipes_list[recipe.recipe_type]["description"] = recipe.description
		self.recipes_list[recipe.recipe_type]["recipe_type"] = recipe.recipe_type
		# self.recipes_list[recipe.recipe_type] = Recipe()
		self.last_update = datetime.now()

cookbook = {"sandwich": {"ingredients": ["ham", "bread", "cheese", "tomato"], "meal": "lunch", "prep_time": 10},
"cake": {"ingredients": ["flour", "sugar", "eggs"], "meal": "dessert", "prep_time": 60},
"salade": {"ingredients": ["avocado", "arugula", "tomatoes", "spinach"], "meal": "lunch", "prep_time": 15}}

def print_recipe(name):	
	print("Recipe for {}:\nIngredient list: {}\nTo be eaten for {}\nTakes {} minutes of cooking".format(name, cookbook[name]["ingredients"], cookbook[name]["meal"], cookbook[name]["prep_time"]))

def	delete_recipe(name):
	cookbook.pop(name)
	print("recipe {} deleted".format(name))

def	add_recipe(name, ingredients, meal,  prep_time):
	cookbook[name] = {
		"ingredients": ingredients,
		"meal": meal,
		"prep_time": prep_time
	}

def	print_all():
	print("Recipes names : {}".format(' '.join(cookbook.keys())))

print('''Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit''')

while True:
	try:
		inp = int(input(">>"))
		if inp == 5:
			break
		elif inp == 4:
			print_all()
		elif inp == 3:
			name = input("Please enter the recipe's name to get its details:")
			if name in cookbook.keys():
				print_recipe(name)
			else:
				print("Recipe not found")
		elif inp == 2:
			name = input("Please enter the recipe's name to delete it:")
			if name in cookbook.keys():
				delete_recipe(name)
			else:
				print("Recipe not found")
		elif inp == 1:
			name = input("enter name >> ")
			ingredients = input("enter ingredients >> ").split()
			meal = input("enter meal >> ")
			prep_time = input("enter prep time >> ")
			add_recipe(name, ingredients, meal, prep_time)
		else:
			raise ValueError
	except ValueError:
		print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")
print("Cookbook closed.")



import random


print('''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!''')


secret = random.randint(1, 99)
itr = 0

while True:
	resp = input("What's your guess between 1 and 99?\n>>")
	itr += 1
	if resp == "exit":
		print("goodbey!")
		break
	try:
		val = int(resp)
	except ValueError:
		print("That's not a number.")
		continue
	if val == secret:
		if secret == 42:
			print("The answer to the ultimate question of life, the universe and everything is 42.")
		if itr == 1:
			print("Congratulations! You got it on your first try!")
		else:
			print("Congratulations, you've got it!")
			print("You won in {} attempts!".format(itr))
		break
	elif val > secret:
		print("Too high!")
	elif val < secret:
		print("Too low!")
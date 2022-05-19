import string

def text_analyzer(text = None, *args):
	'''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.'''
	up = 0
	low = 0
	space = 0
	pun = 0

	if len(args):
		print("ERROR")
		return
	if text == None:
		text = input("> ")
	if type(text) is not str:
		print("ERROR")
		return
	for char in text:
		if char.isupper():
			up += 1
		elif char.islower():
			low += 1
		elif char == ' ':
			space += 1
		elif char in string.punctuation:
			pun += 1
	print("The text contains 143 characters:")
	print("- " + str(up) + " upper letters")
	print("- " + str(low) + " lower letters")
	print("- " + str(pun) + " punctuation marks")
	print("- " + str(space) + " spaces")
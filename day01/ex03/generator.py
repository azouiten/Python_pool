
import random

def generator(text, sep=" ", option=None):
	'''Option is an optional arg, sep is mandatory'''
	assert isinstance(text, str), "ERROR"
	word_list = text.split(sep)
	if option == "shuffle":
		new_list = []
		for index in range(len(word_list)):
			ind = random.randint(0, len(word_list) -1)
			new_list.append(word_list[ind])
			word_list.pop(ind)
		word_list = new_list
	elif option == "ordered":
		word_list.sort()
	elif option == "unique":
		word_list = list(dict.fromkeys(word_list))
	for elem in word_list:
		yield elem
	pass

text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" "):
    print(word)
print("...")
for word in generator(text, sep=" ", option="shuffle"):
    print(word)
print("...")
for word in generator(text, sep=" ", option="ordered"):
    print(word)
print("...")

text = "Lorem Ipsum Lorem Ipsum"
for word in generator(text, sep=" ", option="unique"):
    print(word)
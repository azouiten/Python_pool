import sys
import string

if len(sys.argv) != 3:
	print("ERROR")
else:
	try:
		num = int(sys.argv[2])
		text = str(sys.argv[1])
		print([word for word in text.translate(str.maketrans("", "", string.punctuation)).split() if len(word) > num])
	except ValueError:
		print("ERROR")
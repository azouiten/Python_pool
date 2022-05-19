
import sys

try:
	assert len(sys.argv) == 2, "Wrong number of arguments is provided!"
	assert int(sys.argv[1]), "Not int"
	print(''.join(["I'm Zero." if int(sys.argv[1]) == 0 else "I'm Odd." if int(sys.argv[1]) % 2 != 0 else "I'm Even."]))
except AssertionError as msg:
	print("{}: {}".format(type(msg).__name__, msg))
except ValueError as e:
	print("{}: argument is not an int".format(type(e).__name__))
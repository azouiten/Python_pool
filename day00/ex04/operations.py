
import sys

def usage():
	print("USAGE: python operations.py <number1> <number2>")

def operations(num1, num2):
		ret_list = []
		try:
			ret_list.append(str(num1 + num2))
			ret_list.append(str(num1 - num2))
			ret_list.append(str(num1 * num2))
			ret_list.append(str(num1 / num2))
			ret_list.append(str(num1 % num2))
		except ZeroDivisionError:
			ret_list.append("ERROR (div by zero)")
			ret_list.append("ERROR (modulo by zero)")
		return ret_list


if len(sys.argv) < 3:
	print("InputERROR: Too few arguments")
	usage()
elif len(sys.argv) > 3:
	print("InputERROR: Too many arguments")
	usage()
else:
	try:
		num1 = int (sys.argv[1])
		num2 = int (sys.argv[2])
		results = operations(num1, num2)
		print("Sum:\t\t" + results[0])
		print("Difference:\t" + results[1])
		print("Product:\t" + results[2])
		print("Quotient:\t" + results[3])
		print("Remainder:\t" + results[4])
	except ValueError:
		print("InputERROR: only numbers")
		usage()




import re


class Evaluator:
	@staticmethod
	def zip_evaluate(coefs, words):
		ret_val = 0
		if len(coefs) != len(words):
			return -1
		for elem in zip(coefs, words):
			ret_val += elem[0] * len(elem[1])
		return ret_val
	
	@staticmethod
	def enumerate_evaluate(coefs, words):
		ret_val = 0
		if len(coefs) != len(words):
			return -1
		for index, elem in enumerate(coefs):
			ret_val += elem * len(words[index])
		return ret_val
	pass

# words = ["Le", "Lorem", "Ipsum", "est", "simple"]
# coefs = [1.0, 2.0, 0.0, 4.0, 0.5]
# # print(Evaluator.zip_evaluate(coefs, words))
# print(Evaluator.enumerate_evaluate(coefs, words))
# words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
# coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
# print(Evaluator.zip_evaluate(coefs, words))
# # print(Evaluator.enumerate_evaluate(coefs, words))
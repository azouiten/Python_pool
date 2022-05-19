

class GotCharacter:
	def __init__(self, first_name, is_alive = True):
		self.first_name = first_name
		self.is_alive = is_alive

class Tarly(GotCharacter):
	def __init__(self, first_name, is_alive = True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Tarly"
		self.house_words = "First in Battle"
	def print_house_words(self):
		'''prints to screen the House words'''
		print(self.house_words)
	def die(self):
		'''kills character'''
		self.is_alive = False
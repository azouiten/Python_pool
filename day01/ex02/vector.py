

class Vector:
	def __init__(self, *args):
		self.is_row = True
		if len(args) == 1 and isinstance(args[0], list):
			self._vector = args[0]
			self.shape = (1, len(args[0]))
			self.values = args[0]
		elif len(args) == 1 and isinstance(args[0], int):
			self._vector = [val for val in range(0, args[0])]
			self.shape = (1, args[0])
			self.values = self._vector
		elif len(args) > 1 and isinstance(args[0], list):
			self._vector = list(args)
			self.shape = (len(args), 1)
			self.values = [val for lst in args for val in lst]
			self.is_row = False
		elif len(args) == 1 and isinstance(args[0], tuple) and len(args[0]) == 2:
			self._vector = [val for val in range(args[0][0], args[0][1])]
			self.shape = (1, args[0][1] - args[0][0])
			self.values = self._vector

	def __repr__(self):
		'''returns a representation of the object'''
		if self.is_row:
			return str(self._vector)
		else:
			return str(self._vector)

	def __add__(self, vector):
		'''apply addition on a vectors and a vector'''
		assert isinstance(vector, Vector), "Illegal operation (invalid type)"
		assert vector.shape == self.shape, "Illegal operation (the two vectors dont have the same dimensions)"
		if self.is_row:
			for index, elem in enumerate(self._vector):
				self._vector[index] = self._vector[index] + vector._vector[index]
			return Vector(self._vector)
		else:
			for index_i, elem in enumerate(self._vector):
				for index_j, val in enumerate(elem):
					self._vector[index_i][index_j] = self._vector[index_i][index_j] + vector._vector[index_i][index_j]
			return Vector(self._vector)

	def __sub__(self, vector):
		assert isinstance(vector, Vector), "Illegal operation (invalid type)"
		assert vector.shape == self.shape, "Illegal operation (the two vectors dont have the same dimensions)"
		if self.is_row:
			for index, elem in enumerate(self._vector):
				self._vector[index] = self._vector[index] - vector._vector[index]
			return Vector(self._vector)
		else:
			for index_i, elem in enumerate(self._vector):
				for index_j, val in enumerate(elem):
					self._vector[index_i][index_j] = self._vector[index_i][index_j] - vector._vector[index_i][index_j]
			return Vector(self._vector)

	def __mul__(self, scalar):
		assert isinstance(scalar, int) or isinstance(scalar, float), "Illegal operation (invalid type)"
		if self.is_row:
			for index, elem in enumerate(self._vector):
				self._vector[index] = elem * scalar
			return Vector(self._vector)
		else:
			for index_i, elem in enumerate(self._vector):
				for index_j, val in enumerate(elem):
					self._vector[index_i][index_j] = val * scalar
			return Vector(self._vector)

	def __truediv__(self, scalar):
		assert isinstance(scalar, int) or isinstance(scalar, float), "Illegal operation (invalid type)"
		assert int(scalar) != 0, "cannot devide by zero"
		if self.is_row:
			for index, elem in enumerate(self._vector):
				self._vector[index] = elem / scalar
			return Vector(self._vector)
		else:
			for index_i, elem in enumerate(self._vector):
				for index_j, val in enumerate(elem):
					self._vector[index_i][index_j] = val / scalar
			return Vector(self._vector)

	def __radd__(self, vector):
		'''apply addition on a vectors and a vector'''
		assert isinstance(vector, Vector), "Illegal operation (invalid type)"
		assert vector.shape == self.shape, "Illegal operation (the two vectors dont have the same dimensions)"
		if self.is_row:
			for index, elem in enumerate(self._vector):
				self._vector[index] = self._vector[index] + vector._vector[index]
			return Vector(self._vector)
		else:
			for index_i, elem in enumerate(self._vector):
				for index_j, val in enumerate(elem):
					self._vector[index_i][index_j] = self._vector[index_i][index_j] + vector._vector[index_i][index_j]
			return Vector(self._vector)

	def __rsub__(self, vector):
		assert isinstance(vector, Vector), "Illegal operation (invalid type)"
		assert vector.shape == self.shape, "Illegal operation (the two vectors dont have the same dimensions)"
		if self.is_row:
			for index, elem in enumerate(self._vector):
				self._vector[index] = self._vector[index] - vector._vector[index]
			return Vector(self._vector)
		else:
			for index_i, elem in enumerate(self._vector):
				for index_j, val in enumerate(elem):
					self._vector[index_i][index_j] = self._vector[index_i][index_j] - vector._vector[index_i][index_j]
			return Vector(self._vector)

	def __rmul__(self, scalar):
		assert isinstance(scalar, int) or isinstance(scalar, float), "Illegal operation (invalid type)"
		if self.is_row:
			for index, elem in enumerate(self._vector):
				self._vector[index] = elem * scalar
			return Vector(self._vector)
		else:
			for index_i, elem in enumerate(self._vector):
				for index_j, val in enumerate(elem):
					self._vector[index_i][index_j] = val * scalar
			return Vector(self._vector)

	def __rtruediv__(self, scalar):
		assert isinstance(scalar, int) or isinstance(scalar, float), "Illegal operation (invalid type)"
		assert int(scalar) != 0, "cannot devide by zero"
		if self.is_row:
			for index, elem in enumerate(self._vector):
				self._vector[index] = elem / scalar
			return Vector(self._vector)
		else:
			for index_i, elem in enumerate(self._vector):
				for index_j, val in enumerate(elem):
					self._vector[index_i][index_j] = val / scalar
			return Vector(self._vector)

	def dot(self, vector):
		assert isinstance(vector, Vector), "Illegal operation (invalid type)"
		assert vector.shape == self.shape, "Illegal operation (the two vectors dont have the same dimensions)"
		dot = 0
		for index, elem in enumerate(self._vector):
				dot += self._vector[index] * vector._vector[index]
		return dot
		

	def T(self):
		new_vector = []
		if self.is_row:
			for elem in self._vector:
				new_vector.append(list(elem))
			self.is_row = False
			self.shape = self.shape[::-1]
		else:
			for index_i, elem in enumerate(self._vector):
				for index_j, val in enumerate(elem):
					new_vector.append(self._vector[index_i][index_j])
			self.is_row = True
			self.shape = self.shape[::-1]
		self._vector = new_vector
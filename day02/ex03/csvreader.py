

import traceback as tb

class CsvReader():
	def __init__(self, filename=None, sep=",", header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.header_content = []
		self.data = []
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.file = None
		self.lenght = 0

	def __enter__(self):
		try:
			if self.filename != None:
				self.file = open(self.filename, "r")
			assert self.file != None, "file not opened"
			lines = self.file.readlines()
			assert len(lines) > (self.skip_bottom + self.skip_top), "Invalid skip params"
			if self.header == True:
				self.header_content = lines[0].split(self.sep)
				lines.pop(0)
			lines = lines[self.skip_top: len(lines) - self.skip_bottom]
			for line in lines:
				self.data.append([elem.strip() for elem in line.split(self.sep)])
			self.lenght = len(self.data[0])
			assert all(self.lenght == len(row) for row in self.data), "bad format"
			assert all(len(elem) != 0 for row in self.data for elem in row), "bad format"
		except AssertionError as msg:
			print("AssertionError: " + str(msg))
			return None
		return self

	def __exit__(self, exc_type, exc_value, exc_traceback):
		if self.file != None:
			self.file.close()
		if exc_type != None:
			return (not print("{}: {}".format(exc_type.__name__, exc_value)))

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Returns:
		nested list (list(list, list, ...)) representing the data.
		"""
		return self.data




	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
		list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
		return self.header_content

if __name__ == "__main__":
	with CsvReader(None) as file:
		if file == None:
			print("File is corrupted")
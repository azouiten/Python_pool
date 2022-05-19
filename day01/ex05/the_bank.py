

class Bank:
	"""The bank"""

	def __init__(self):
		self.account = []

	def add(self, account):
		account_att = dir(account)
		if len(account_att) % 2 == 0 or all(not element.startswith("zip") for element in account_att)\
			or all(not element.startswith("addr") for element in account_att) or\
				not all(not element.startswith("b") for element in account_att) or\
					"name" not in account_att or "id" not in account_att or "value" not in account_att:
					print("Error: corrupted account")
					return False
		self.account.append(account)
		return True

	def transfer(self, origin, dest, amount):
		"""
		@origin: int(id) or str(name) of the first account
		@dest: int(id) or str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		#check if the accounts are corrupted
		origin_att = dir(origin)
		dest_att = dir(dest)
		if len(origin_att) % 2 == 0 or all(not element.startswith("zip")\
			for element in origin_att) or all(not element.startswith("addr") for element in origin_att)\
				or len(dest_att) % 2 == 0 or all(not element.startswith("zip") for element in dest_att)\
					or all(not element.startswith("addr") for element in dest_att)\
						or not all(not element.startswith("b") for element in origin_att)\
							or not all(not element.startswith("b") for element in dest_att)\
								or "name" not in origin_att or "name" not in dest_att\
									or "id" not in origin_att or "id" not in dest_att\
										or "value" not in origin_att or "value" not in dest_att:
			print("Error: corrupted account")
			return False
		if amount < 0 or origin.value - amount < 0:
			print("Error: insufficient funds")
			return False
		origin.value -= amount
		dest.value += amount
		return True
	
	def fix_account(self, account):
		"""
		fix the corrupted account
		@account: int(id) or str(name) of the account
		@return True if success, False if an error occured
		"""
		account_att = dir(account)
		if all(not element.startswith("zip") for element in account_att):
			setattr(account, 'zip_attr', None)
		if all(not element.startswith("addr") for element in account_att):
			setattr(account, 'addr_attr', None)
		if "name" not in account_att:
			setattr(account, 'name', None)
		if "id" not in account_att:
			setattr(account, 'id', 1)
		if "value" not in account_att:
			setattr(account, 'value', 0)
		for elem in account_att:
			if elem.startswith("b"):
				delattr(account, elem)
		account_att = dir(account)
		if len(account_att) % 2 == 0:
			setattr(account, 'extra_attr', None)


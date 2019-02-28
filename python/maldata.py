class _MalData:

	INT = "INT"
	FLOAT = "FLOAT"
	SYMBOL = "SYMBOL"
	TRUE = "TRUE"
	FALSE = "FALSE"

	def __init__(self, type_str="INT", val=None):
		self.type = type_str
		self.val = val

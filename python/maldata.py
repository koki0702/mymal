class _MalData:

	INT = "INT"
	FLOAT = "FLOAT"
	SYMBOL = "SYMBOL"
	STRING = "STRING"
	TRUE = "TRUE"
	FALSE = "FALSE"
	NIL = "NIL"

	def __init__(self, type_str="INT", val=None):
		self.type = type_str
		self.val = val

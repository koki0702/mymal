from maldata import _MalData

print_readably = True


def pr_str(ast):
	if isinstance(ast, tuple):
		return "(" + " ".join([pr_str(x) for x in ast]) + ")"
	elif ast.type == "SYMBOL":
		return ast.val
	elif ast.type == "INT" or ast.type == "FLOAT":
		return str(ast.val)
	elif ast.type == "STRING":
		if print_readably:
			txt = ast.val
			#txt.replace("\n", "\n")
			#txt.replace("\\", "\")
			#txt.replace('\"', '"')

		return ast.val
	else:
		print(ast.type)
		raise Exception("No Data Type!")


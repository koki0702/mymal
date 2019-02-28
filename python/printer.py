from maldata import _MalData


def pr_str(ast):
	if isinstance(ast, tuple):
		return "(" + " ".join([pr_str(x) for x in ast]) + ")"
	elif ast.type == "SYMBOL":
		return ast.val
	elif ast.type == "INT" or ast.type == "FLOAT":
		return str(ast.val)
	else:
		print(ast.type)
		raise Exception("No Data Type!")
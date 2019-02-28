
def pr_str(ast):
	if isinstance(ast, str):
		return ast
	elif isinstance(ast, int) or isinstance(ast, float):
		return str(ast)
	elif isinstance(ast, tuple):
		return "(" + " ".join([pr_str(x) for x in ast]) + ")"
	else:
		raise Exception("No Data Type!")
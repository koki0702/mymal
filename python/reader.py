import re 



class Reader:

	def __init__(self, tokens=None):
		self.pos = 0
		self.tokens = tokens
		pass

	def next(self):
		token = self.tokens[self.pos]
		self.pos += 1
		return token		

	def peek(self, pos=None):
		if self.pos >= len(self.tokens):
			raise Exception('xxx')

		p = pos if pos is not None else self.pos
		return self.tokens[p]


def read_str(txt):
	tokens = tokenize(txt)
	reader = Reader(tokens)
	ast = read_form(reader)
	return ast


def tokenize(txt):
	return re.findall(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)""", txt)


def read_form(reader):
	token = reader.peek()
	if token == '(':
		reader.next()
		return read_list(reader)
	else:
		return read_atom(reader)


def read_list(reader):
	ret = []
	while reader.peek() != ')':
		l = read_form(reader)
		ret.append(l)
		reader.next()

	return tuple(ret)

def read_atom(reader):
	token = reader.peek()
	if token.isdigit():
		token = int(token)
	elif token.isnumeric():
		token = float(token)

	return token


if __name__=='__main__': 
## test
	from printer import pr_str

	print(read_str(':kw'))
	"""
	txts = ['123', '123 ', 'abc', 'abc ', '(123 456)', '( 123 456 789 )', '( + 2 (* 3 4) ) ']

	for txt in txts:
		data = read_str(txt)
		t2 = pr_str(data)
		print(txt + '-' + t2 + '-')
		#print(str(txt)+ '-' + str(read_str(txt)) + '-')

	"""
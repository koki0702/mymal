import re 
from maldata import _MalData


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
            raise Exception('unbalanced parens')

        p = pos if pos is not None else self.pos
        return self.tokens[p]


def read_str(txt):
    tokens = tokenize(txt)
    reader = Reader(tokens)
    try:
        ast = read_form(reader)
    except Exception:
        ast = _MalData("SYMBOL", "EOF")
    return ast


def tokenize(txt):
    return re.findall(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)""", txt)

SYMBOL_MAP = {'\'':'quote', '`':'quasiquote', '~':'unquote', '~@':'splice-unquote', '@':'deref'}

def read_form(reader):
    token = reader.peek()
    # reader macros

    if token[0] == ';':
        reader.next()
        return _MalData("NIL")
    elif token in SYMBOL_MAP.keys():  # quote or quasiquote
        reader.next()
        _v = (_MalData("SYMBOL", SYMBOL_MAP[token]), read_form(reader))
        return _MalData("LIST", _v)
    elif token == '^':
        reader.next()
        meta = read_form(reader)
        reader.next()
        _v = (_MalData("SYMBOL", 'with-meta'), read_form(reader), meta)
        return _MalData("LIST", _v)
    # list
    elif token == '(':
        return read_list(reader, "LIST")
    elif token == ')':
        raise Exception('Unexpected ")"')

    # vector
    elif token == '[':
        return read_list(reader, "VECTOR")
    elif token == ']':
        raise Exception('Unexpected "]"')

    # hash-map
    elif token == '{':
        return read_hash(reader)
    elif token == '}':
        raise Exception('Unexpected "}"')

    else:
        return read_atom(reader)


def read_hash(reader):
    ret = {}
    reader.next()

    while reader.peek() != '}':
        key = read_form(reader)
        reader.next()
        if reader.peek() == '}': raise Exception('unbalanced hashmap')
        val = read_form(reader)
        ret[key] = val
        reader.next()

    return _MalData("HASH", ret)


def read_list(reader, type="LIST"):
    ret = []
    reader.next()
    right_token = ')' if type == "LIST" else ']'

    while reader.peek() != right_token:
        l = read_form(reader)
        ret.append(l)
        reader.next()
    if type == "LIST": ret = tuple(ret)
    else: ret = list(ret)

    return _MalData(type, ret)


def _unescape(s):
    return s.replace('\\\\', '\u029e').replace('\\"', '"').replace('\\n', '\n').replace('\u029e', '\\')

def _keyword(txt):
    return '\u029e' + txt[1:]

def read_atom(reader):
    token = reader.peek()
    mal_data = None

    #if token.isdigit():
    if re.match('-?\d', token):
        return _MalData("INT", int(token))
    elif token[0] == '"':
        if token[-1] == '"':
            return _MalData("STRING", _unescape(token[1:-1]))
        else:
            raise Exception("expected '\"', got EOF")
    elif token[0] == ":":  # keyword
        return _MalData("KEYWORD", _keyword(token))
    elif token == "true":
        return _MalData("TRUE")
    elif token == "false":
        return _MalData("FALSE")
    elif token == "nil":
        return _MalData("NIL")
    else:
        return _MalData("SYMBOL", str(token))


if __name__=='__main__': 
## test
    from printer import pr_str

    #txts = ['123', '123 ', 'abc', 'abc ', '(123 456)', '( 123 456 789 )', '( + 2 (* 3 4) ) ']
    txts = ['{"abc" 1}', '^{"a" 1} [1 2 3]']
    for txt in txts:
        data = read_str(txt)
        t2 = pr_str(data)
        print(txt + '-' + t2 + '-')
        #print(str(txt)+ '-' + str(read_str(txt)) + '-')

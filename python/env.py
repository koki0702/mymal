from maldata import _MalData


class Env:

    def __init__(self, outer=None, binds=None, exprs=None):
        self.data = {}
        self.outer = outer

        if binds:
            for i in range(len(binds)):
                if binds[i] == "&":
                    self.data[binds[i+1]] = _MalData("LIST", exprs[i:])
                    break
                else:
                    self.data[binds[i]] = exprs[i]

    def set(self, key, val):
        self.data[key] = val

    def find(self, key):
        if key in self.data:
            return self.data
        else:
            if isinstance(self.outer, Env):
                return self.outer.find(key)
            else:
                return None

    def get(self, key):
        data = self.find(key)
        if data is not None:
            return data[key]
        else:
            raise Exception("'" + key + "' not found")

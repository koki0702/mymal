class _MalData:

    def __init__(self, type_str="INT", val=None):
        self.type = type_str
        self.val = val

    def __call__(self, *args):
        if self.type == "FUNCTION":
            if hasattr(self, '__ast__'):
                ast = self.__ast__
                env = selfs.__gen_env__(args)
                return self.val()
            else:
                return self.val(*args)

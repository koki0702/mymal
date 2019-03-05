class _MalData:

    def __init__(self, type_str="INT", val=None):
        self.type = type_str
        self.val = val
        self.is_macro = False

class MalException(Exception):
    def __init__(self, object):
        self.object = object
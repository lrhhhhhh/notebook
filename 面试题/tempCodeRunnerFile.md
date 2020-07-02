class Foo:
    def __init__(self):
        self._read_only_attr = 1

    @property
    def read_only_attr(self):
        return self._read_only_attr
    
    @read_only_attr.setter
    def read_only_attr(self, val):
        raise Exception('read only')

f = Foo()
print(f.read_only_attr)
f.read_only_attr = 2
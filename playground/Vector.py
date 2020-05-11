from array import array
from math import sqrt
import reprlib

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)
    
    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
    

v1 = Vector([3.1, 4.2])
print(v1)
>>>(3.1, 4.2)

v2 = Vector([3.0, 4.0, 5.0])
print(v2)
>>>(3.0, 4.0, 5.0)

v3 = Vector(range(100))
print('%r' % v3)
>>>Vector([0.0, 1.0, 2.0, 3.0, 4.0, ...])


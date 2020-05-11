from array import array
from math import sqrt

class Vector2d:
    __slots__ = ('__x', '__y')

    typecode = 'd'

    def __init__(self, x:float, y:float):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (_ for _ in (self.x, self.y))

    def __repr__(self):
        return 'Vector2d({x}, {y})'.format(x=self.x, y=self.y)
    
    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)
    
    def __eq__(self, rhs):
        return self.x==rhs.x and self.y==rhs.y

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))) 

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __bool__(self):
        return self.x != 0 and self.y != 0
    
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


v1 = Vector2d(1, 2)
v2 = Vector2d(1, 2)
print(v1 == v2)
>>>True

print(v1)
>>>(1.0, 2.0)

print(abs(Vector2d(3, 4)))
>>>5.0

v0 = Vector2d(0, 0)
print(bool(v0))
>>>False

x, y = v0
print(x, y)
>>>0.0 0.0

print(bytes(v0))
>>>b'd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

s = {v0, v1}
print(s)
>>>{Vector2d(0.0, 0.0), Vector2d(1.0, 2.0)}

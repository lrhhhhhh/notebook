## 分块1
### 题目来源 https://github.com/kenwoodjw/python_interview_question
### [1.1] 4G内存读取10G大小的文件
要点: 不能一次性读取10G大小的文件到内存

思路1: 利用生成器
```python
def get_lines(filename):
    with open(filename) as fp:
        for line in fp:
            yield line
```
思路2: 开辟指定大小的缓存区，每次读取对应大小
```python
BUFSIZE = 65536
def get_lines(filename):
    with open(filename, 'r') as fp:
        while True:
            chunk = fp.readlines(BUFSIZE)
            if not chunk:
                raise StopIteration
            yield chunk
```
思路3: mmp

### [1.2] 题目没看明白

### [1.3] 输入日期， 判断这一天是这一年的第几天？
思路1: 利用现有的包
思路2: 强行模拟

### [1.4] 打乱一个排好序的list对象？
思路: 利用ramdom.shuffle()
```python
import random
L = [1, 2, 3, 4, 5]
random.shuffle(L)
print(L)
```

### [1.5] 现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
```python
d = {'a':24,'g':52,'i':12,'k':33}
n = sorted(d.items(), key=lambda x : x[1])
print(n)
```

### [1.6] 字典推导式

### [1.7] 反转字符串
思路1: 利用切片
```python
s = 'I_LOVE_YOU'
print(s[::-1])
```
思路2: 利用reversed()
```python
s = 'I_LOVE_YOU'
print(''.join(list(reversed(s))))
```

### [1.8] 将字符串 "k:1|k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
思路: 使用split()
```python
s = "k:1|k1:2|k2:3|k3:4"
d = dict()
for each in s.split('|'):
    k, v = each.split(':')
    d[k] = v
print(d)
```

### [1.9] 请按alist中元素的age由大到小排序
```python
alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
L1 = sorted(alist, key=lambda x : x['age'], reverse=True)
print(L1)
```

### [1.9.1] 思考题: 请按alist中元素的age由大到小排序, 注意对比[1.5]
```python
alist = [{'age':20},{'age':30},{'age':25}]
L1 = sorted(alist, key=lambda x : x['age'], reverse=True)
print(L1)
```

### [1.10] 下面的代码输出什么
```python
list = ['a','b','c','d','e']
print(list[10:])
```
答，输出[]

### [1.11]写一个列表生成式，产生一个公差为11的等差数列
```python
L = [x for x in range(0, 100, 11) ]
print(L)
```

### [1.12] 给定两个列表，怎么找出他们相同的元素和不同的元素？
思路: 利用set的and与xor
```python
L1 = [1, 2, 3]
L2 = [3, 4, 5]
print(set(L1) & set(L2))
print(set(L1) ^ set(L2))
```

### [1.13]请写出一段python代码实现删除list里面的重复元素？
```python
L = [8, 8, 1, 2, 2, 3, 4, 5, 5, 6, 7]
d = dict()
for each in L:
    if not d.get(each):
        d[each] = True
L = [x for x in d.keys()]
print(L)
```

### [1.14] 给定两个list A，B ,请用找出A，B中相同与不同的元素
思路: 利用set的and和xor

### [1.15] python新式类和经典类的区别？
[不知道1] [以下答案来自原帖]  
a. 在python里凡是继承了object的类，都是新式类  
b. Python3里只有新式类  
c. Python2里面继承object的是新式类，没有写父类的是经典类  
d. 经典类目前在Python里基本没有应用  
e. 保持class与type的统一对新式类的实例执行a.__class__与type(a)的结果是一致的，对于旧式类来说就不一样了。  
f.对于多重继承的属性搜索顺序不一样, 新式类是采用广度优先搜索，旧式类采用深度优先搜索。  

### [1.16]python中内置的数据结构有几种？
python3:
int, float, complex, str, dict, list, tuple, set 

### [1.17] python如何实现单例模式?请写出两种实现方式?
[不知道2][以下回答来自原帖]
思路一: 装饰器
```python
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Foo(object):
    pass
foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)  # True
print(foo1.__class__)
```

思路二: 使用基类New, 通过调用super, 将唯一实例附着在类属性里 
```python

class SingletonPattern:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingletonPattern, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class Foo(SingletonPattern):
    pass

foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)

```
思路三: 元类
```python
class SingletonPattern(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingletonPattern, cls).__call__(*args, **kwargs)
        return cls._instance

class Foo(metaclass=SingletonPattern):
    pass

foo1 = Foo()
foo2 = Foo()

print(foo1 is foo2)
```

### [1.18] 反转一个整数，例如-123 --> -321
思路: 转换成字符串直接reverse, 特判负数和10的倍数

### [1.19] 设计实现遍历目录与子目录，抓取.pyc文件
[答案来自原帖]
```python
import os

def get_files(dir, suffix):
    res = list()
    for root, dirs, files in os.walk(dir):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))
    return res
```

### [1.20] 一行代码实现1-100之和
```python
print(sum(range(1, 101)))
```

### [1.21] 遍历列表时删除元素的正确做法
没看懂问题

### [1.22] 
pass, 纯属编程题，与python无关

### [1.23] 可变类型和不可变类型
来源《fluent python》 
- 可变: list, bytearray, array.array, collections.deque, memoryview
- 不可变: tuple, str, bytes
tuple是引用不可变，不代表内容不可变

### (1.24) is 和 == 的区别
`==`的判断依据是`__equal__()`中的实现，约定为判断两个变量的内容是否相等  
`is`比较的是两个被比较对象的id是否相同，是否为同一个实例

### (1.25) 求出列表所有奇数并构造新列表
思路一: 使用filter
```python
a = [1,2,3,4,5,6,7,8,9,10]
L = filter(lambda x : x%2!=0, a)
print(list(L))
```
思路二: 列表推导
```python
a = [1,2,3,4,5,6,7,8,9,10]
L = [x for x in a if x%2!=0]
print(L)
```

### (1.26) 用一行python代码写出1+2+3+10248
思路一: sum
```python
print(sum(range(1, 10249)))
```
思路二； reduce
```python
from functools import reduce
print(reduce(lambda x, y : x+y, range(1, 10249)))
```

### (1.27) python中变量的作用域
LEGB, 即local, enclosing, global, build-in

### (1.28) 字符串 "123" 转换成 123，不使用内置api，例如 int()
按题意模拟

### (1.29) 编程题，pass

### (1.30) python代码实现删除一个list里面的重复元素
重复了, 同(1.15)

### (1.31) 统计一个文本中单词频次最高的10个单词？
思路: 利用正则表达式提取单个单词，利用dict记录词频， 排序
```python
import re
def solve(filename):
    pattern =  re.compile("[a-zA-Z']+")
    d = dict()
    with open(filename, 'r') as fp:
        for line in fp:
            res = pattern.findall(line)
            for each in res:
                if not d.get(each):
                    d[each] = 1
                else:
                    d[each] += 1
    print(sorted(d.items(), key=lambda x:x[1], reverse=True)[:10])
```

### (1.32) 纯编程题, pass

### (1.33) 使用单一的列表生成式来产生一个新的列表
没看懂题目

### (1.34) 用一行代码生成[1,4,9,16,25,36,49,64,81,100]
```python
print([x*x for x in range(1, 11)])
```

### (1.35) 重复题目, 同(1.3)

### (1.36) 两个有序列表，l1,l2，对这两个列表进行合并不可使用extend
这题描述不清

### (1.37) 编程题，pass

### (1.38) 编程题, pass

### (1.39) 阅读一下代码他们的输出结果是什么？
```python
def multi():
    return [lambda x : i*x for i in range(4)]
print([m(3) for m in multi()])
```
我的答案: 0, 3, 6, 9  
正确答案: 9, 9, 9, 9  
闭包中的变量i是在内部函数被调用的时候被查找的

### (1.40) 统计一段字符串中字符出现的次数
思路1: 模拟
思路2: 利用Counter 
```python
from collections import Counter
print(Counter("AAABBCCAC").most_common())
```

### (1.41) super函数的具体用法和场景
调用父类方法, 主要是由于多重继承过于复杂，导致了super()的参数和设置这么奇怪

### (1.42) Python中类方法、类实例方法、静态方法有何区别？
类方法使用@classmethod装饰器进行定义, 可以通过类对象和实例对象调用, 形参是cls, 表示类对象    
类实例方法只有实例对象可以调用，形参是self, 表示类实例本身  
静态方法使用@staticmethod装饰器进行定义, 可以通过类对象和类实例调用

### (1.43) 遍历一个object的所有属性，并print每一个属性名？
```python
for attr in dir(obj):
    print(attr)
```

### (1.44) 写一个类，并让它尽可能多的支持操作符?
```python
from array import array
from functools import reduce

class Vector:

    typecode = 'd'

    def __init__(self, initializer):
        self.arr = array(self.typecode, initializer)
    
    def __iter__(self):
        return iter(self.arr)
    
    def __eq__(self, other):
        return self.arr == other.arr
    
    def __add__(self, other):
        return Vector(a+b for a, b in zip(self, other))
    
    def __sub__(self, other):
        return Vector(a-b for a, b in zip(self, other))

    def __getitem__(self, idx):
        return self[idx]
    
    def __setitem__(self, idx, val):
        self.arr[idx] = val
    
    def __repr__(self):
        return 'Vector(%s)' % ', '.join(str(_) for _ in self.arr)


v1 = Vector([1, 2, 3, 4, 5])
v2 = Vector([6, 7, 8, 9, 10])
v3 = Vector([1, 2, 3, 4, 5])
print(v1)
print(v2)
print(v1 + v2)
print(v1 - v2)
print(v1 == v3)
print(v1 == v2)
v1[4] = 1
v2[4] = 2
print(v1)
print(v2)
```

### (1.45) 介绍Cython，Pypy Cpython Numba各有什么缺点
这个问题找不到准确答案，建议直接放弃，直到有机会遇到具体的应用场景

### (1.46) 请描述抽象类和接口类的区别和联系
我怀疑原贴答案是基于java回答的
[未解决1] 
抽象类与接口类的相似点是规定了一系列方法，要求继承这些类的子类去实现，
区别是, 对于抽象类来说，它更偏向于实现"祖先"的职能, 即实现这一个种族所共有的特征，
而接口类，偏向于实现某个具体职能，建立不同个体之间沟通的规则。

### (1.47) Python中如何动态获取和设置对象的属性？
```python
obj.attr = val
```

### (1.48) 哪些操作会导致Python内存溢出，怎么处理？


### (1.49) 关于Python内存管理,下列说法错误的是( B )

A,变量不必事先声明 B,变量无须先创建和赋值而直接使用

C,变量无须指定类型 D,可以使用del释放资源

### (1.50) Python的内存管理机制及调优手段？
[未解决2]
内存管理机制: 引用机制、垃圾回收、内存池
循环引用使引用计数失效，引入“标记-清除”，“分代回收” 弥补缺陷
调优手段:
1.手动垃圾回收
2.调高垃圾回收阈值
3.避免循环引用

### (1.51) 内存泄露是什么？如何避免？
[未解决3] [以下答案来自原贴]
内存泄漏指由于疏忽或错误造成程序未能释放已经不再使用的内存。内存泄漏并非指内存在物理上的消失，而是应用程序分配某段内存后，由于设计错误，导致在释放该段内存之前就失去了对该段内存的控制，从而造成了内存的浪费。

有__del__()函数的对象间的循环引用是导致内存泄露的主凶。不使用一个对象时使用: del object 来删除一个对象的引用计数就可以有效防止内存泄露问题。

通过Python扩展模块gc 来查看不能回收的对象的详细信息。

可以通过 sys.getrefcount(obj) 来获取对象的引用计数，并根据返回值是否为0来判断是否内存泄露

### (1.52) python常见的列表推导式？
pass

### (1.53) 简述read、readline、readlines的区别？
read 将整个文件读入内存
readline 一次读取一行
readlines(sizehint) 读取sizehint字节的文件，如果没有提供则读取全部，返回一个列表
 
### (1.54) 什么是Hash（散列函数）？
将某个东西映射为另一个东西

### (1.55) python函数重载机制？
python没有其他语言那样的重载机制，可以通过functools.singledispatch装饰器实现类似的效果
python由于动态的特性根本不需要重载

### (1.56) python函数重载机制？
pass

### (1.57) 手写一个判断时间的装饰器
```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        st = time.time()
        func(*args, **kwargs)
        time.sleep(10)
        ed = time.time()
        print(ed - st)
        
        if ed -st > 10:
            raise 
    return wrapper

@timer
def test():
    print('yes')

test()
```

### (1.58) 使用Python内置的filter()方法来过滤？
```python
filter(func, iterable)
```

### (1.59) 编写函数的4个原则
pass

### (1.60) 函数调用参数的传递方式是值传递还是引用传递？
不可变参数传值引用，如数值和str，其余可变参数传引用

### (1.61) 如何在function里面设置一个全局变量
```python
def test():
    global x
    x = 1

test()
print(x)
```

### (1.62) 对缺省参数的理解 ？
缺省参数即默认参数

### (1.63) 不是python题目

### (1.64) 带参数的装饰器?
```python
from functools import wraps

def three(myarg=''):
    def two(func):
        @wraps(func)
        def one(*args, **kwargs):
            func(*args, **kwargs)
            print('i was called at ' + myarg)
        return one
    return two

@three('lrh')
def test():
    print('yes')

test()
```

### (1.65) 为什么函数名字可以当做参数用?
函数类

### (1.66) Python中pass语句的作用是什么？
为了使得函数为空，且不报错

### (1.67) 有这样一段代码，print c会输出什么，为什么？
```python
a = 10
b = 20
c = [a]
a = 15
```
[10]

### (1.68) 交换两个变量的值？
```python
a, b = b, a
```

### (1.69) map函数和reduce函数？
```python
from functools import reduce
L = [1, 2, 3, 4, 5]
L1 = list(map(lambda x:x*10, L))
L2 = reduce(lambda x,y:x+y, L, 2333)
print(L1)
print(L2)
```

### (1.70) 回调函数，如何通信的?
这个要怎么说...

### (1.71) Python主要的内置数据类型都有哪些？ print dir( 'a ') 的输出？
内置数据类型:
number, str, tuple, dict, set, list, .....
输出`'a '`这个str对象的内置方法和属性

### (1.72) map(lambda x:xx，[y for y in range(3)])的输出？
这xx是啥玩意？

### (1.73) hasattr() getattr() setattr() 函数使用详解？
pass

### (1.74) 一句话解决阶乘函数？
```python
from functools import reduce
print(reduce(lambda x, y: x*y, range(1, 101)))
```

### (1.75) 什么是lambda函数？ 有什么好处？
lambda函数即匿名函数，好处是不用想名字

### (1.76) 递归函数停止的条件？
pass

### (1.77) 下面这段代码的输出结果将是什么？请解释。
```python
def multipliers():
    return [lambda x: i *x for i in range(4)]

print([m(2) for m in multipliers()])
```
[6, 6, 6, 6]

### (1.78) 什么是lambda函数？它有什么好处？写一个匿名函数求两个数的和
重复, pass

### (1.79) 对设计模式的理解，简述你了解的设计模式？
设计模式是对各种各样不同场景下代码的结构和实现的总结和抽象，复用前人总结的设计模式可以帮助我们设计和实现更好的方案

### (1.80) 请手写一个单例
```python
from functools import wraps

def singleton_pattern(cls):
    instance = dict()
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if not instance.get(cls):
            return instance.setdefault(cls, cls(*args, **kwargs))
        return instance.get(cls)
    return wrapper

@singleton_pattern
class Foo:
    pass

f1 = Foo()
f2 = Foo()

print(f1 is f2)
```

### (1.81) 单例模式的应用场景有那些？
任何只能拥有一个实例的场景(原谅我还真想不出)

### (1.82) 用一行代码生成[1,4,9,16,25,36,49,64,81,100]
```python
print([x**2 for x in range(1, 11)])
```

### (1.83) 对装饰器的理解，并写出一个计时器记录方法执行性能的装饰器？
```python
from functools import wraps
from time import time, sleep

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        st = time()
        func(*args, **kwargs)
        ed = time()
        print('start from %s, end at %s, elapsed %s' % (st, ed, ed - st))
    return wrapper

@timer
def test():
    sleep(10)

test()
```

### (1.84) 解释一下什么是闭包
```python
def func_a():
    x = 1
    def func_b():
        x =2
```
则闭包指的是x=1那一行至x=2那一行, 即子函数使用到父函数的变量，所用到的变量与子函数构成闭包


### (1.85) 函数装饰器有什么作用？ 
[以下回答来自源帖]
装饰器本质上是一个callable object，它可以在让其他函数在不需要做任何代码的变动的前提下增加额外的功能。装饰器的返回值也是一个函数的对象，它经常用于有切面需求的场景。比如：插入日志，性能测试，事务处理，缓存。权限的校验等场景，有了装饰器就可以抽离出大量的与函数功能本身无关的雷同代码并发并继续使用。 详细参考：https://manjusaka.itscoder.com/2018/02/23/something-about-decorator/

### (1.86) 生成器，迭代器的区别？
直接说区别不好说，最好直接给两者下定义
迭代器提供一个统一的接口，用于访问容器里的元素，而不需要关心容器到底如何实现，在python里，迭代器需要实现迭代器协议，
实现`__iter__()`和`__next__()`

使用里yield的函数被称为生成器，所有生成器都是迭代器,因为生成器完全实现了迭代器接口，生成器可以节约内存

### (1.87) X是什么类型?
```python
X= (i for i in range(10))
```
生成器类型

### (1.88) 请用一行代码 实现将1-N 的整数列表以3为单位分组
```python
print([[i, i+1, i+2] for i in range(1, 100, 3)])
```

### (1.89) Python中yield的用法?
生成器，协程

### (1.90) Python中的可变对象和不可变对象？
不可变对象指的是对象一旦生成内容便不可变

```python
L = [1, 2]
a = (L, 1)
print(id(a))
a[0].append(3)
print(a)
print(id(a))

```
tuple不知道什么时候修复了以上

### (1.91) Python的魔法方法
pass, 没啥好说的

### (1.92) 面向对象中怎么实现只读属性?
```python
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
```

### (1.93) 谈谈你对面向对象的理解？
面向对象即万物皆对象，三大特性: 封装，继承，多态

### (1.94) ~ (1.105) 有关与正则表达式和re包的题目
pass，如果有哪个公司问到这些题目，专家建议直接放弃这些题的得分

### (1.106) 
此处应有进程，线程，进程通信相关代码

### (1.107) 谈谈你对多进程，多线程，以及协程的理解，项目是否用？
[以下来自原帖] [未解决4]
这个问题被问的概念相当之大， 进程：一个运行的程序（代码）就是一个进程，没有运行的代码叫程序，进程是系统资源分配的最小单位，进程拥有自己独立的内存空间，所有进程间数据不共享，开销大。

线程: cpu调度执行的最小单位，也叫执行路径，不能独立存在，依赖进程存在，一个进程至少有一个线程，叫主线程，而多个线程共享内存（数据共享，共享全局变量),从而极大地提高了程序的运行效率。

协程: 是一种用户态的轻量级线程，协程的调度完全由用户控制。协程拥有自己的寄存器上下文和栈。协程调度时，将寄存器上下文和栈保存到其他地方，在切回来的时候，恢复先前保存的寄存器上下文和栈，直接操中栈则基本没有内核切换的开销，可以不加锁的访问全局变量，所以上下文的切换非常快。

### (1.108) Python异步使用场景有那些？
[以下来自原贴]
异步的使用场景:
1、不涉及共享资源，或者对共享资源只读，即非互斥操作
2、没有时序上的严格关系
3、不需要原子操作，或可以通过其他方式控制原子性
4、常用于IO操作等耗时操作，因为比较影响客户体验和使用性能
5、不影响主线程逻辑

### (1.109) 多线程共同操作同一个数据互斥锁同步？
[未解决5]

### (1.110) 什么是多线程竞争？
[以下来自原帖]
线程是非独立的，同一个进程里线程是数据共享的，当各个线程访问数据资源时会出现竞争状态即：数据几乎同步会被多个线程占用，造成数据混乱，即所谓的线程不安全
那么怎么解决多线程竞争问题？---锁
锁的好处： 确保了某段关键代码（共享数据资源）只能由一个线程从头到尾完整地执行能解决多线程资源竞争下的原子操作问题。
锁的坏处： 阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
锁的致命问题: 死锁

### (1.111) 请介绍一下python的线程同步？
[未解决6]

### (1.112) 解释以下什么是锁，有哪几种锁？
锁借鉴于现实生活，与现实世界一致，意思是锁住某些东西，不让其他人看到，在编程语言中就是，使用锁锁住某些共享资源，使得程序不能访问，通过控制锁的开和闭，达到每次只能有一个程序访问这一资源的目的

锁有互斥锁，可重入锁，死锁， 数据库里有悲观锁和乐观锁

### (1.113) 什么是死锁?
死锁产生的环境为，线程A占用了锁a， 线程B占用了锁b，A想要锁b，B想要锁a，但是它们都不放弃原先占有的锁

### (1.114) 多线程交互访问数据，如果访问到了就不访问了？
[没读懂题目] [未解决7]

### (1.115) 什么是线程安全，什么是互斥锁？
线程安全指的是 多线程访问共享资源时的有序，不会造成共享资源的混乱  
互斥锁，下定义不好下，但作用好理解，是用来保证某个资源全局只被一个程序访问，程序访问这样的资源时，上了互斥锁，则其他程序无法继续获得这个资源的控制权

### (1.116) 说说下面几个概念：同步，异步，阻塞，非阻塞？
[以下来自原贴]
同步： 多个任务之间有先后顺序执行，一个执行完下个才能执行。
异步： 多个任务之间没有先后顺序，可以同时执行，有时候一个任务可能要在必要的时候获取另一个同时执行的任务的结果，这个就叫回调！
阻塞： 如果卡住了调用者，调用者不能继续往下执行，就是说调用者阻塞了。
非阻塞： 如果不会卡住，可以继续执行，就是说非阻塞的。
同步异步相对于多任务而言，阻塞非阻塞相对于代码执行而言。

### (1.117) 什么是僵尸进程和孤儿进程？怎么避免僵尸进程？
[以下来自原贴] [未解决8]
孤儿进程： 父进程退出，子进程还在运行的这些子进程都是孤儿进程，孤儿进程将被init 进程（进程号为1）所收养，并由init 进程对他们完成状态收集工作。

僵尸进程： 进程使用fork 创建子进程，如果子进程退出，而父进程并没有调用wait 或waitpid 获取子进程的状态信息，那么子进程的进程描述符仍然保存在系统中的这些进程是僵尸进程。
避免僵尸进程的方法：
1.fork 两次用孙子进程去完成子进程的任务
2.用wait()函数使父进程阻塞
3.使用信号量，在signal handler 中调用waitpid,这样父进程不用阻塞


### (1.118) python中进程与线程的使用场景？
cpu密集型用多进程，I/O密集型用多线程

### (1.119)线程是并发还是并行，进程是并发还是并行？
线程并发，进程并行

### (1.120) 并行(parallel)和并发（concurrency)?
并发强调一起出发，并行强调一起运行

并行: 同一时刻多个任务同时在运行
并发: 不会在同一时刻同时运行，存在交替执行的情况。

### (1.121) IO密集型和CPU密集型区别？
表面意思

### (1.122) python asyncio的原理？
[未解决9]

### (1.123) 怎么实现强行关闭客户端和服务器之间的连接?
服务器请求关闭，且在客户端设置超时关闭

### (1.124) 简述TCP和UDP的区别以及优缺点?
[未解决10]
TCP的优点是能验证数据是否完整送达，缺点是TCP报文开销比较大以及建立链接的时间消耗
UDP的优点是协议简单，报文开销小，无需建立链接，可以实现广播发送，缺点是无法保证送达

### (1.125) 简述浏览器通过WSGI请求动态资源的过程?
[未解决11]

### (1.126) 描述用浏览器访问www.baidu.com的过程
先是获取域名对应的ip地址(DNS协议)，得到后向该地址发出http请求, http是建立在tcp上的， tcp又是建立在各种路由协议上的，浏览器得到响应后，渲染

### (1.127) Post和Get请求的区别?
get重在获得，post重在发送


### (1.128) cookie 和session 的区别？
[以下答案来源此链接](https://www.cnblogs.com/Young111/p/9789146.html)  
1、Cookie和Session都是会话技术，Cookie是运行在客户端，Session是运行在服务器端。   
2、Cookie有大小限制以及浏览器在存cookie的个数也有限制，Session是没有大小限制和服务器的内存大小有关。
3、Cookie有安全隐患，通过拦截或本地文件找得到你的cookie后可以进行攻击。
4、Session是保存在服务器端上会存在一段时间才会消失，如果session过多会增加服务器的压力。

### (1.129) https://www.cnblogs.com/Young111/p/9789146.html
- 200 成功
- 201 资源建立
- 401 没有权限访问
- 403 服务器拒绝请求
- 500 服务器内部错误错误
等等


### (1.130) 请简单说一下三次握手和四次挥手？
我的回答注定被扣分:
主机A向主机B发送建立TCP链接请求，消耗一个序列号
主机B收到主机A的请求，对请求进行响应(ack)，同时消耗一个序列号，
主机A收到后再进行响应，主机B接收到响应后TCP连接成功建立

四次挥手，主机A结束了数据传输后，向主机B请求单方面断开tcp链接，主机接收到请求后进行响应，若干时间后，主机B也结束了

这里有一篇文章，写得海星[TCP的三次握手与四次挥手理解及面试题（很全面）](https://blog.csdn.net/qq_38950316/article/details/81087809)

### (1.131) 说一下什么是tcp的2MSL？
TCP 2MSL出现在四次挥手关闭TCP链接中，当TCP连接结束时，一方向另一方发送FIN请求断开，另一方发送ACK进行确认，若无错误则判定正常断开，但是由于复杂的网络环境，当ACK丢失时，将导致一方不停发送FIN，而另一方却关闭的情况。所以当等待2MSL(Maximum Segment Lifetime)后，若再无请求则认为正常关闭

### (1.132) 为什么客户端在TIME-WAIT状态必须等待2MSL的时间？
pass

### (1.133) 说说HTTP和HTTPS区别？
[未解决12] 
https://blog.csdn.net/qq_35684336/article/details/80437661

### (1.134) 谈一下HTTP协议以及协议头部中表示数据类型的字段？
[未解决13]
面试造火箭？

### (1.135) HTTP请求方法都有什么？
GET, POST, DELETE, PUT, HEAD

### (1.136) 使用Socket套接字需要传入哪些参数 ？
[未解决14]

### (1.137) HTTP常见请求头？
[未解决15] 

### (1.138) 七层模型？
[未解决16]
应表会传网数物

### (1.139) url的形式？
[未解决17]  
scheme:[//[user[:password]@]host[:port]][/path][?query][#fragment]

### (1.140) 对Flask蓝图(Blueprint)的理解？
[以下来自原贴]
蓝图 /Blueprint 是Flask应用程序组件化的方法，可以在一个应用内或跨越多个项目共用蓝图。使用蓝图可以极大简化大型应用的开发难度，也为Flask扩展提供了一种在应用中注册服务的集中式机制。

蓝图的应用场景：

把一个应用分解为一个蓝图的集合。这对大型应用是理想的。一个项目可以实例化一个应用对象，初始化几个扩展，并注册一集合的蓝图。

以URL前缀和/或子域名，在应用上注册一个蓝图。URL前缀/子域名中的参数即成为这个蓝图下的所有视图函数的共同的视图参数（默认情况下） 在一个应用中用不同的URL规则多次注册一个蓝图。

通过蓝图提供模板过滤器、静态文件、模板和其他功能。一个蓝图不一定要实现应用或视图函数。

初始化一个Flask扩展时，在这些情况中注册一个蓝图。

蓝图的缺点：

不能在应用创建后撤销注册一个蓝图而不销毁整个应用对象。

### (1.141) Flask 和 Django 路由映射的区别？
[未解决18]

### (1.142) 什么是wsgi,uwsgi,uWSGI?
wsgi: Web Service Gateway Interface 指定了web服务器和Python web应用或web框架之间的标准接口，以提高web应用在一系列web服务器间的移植性。

uWSGI 是一个web服务器

### (1.143) Django、Flask、Tornado的对比？
[未解决19] 
 Flask 是轻量级的框架，自由，灵活，可扩展性强，核心基于Werkzeug WSGI工具 和jinja2 模板引擎

### (1.144) CORS 和 CSRF的区别？
[以下来自原答案]
什么是CORS？
CORS是一个W3C标准,全称是“跨域资源共享"(Cross-origin resoure sharing). 它允许浏览器向跨源服务器，发出XMLHttpRequest请求，从而克服了AJAX只能同源使用的限制。

什么是CSRF？
CSRF(cross-site request forgery)跨站点请求伪造
用户登录A网站后得到cookie存储在浏览器中，此时若用户访问危险网站B，B返回一些攻击性的代码，要求攻击A网站

### (1.145) Session, Cookie, JWT的理解
[以下来自原答案]
为什么要使用会话管理

众所周知，HTTP协议是一个无状态的协议，也就是说每个请求都是一个独立的请求，请求与请求之间并无关系。但在实际的应用场景，这种方式并不能满足我们的需求。举个大家都喜欢用的例子，把商品加入购物车，单独考虑这个请求，服务端并不知道这个商品是谁的，应该加入谁的购物车？因此这个请求的上下文环境实际上应该包含用户的相关信息，在每次用户发出请求时把这一小部分额外信息，也做为请求的一部分，这样服务端就可以根据上下文中的信息，针对具体的用户进行操作。所以这几种技术的出现都是对HTTP协议的一个补充，使得我们可以用HTTP协议+状态管理构建一个的面向用户的WEB应用。

Session 和Cookie的区别

这里我想先谈谈session与cookies,因为这两个技术是做为开发最为常见的。那么session与cookies的区别是什么？个人认为session与cookies最核心区别在于额外信息由谁来维护。利用cookies来实现会话管理时，用户的相关信息或者其他我们想要保持在每个请求中的信息，都是放在cookies中,而cookies是由客户端来保存，每当客户端发出新请求时，就会稍带上cookies,服务端会根据其中的信息进行操作。 当利用session来进行会话管理时，客户端实际上只存了一个由服务端发送的session_id,而由这个session_id,可以在服务端还原出所需要的所有状态信息，从这里可以看出这部分信息是由服务端来维护的。

除此以外，session与cookies都有一些自己的缺点：

cookies的安全性不好，攻击者可以通过获取本地cookies进行欺骗或者利用cookies进行CSRF攻击。使用cookies时,在多个域名下，会存在跨域问题。 session 在一定的时间里，需要存放在服务端，因此当拥有大量用户时，也会大幅度降低服务端的性能，当有多台机器时，如何共享session也会是一个问题.(redis集群)也就是说，用户第一个访问的时候是服务器A，而第二个请求被转发给了服务器B，那服务器B如何得知其状态。实际上，session与cookies是有联系的，比如我们可以把session_id存放在cookies中的。

JWT是如何工作的

首先用户发出登录请求，服务端根据用户的登录请求进行匹配，如果匹配成功，将相关的信息放入payload中，利用算法，加上服务端的密钥生成token，这里需要注意的是secret_key很重要，如果这个泄露的话，客户端就可以随机篡改发送的额外信息，它是信息完整性的保证。生成token后服务端将其返回给客户端，客户端可以在下次请求时，将token一起交给服务端，一般是说我们可以将其放在Authorization首部中，这样也就可以避免跨域问题。

### (1.146) 简述Django请求生命周期
[未解决20]
pass

### (1.147) 用的restframework完成api发送时间时区
[未解决21]
pass

### (1.148) nginx,tomcat,apach到都是什么？
web服务器

### (1.149) 请给出你熟悉关系数据库范式有哪些，有什么作用？
[未解决22]

### (1.150) 简述QQ登陆过程
[未解决23]

### (1.151) post 和 get的区别?
pass

### (1.152) 项目中日志的作用
pass

### (1.153) django中间件的使用？
pass

### (1.154) 谈一下你对uWSGI和nginx的理解？
pass

### (1.155) 

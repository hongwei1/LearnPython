# https://foofish.net/magic-method.html
# 简述 __init__、__new__、__call__ 方法
# 创建--> 初始化--> 使用 --> 垃圾回收, 不同阶段不用方法负责执行.
 
# 必须显示继承 object, python 默认都继承了.
# __init__ 方法
# 负责对象的初始化,系统执行该方法前,其实对象已经存在.
#eg1:
class A:
    def __init__(self):
        print("__init__ ")
        print(self)
        super(A, self).__init__()
        return None # this method can only return None, can not return other types.

    def __new__(cls):
        print("__new__ ")
        self = super(A, cls).__new__(cls)
        print(self)
        return self
    
    def __call__(self):  # 可以定义任意参数
        print('__call__ ')

A()

class B:
    def __init__(self, *args, **kwargs):
        print("init", args, kwargs)

    def __new__(cls, *args, **kwargs):
        print("new", args, kwargs)
        return super().__new__(cls)

B(1, 2, 3)

# 输出

# new (1, 2, 3) {}
# init (1, 2, 3) {}


# __new__ 方法
# 一般不会重写该方法,是构造函数,用于创建对象.是个工厂函数,专门用于生产实例对象.
#eg1: 应用1: 单例模式
class BaseController(object):
    _singleton = None
    def __new__(cls, *a, **k):
        if not cls._singleton:
            cls._singleton = object.__new__(cls, *a, **k)
        return cls._singleton




# __call__ 方法
# 可调用对象(callable), 自定义的函数, 内置函数和类都属于可调用对象.
# 但凡可以把()应用到某个对象身上的都可称为可调用对象.
# 若类中实现了__call__ 方法,那么实例对象也将成为一个可调用对象.

a = A()
print(callable(a))  # True
a()
class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@Counter
def foo():
    pass

for i in range(10):
    foo()

print(foo.count)











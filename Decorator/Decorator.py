# https://foofish.net/python-decorator.html
# 理解 Python 装饰器看这一篇就够了

# step1: python 的函数的参数可以接受另一个函数.
# def foo():
#      print("'I ma foo'")
# 
# # this will accept the method name as the parameters:     
# def bar(func):
#      func()
# 
# bar(foo)


# 不用修改任何代码的前提增加额外功能. 返回值,也是函数/类对象.
# 用于又切面需求的场景: 插入日子,性能测试,事务处理,缓存,权限校验等...
# 为已经存在的对象添加额外的功能.
# 增加日志代码:
import logging
def foo():
     print('i am foo')

# def use_logging(func):
#      logging.warning("%s is running" % func.__name__)
#      func()
# 不再调用这个:
foo()
# 以后需要调用这个,破坏了代码结构.
# use_logging(foo)

# 面向切面编程:
def use_logging(func):
     def wrapper():
          logging.warning("%s is running" % func.__name__)
          return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
     return wrapper

foo = use_logging(foo) # 因为装饰器,返回函数对象 wrapper,这相当于 foo = wrapper.
foo() # 此时执行 foo(),就是执行 wrapper().

# @ 语法糖 -- 放在函数开始的地方,可以省略最后一步再次赋值的操作.

# 只要用@ 就能添加功能,好简单啊.
@use_logging # 省去了 foo = use_logging(foo) 这一句.直接用 foo()就能得到想要的结果.
def foo1():
     print('I am foo1 sugar!!')
     
foo1() 


# 业务逻辑函数 foo需要参数怎么办?
def foo2(name):
     print("i am %s" % name)
     
foo2("Hongwei")

#我们可以在定义 wrapper 函数时指定参数:

# 当装饰器不知道 foo 到底多少个参数时,我们可以用*args代替:

def foo61(name, age = None, height = None):
     print("I am %s, age %s, height %s" % (name,age, height))
     
foo61("hongwei",12,15)     
# *args 是一个数组.
# *kwargs 一个字典.

def use_logging(level):
     def decorator(func):
          def wrapper(*args, **kwargs):
               if level == "warn":
                    logging.warn("%s is running" % func.__name__)
               elif level == "info":
                    logging.info("%s is running" % func.__name__)
               return func(*args)
          return wrapper

     return decorator

@use_logging(level="warn")
def foo81(name='foo'):
     print("i am %s" % name)

foo81()


# 类装饰器 -- 主要依靠_call_ 方法,当使用@ 形式将装饰器附加到函数上是,就是调用此方法.
class Foo(object):
     def __init__(self, func):
          self._func = func
     #TODO I really want to know what is __call__??? 
     def __call__(self):
          print ('class decorator runing')
          self._func()
          print ('class decorator ending')
@Foo
def bar():
     print ('bar')

bar()


# 装饰器
def logged(func):
     def with_logging(*args, **kwargs):
          # print func.__name__      # 输出 'with_logging'
          # print func.__doc__       # 输出 None
          return func(*args, **kwargs)
     return with_logging


# 函数
@logged
def f(x):
     """does some math"""
     return x + x * x

logged(f)

from functools import wraps
def logged(func):
     @wraps(func)
     def with_logging(*args, **kwargs):
          # print func.__name__      # 输出 'f'
          # print func.__doc__       # 输出 'does some math'
          return func(*args, **kwargs)
     return with_logging

@logged
def f(x):
     """does some math"""
     return x + x * x


# 装饰器的顺序
# @a
# @b
# @c
# def f ():
#      pass
# 执行是从里到外,先调用最里面的装饰器,最后调用最外层的装饰器.--> 靠的越近,越先调用.
# --> f = a(b(c(f)))
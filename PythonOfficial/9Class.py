def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)
        
myDog = Dog("hongwei")
myDog.good = "w"
myDog.bad = "d"
print(myDog.good)
f = open('/Users/zhanghongwei/Documents/GitHub-Tower/LearnPython/PythonOfficial/fibo.py', 'r')
f = open('/Users/zhanghongwei/Documents/GitHub-Tower/LearnPython/PythonOfficial/fibo.py', 'r')
f = open('/Users/zhanghongwei/Documents/GitHub-Tower/LearnPython/PythonOfficial/fibo.py', 'r')
f = open('/Users/zhanghongwei/Documents/GitHub-Tower/LearnPython/PythonOfficial/fibo.py', 'r')
f = open('/Users/zhanghongwei/Documents/GitHub-Tower/LearnPython/PythonOfficial/fibo.py', 'r')
f = open('/Users/zhanghongwei/Documents/GitHub-Tower/LearnPython/PythonOfficial/fibo.py', 'r')
f = open('/Users/zhanghongwei/Documents/GitHub-Tower/LearnPython/PythonOfficial/fibo.py', 'r')
f = open('/Users/zhanghongwei/Documents/GitHub-Tower/LearnPython/PythonOfficial/fibo.py', 'r')
f = open('/Users/zhanghongwei/Documents/GitHub-Tower/LearnPython/PythonOfficial/fibo.py', 'r')
f = open('/Users/zhanghongwei/Documents/GitHub-Tower/LearnPython/PythonOfficial/fibo.py', 'r')


print(myDog.bad)




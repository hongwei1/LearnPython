#List 有序的集合,可以随时添加和删除元素.


classmates = ["Michael",'Bob','Tracy']
len(classmates)

classmates[0]
# classmates[3] # IndexError: list index out of range !
classmates[-1] # get the last element directly!


classmates.append('Adam')
classmates.insert(1,'Jack')

classmates.pop()
classmates.pop(2) # delete this position item.

classmates[1]="hongwei"

L = ['Apple',123, True]
S = ['Python', 'Java',['asp','php'],'scheme']



#2 tuple -- 另一种有序列表叫元组: tuple.  一旦初始化就不能被修改.
classmates = ('Michael','Bob','Tracy')
#没有append(). insert() 方法.代码更安全.

t=(1)
t=(1,)























print(123)
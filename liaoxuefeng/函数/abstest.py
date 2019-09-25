def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x # 必须又 return, 不然返回 None
    
    
# 通过条件+循环--> 非常复杂的逻辑.

my_abs(1)
# '2'+2
# while True:
#     try:
#         x = int(input("Pleaes enter a number:"))
#         print("we got your number: %s" % x)
#         break
#     except ValueError:
#         print("Tra again")
#         pass

import sys
for arg in sys.argv[1:]:
    try:
        # 1/0
        # f = open(arg, 'r')
        1
    except OSError:
        print('cannot open', arg)
    else:
        # print(arg, 'has', len(f.readlines()), 'lines')
        print( 'lines')
    finally:    
        print( 'finally')
    #     //f.close()
    
# try:
#     raise Exception("Span","eggs")
# except Exception as inst:
#     print(type(inst))
#     print(inst.args)
#     print(inst)
#     x,y = inst.args
#     print('x=', x)
#     print('y=', y)

# raise NameError('HiThere')    raise is the same as throw new exception
# raise ValueError


# def bool_return():
#     try:
#         return True
#     finally:
#         print(123)
#         return False
# bool_return()
# x,y =1,0
# 
# try:
#     result = x/y
# except OSError:
#     print("ZeroDivisionError")
# else:
#     print(123888)
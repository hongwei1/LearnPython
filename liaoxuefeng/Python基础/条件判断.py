age = 20
if age >= 18:  # : 必须写上!!!
    print('your age is',age) # 缩进原则: 没有{}只用缩进决定
    print('adult')
elif age >=6:
    print('teenager')
else:
    print('your age is',age)
    print('teenager')


birth = input('birth: ')

if(isinstance(birth, int)):
    if int(birth) < 2000:
        print('00前')
    else:
        print('00后')
else:
    print("You are wrong, must write the integer value")

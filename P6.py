a = float(input("a: "))
b = float(input("b: "))
if a == 0 and b == 0 :
    print('a/b =','Not defined')
elif a > 0 and b == 0:
    print('a/b =','Infinity')
elif a < 0 and b == 0 :
    print('a/b =','Negative infinity')
else :
    print('a/b =', a/b)

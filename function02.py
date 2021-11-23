b = 10
c = 20

def fun_sum(b, c):
    a = b + c
    return a

def fun_minus(b, c):
    a = b - c
    return a

def fun_mul(b, c):
    a = b * c
    return a

def fun_div(b, c):
    a = b / c
    return a

a1 = fun_sum    (b, c)
a2 = fun_minus  (b, c)
a3 = fun_mul    (b, c)
a4 = fun_div    (b, c)

print('더하기   : ',    a1)
print('빼기     : ',    a2)
print('곱하기   : ',    a3)
print('나누기   : ',    a4)



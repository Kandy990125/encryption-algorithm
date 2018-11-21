# -*- coding=UTF-8 -*-
# int ext_euclid(int a,int b, int &x, int &y) ;
'''' 扩展的欧几里得算法 '''''
def ext_euclid(a, b):
    a1 = max(a, b)
    b1 = min(a, b)
    return ext_algorithm(a1, b1)

def ext_algorithm(a, b):
    if b == 0:
         return 1, 0, a
    x2, y2, gcd = ext_euclid(b, a % b)
    tmp = x2
    x1 = y2
    y1 = tmp - int(a/b)*y2
    return x1, y1, gcd


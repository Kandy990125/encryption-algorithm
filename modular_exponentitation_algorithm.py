# -*- coding=UTF-8 -*-
# int modular_exponentitation(int a, int b, int n);
'''' 模幂运算 '''''
def binary_func(b):
    list = []
    list.append(b % 2)
    a = (b - b % 2) / 2
    while a >= 2:
        list.append(a % 2)
        a = (a - a % 2) / 2
    if a != 0:
        list.append(a)
    sorted_list = []
    i = len(list) - 1
    while i >= 0:
        sorted_list.append(list[i])
        i = i - 1
    return sorted_list
def modular_exponentitation(a, b, n):
    list = binary_func(b)
    # print list
    list_len = len(list)
    i = 0
    c = 0
    f = 1
    while i < list_len:
        c = 2 * c
        f = (f * f) % n
        # print list[i]
        if list[i] == 1:
            c = c + 1
            f = (f * a) % n
        i = i + 1
    return f

if __name__ == "__main__":
    print "模幂运算"
    a = input("请输入:")
    b = input("请输入:")
    n = input("请输入:")
    print "结果为:", modular_exponentitation(a, b, n)
# print (pow(7,560))%561
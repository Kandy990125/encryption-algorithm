# -*- coding=UTF-8 -*-
'''' 欧拉函数 '''''
import math
import sys
sys.setrecursionlimit(1000000)  # 设置为一百万
def judge(x):
    if x == 1:
        return True
    i = 2
    while i < math.sqrt(x):
        if x % i == 0:
            return False
        i = i + 1
    return True

def prime_num_list():
    i = 1
    list = []
    while i <= 1000:
        if judge(i):
            list.append(i)
        i = i + 1
    return list

def euler_func(n, list):
    if judge(n):
        return (n-1)
    i = 0
    for p in list:
        if p > n:
            break
        i = i + 1
    if i == len(list):
        i = i - 1
    while i >= 0:
        p = list[i]
        if n % p == 0 and (n / p) % p == 0:
            return (euler_func(n/p, list))*p
        if n % p == 0 and (n / p) % p != 0:
            return (euler_func(n/p, list)) * (p - 1)
        i = i - 1

def euler_main():
    list = prime_num_list()
    euler_list = []
    for n in range(1, 10001):
        euler_list.append(euler_func(n, list))
    return euler_list
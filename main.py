# -*- coding=UTF-8 -*-
from extended_Euclidean_algorithm import ext_euclid
from Euler_function_algorithm import euler_main
if __name__ == "__main__":

    # '''' 扩展的欧几里得算法 '''''
    #     print "使用扩展的欧几里得算法求最大公约数"
    #     a = input("请输入:")
    #     b = input("请输入:")
    #     print "x:", ext_euclid(a, b)[0]
    #     print "y:", ext_euclid(a, b)[1]
    #     print str("x*%d+y*%d=%d"%(max(a,b),min(a,b),ext_euclid(a, b)[2]))
    #     print "--------------------------------------"

    '''' 欧拉函数 '''''
    print "计算自然数n(100~10000)的欧拉函数Ø(n)."
    list = euler_main()
    while True:
        n = input("请输入想要查询的数字:(输入0退出)")
        if n == 0:
            break
        print "欧拉函数结果为:", list[n-1]
# 给定一个正数 n > 1 找到 n 的素因数分解。 结果将是一个具有以下形式的字符串：

#  "(p1**n1)(p2**n2)...(pk**nk)"
# p（i） 按递增顺序排列，n（i） 为空，如果 n（i） 为 1。

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
import math
def prime_factors(n):
    i=2
    while True:
        s=n-(int(math.log(n,i)))
print(math.log(78,5))
print(78/5)
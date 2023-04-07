#罗马数字解码器
# 现代罗马数字是通过表示要单独编码的数字的每个十进制数字来书写的，从最左边的数字开始并跳过任何 0。因此，1990 年呈现为“MCMXC”（1000 = M，900 = CM，90 = XC），2008 呈现为“MMVIII”（2000 = MM，8 = VIII）。1666年的罗马数字“MDCLXVI”按降序使用每个字母。

# 例：

# solution('XXI') # should return 21
# 帮助：

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

def solution(roman):
    c=0
    for i in list(roman):
        if i=='I':
            i=1
        if i=='V':
            i=5
        if i=='X':
            i=10
        if i=='L':
            i=50
        if i=='C':
            i=100
        if i=='D':
            i=500
        if i=='M':
            i=1000
        c=c+i
    return c
roman='XIX'
print(solution(roman))

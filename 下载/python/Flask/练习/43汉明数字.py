# 汉明数是形式为 2 的正整数我3j5k，对于某些非负整数 i、j 和 k。

# 编写一个函数来计算n千最小的汉明数。

# 具体说来：

# 第一个最小的汉明数是 1 = 203050
# 第二个最小的汉明数是 2 = 213050
# 第三个最小的汉明数是 3 = 203150
# 第四个最小的汉明数是 4 = 223050
# 第五个最小的汉明数是 5 = 203051
# 20个最小的汉明数在示例测试夹具中给出。

# 你的代码应该能够计算第一个（LC：，Clojure：，Haskell：，NASM，C，D，C++，Go和Rust：）汉明数而不会超时。5 0004002 00012 69113 282

# 数论算法
def hamming(n):
    k1,k2,k3=0,0,0
    res=[1]
    for i in range(0,n):
        s1=res[k1]*2
        s2=res[k2]*3
        s3=res[k3]*5
        min_val=min(s1,s2,s3)
        res.append(min_val)
        if res[i] ==s1:
            k1+=1
        if res[i] ==s2:
            k2+=1 
        if res[i] ==s3:
            k3+=1
    return res[-1]
print(hamming(1))
        

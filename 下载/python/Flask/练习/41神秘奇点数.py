# 描述：
# 这是一个相当简单但有趣的kata。尝试使用逻辑来解决它。最短的解决方案可以放入一条生产线中。

# 任务
# 关键是给出了一个自然数 N （1 <= N <= 10^9）。你需要编写一个函数来查找不超过 N 且不除以任何数字 [2， 3， 5] 的自然数。

# 例
# 让我们以数字 5 为例：

# 1 - 不将整数除以 2、3 和 5
# 2 - 将整数除以 2
# 3 - 将整数除以 3
# 4 - 将整数除以 2
# 5 - 将整数除以 5
# 答案： 1

# 因为只有一个数字不会将整数除以 2、3、5 中的任何一个

# 注意
# 同样，尝试想出一个公式来缩短您的解决方案并帮助您通过大型测试。

# 祝你好运:)

def real_numbers(n):
  x=n-n//2
  y=x-x//3
  z=y-y//5
  return z


print(real_numbers(7))#, 2))

print(real_numbers(5))#, 1))
print(real_numbers(10))#, 2))
print(real_numbers(20))#, 6))
print(real_numbers(30))#, 8))
print(real_numbers(40))#, 10))
print(real_numbers(55))#, 15))
print(real_numbers(66))#, 17))
print(real_numbers(75))#, 20))
print(real_numbers(100))#, 26))
list1=[]
for i in range(0,20,5):
    list1.append(i)


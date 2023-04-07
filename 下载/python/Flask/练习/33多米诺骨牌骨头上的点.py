# 描述：
# 要赚取巨额资金，您需要拥有非常规的心态。当然，如此复杂的工作，还必须有专门的娱乐娱乐机制。为此，赌场想出了一个特殊的多米诺骨牌。普通多米诺骨牌是两个图块的不同组合的集合，每个图块都显示到点。而这个集合是类似的瓷砖组合，但每个图块上的点数可以从零到一个取决于玩家智力水平的设定值。这个骰子集中有各种各样的瓷砖组合，但都不必重复（例如 和 等组合被认为是相同的）。 在制作这组多米诺骨牌时，制造商面临着计算所有多米诺骨牌上总点数的问题。这是因为多米诺骨牌上装饰着钻石，钻石是瓷砖上的点，必须在制造过程中估算其成本。062 | 55 | 2there's a domino, don't worry :)

# 输入数据：

# 函数 dots_on_domino_bones（） - 传递 n - 一个多米诺骨牌上的最大点数。

# 测试值为 -10 < n < 1000

# 输出数据：

# 您的函数应返回要为一组给定的骰子制作的钻石数量。

# 如果将小于零的数字传递给函数，则应输出 -1

# 例：

# 对于指关节上最大可能数量为 2 的多米诺骨牌，可能的指关节将如下所示 --> 、 、 ，因此，指关节上所有值的总和将是0 | 10 | 21 | 11 | 22 | 21 + 2 + 1 + 1 + 1 + 2 + 2 + 2 = 12

# dots_on_domino_bones(2) --> 12
# dots_on_domino_bones(3) --> 30
# dots_on_domino_bones(20) --> 4620
# dots_on_domino_bones(-3) --> -1
# 帮我写一个解决这个问题的程序。

# 如果有人有兴趣，您可以在此处阅读多米诺骨牌游戏的规则;)多米诺骨牌游戏
import re
def dots_on_domino_bones1(n):
    list1=[]
    num_add=0
    if n >0:
        for i in range(0,n+1):
            for x in range(0,n+1):
                if [i,x] not in list1 and  [x,i] not in list1:
                    list1.append([i,x])
        print(list1)
        for n in (re.findall(pattern='\d{1,3}',string=str(list1))):
            if int(n) >0:
                num_add=num_add+int(n)
        return num_add
    else:
        return -1
print(dots_on_domino_bones1(10))

#优化 减少循环
def dots_on_domino_bones(n):
 
    num_add=0
    if n >=0:
        for n in range(0,n+1): 
            num_add=num_add+n
        return num_add*(n+2)
    else:
        return -1
print(dots_on_domino_bones1(10))

 
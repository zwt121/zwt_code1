# 给定一个字符串和一个表示索引的整数数组，将给定索引处的所有字母大写。

# 例如：

# capitalize("abcdef",[1,2,5]) = "aBCdeF"
# capitalize("abcdef",[1,2,5,100]) = "aBCdeF".没有索引 100。
# 输入将是没有空格和数字数组的小写字符串。

# 祝你好运！

# 请务必尝试：

# 交替大写

# 字符串数组修订
s='askbjdja'
b=[]
ind=[1,3,4,5,100,10000000]
def capitalize(s, ind):
    s=list(s)
    try:
        for i in range(0,len(s)):
            if i in ind:
                b.append(s[i].upper())
            else:
                b.append(s[i])
        return ''.join(b)
    except BaseException as e:
         return ''.join(b)


        
print(capitalize(s,ind))

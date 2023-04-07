#Simple, given a string of words, return the length of the shortest word(s).

#String will never be empty and you do not need to account for different data types.

#给定一串单词，返回最短单词的长度。

# 字符串永远不会为空，并且您不需要考虑不同的数据类型
def find_short(s):
    a=s.split(' ')
    b=[]
    for i in a:
        b.append(len(i))
        
    b.sort()
    l=b[0]
    return l # l: shortest word length

s="bitcoin take over the world maybe who knows perhaps a"
print(find_short(s))
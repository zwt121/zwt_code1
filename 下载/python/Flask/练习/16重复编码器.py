# 本练习的目标是将字符串转换为新字符串，其中新字符串中的每个字符都是该字符在原始字符串中仅出现一次，或者该字符在原始字符串中出现多次。确定字符是否重复时忽略大小写。"("")"

# 例子
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 
# 笔记
# 断言消息可能不清楚它们在某些语言中显示的内容。如果您阅读，这是预期的结果，而不是输入！"...It Should encode XXX""XXX"
def duplicate_encode(word):
    #your code here
    word=str(word).lower()
    a=list(word)
    b=''
    print(a)
    for i in a:
        if a.count(i)==1:
           b=b+'('
        if a.count(i)>1:
           b=b+')'
    return b
print(duplicate_encode('Success'))
word='Success'
print(word.lower())






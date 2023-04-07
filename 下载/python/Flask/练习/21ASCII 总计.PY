# 您将获得一个字符串，并且必须将所有字符的总和作为 int 返回。该函数应该能够处理所有可打印的 ASCII 字符。

# 例子：

# uniTotal("a") == 97
# uniTotal("aaa") == 291
a='asdasd'
for i in a:
    print(i)
def uni_total(s):
    c=0
    for i in s:
        c=int(ord(i))+c
    return(c)

print(uni_total('aaa'))
# 完成解决方案，以便在传入的第一个参数（字符串）以第二个参数（也是字符串）结尾时返回 true。

#  例子：

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false
a="samurai"
b= "ra"
print(a[len(a)-len(b)::] )
def solution(text, ending):
    # your code here...
    if ending in text:
        if text[len(text)-len(ending)::]==ending:
            return True
        else: return False
    else:
        return False
print(solution(a,b))

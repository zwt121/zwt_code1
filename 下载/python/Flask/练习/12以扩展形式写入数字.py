# 以扩展形式写入数字
# 您将获得一个数字，您需要将其作为扩展形式的字符串返回。例如：

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
def expanded_form(num):
    b=[]
    a=list(str(num))

    for i in range(0,len(a)):
        if a[i]=='0':
            a[i]=' '
        else:
            c=(a[i]+(len(a)-i-1)*'0')
            if (len(a)-i-1)==0:
                c=(a[i]+(len(a)-i-1)*'0')
            b.append(c)
    return  ' + '.join(b)
num='7560756'
print(list(str(num)))
print(expanded_form(num))

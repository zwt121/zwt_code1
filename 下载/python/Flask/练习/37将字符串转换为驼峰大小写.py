# 完成方法/函数，以便它将破折号/下划线分隔的单词转换为驼峰大小写。仅当原始单词大写时，输出中的第一个单词才应大写（称为上骆驼大小写，通常也称为 Pascal 大小写）。接下来的单词应始终大写。

# 例子
# "the-stealth-warrior"转换为"theStealthWarrior"

# "The_Stealth_Warrior"转换为"TheStealthWarrior"

# "The_Stealth-Warrior"转换为"TheStealthWarrior"

# 正则表达式算法字符串
import re
def to_camel_case(text):
    result=[]
    re_text=re.sub(pattern='_|-',repl=' ',string=text)
    list_text=re_text.split(' ')
    for i in range(0,len(list_text)):
        if i==0:
            result.append(list_text[i])

        else:result.append(list_text[i].capitalize())
    
    return ''.join(result)
        


print(to_camel_case('the_stealth-Warrior'))
s='alskdnma'
print(s[0].isupper())
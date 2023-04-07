# 创建电话号码
# 编写一个接受 10 个整数（介于 0 和 9 之间）的数组的函数，该数组以电话号码的形式返回这些数字的字符串。

# 例
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# 返回的格式必须正确才能完成此质询。

# 不要忘记右括号后面的空格！

#我的方法
import re
def create_phone_number(n):
    string=str(n).replace(', ',"")[1:len(n)+1]
    one='('+(re.findall(pattern='(\d{3})\d{3}\d{4}',string=string))[0]+') '
    two=(re.findall(pattern='\d{3}(\d{3})\d{4}',string=string))[0]+'-'
    three=(re.findall(pattern='\d{3}\d{3}(\d{4})',string=string))[0]
    return one+two+three

# 最佳方法
def create_phone_number(n):
	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))


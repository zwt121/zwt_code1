# 在此示例中，您必须验证用户输入字符串是否为字母数字。给定的字符串不是 ，所以你不必检查它。nil/null/NULL/None

# 该字符串具有以下字母数字条件：

# 至少一个字符（无效）""
# 允许的字符是大写/小写拉丁字母和从 to 的数字09
# 无空格/下划线
import re
def alphanumeric(password):
    a=list(password)
    if '_' in a or ' ' in a:
        return False
    if re.findall(pattern='\W',string=password):
        return False
    
    if re.findall(pattern='[A-Za-z0-9]',string=password):
        return True
    else:
        return False
password=("PassW0rd")
print(alphanumeric(password))
print(re.findall(pattern='[A-Za-z0-9]',string=password))
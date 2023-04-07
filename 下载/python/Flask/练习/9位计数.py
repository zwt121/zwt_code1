# 描述：
# 编写一个函数，该函数将整数作为输入，并返回在该数字的二进制表示形式中等于 1 的位数。您可以保证输入是非负数。

# 示例：二进制表示形式为 ，因此在这种情况下应返回函数1234100110100105
import re
def count_bits(n):
    return len(re.findall(pattern='1',string=bin(n)))
    
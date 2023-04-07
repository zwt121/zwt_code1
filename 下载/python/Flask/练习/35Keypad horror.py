# 键盘布局有两个标准不方便！
# 电脑键盘布局：
# 7 8 9  \n
# 4 5 6  \n
# 1 2 3  \n
#   0 \n

# 手机键盘的布局：
# 1 2 3\n 
# 4 5 6\n  
# 7 8 9\n  
#   0\n

# 通过提供将计算机输入转换为数字的功能来解决非标准化键盘的恐怖，就像在手机上键入一样。

# 示例：“
# 789”->“123”

# 注意：
# 你得到一个只包含数字的字符串

def computer_to_phone(numbers):
    phone_number=''
    computer=['0','7','8','9','4','5','6','1','2','3']
    phone=['0','1','2','3','4','5','6','7','8','9']
    for i in numbers:
        if i in computer:
            phone_number=phone_number+phone[computer.index(i)]
    return phone_number
print(computer_to_phone('94561'))


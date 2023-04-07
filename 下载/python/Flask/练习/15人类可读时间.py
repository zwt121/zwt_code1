# 编写一个函数，该函数将非负整数（秒）作为输入，并以人类可读的格式（HH:MM:SS)

# HH= 小时，填充为 2 位数字，范围：00 - 99
# MM= 分钟，填充为 2 位数字，范围：00 - 59
# SS= 秒，填充为 2 位数字，范围：00 - 59
# 最长时间永远不会超过 359999 （99:59:59)

# 您可以在测试夹具中找到一些示例。
def make_readable(seconds):
    if seconds<=359999:
        hh=(seconds//3600)
        mm=(seconds%3600)//60
        seconds1=(seconds%60)
        if hh<=9:
            hh=f'0{hh}'
        if mm<=9:
            mm=f'0{mm}'
        if seconds1<=9:
            seconds1=f'0{seconds1}'
        
            
    return f'"{hh}-{mm}-{seconds1}"'
def make_readable(seconds):
    hours = seconds/3600
    min = (seconds%3600)/60
    sec = seconds%60
    return "{:02d}:{:02d}:{:02d}".format(hours,min,sec)
print(make_readable(61))


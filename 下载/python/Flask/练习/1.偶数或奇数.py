#创建一个函数，该函数将整数作为参数并返回偶数或奇数。"Even""Odd"

def fun1(a):
    if int(a)%2==0:
        print('偶数Even')
    if int(a)==0:
        print('0')
    if int(a)%2!=0:
        print('奇数Odd')

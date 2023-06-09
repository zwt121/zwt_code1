# 描述：
# 编写一个函数，该函数采用一个表示方格板尺寸的参数。板将始终是正方形的，因此 5 表示您将需要 5x5 板。

# 深色方块将由 unicode 白色方块表示，而浅色方块将由 unicode 黑色方块表示（相反的颜色确保板在代码战争的深色背景上看起来不会相反）。它应该返回一个板的字符串，每个方块之间都有一个空格，并考虑到新行。

# 偶数应返回以深色正方形开头的板。奇数应返回以浅色方块开头的板。

# 例子
# Input: 5

# Output:
# ■ □ ■ □ ■
# □ ■ □ ■ □
# ■ □ ■ □ ■
# □ ■ □ ■ □
# ■ □ ■ □ ■
# 每行末尾不应有尾随空格，字符串末尾不应有换行符。

# 注意
# 方块是字符，带有代码和.
# 不要对正方形使用 HTML 实体（例如 对于白色方块），因为代码不认为它是有效的正方形。检查解决方案是否在本地终端上打印了正确的棋盘格。■□\u25A0\u25A1□
def checkered_board(n):
    if n%2==1:
        for i in range(0,n):
            if i%2!=0:
                print('\u25A1')
            else:
                print('\u25A0')
            for x in range(0,n):
             pass
checkered_board(5)

for i in range(1,9):
    for x in range(1,9):
        print(f'{i}*{x}=={i*x}')
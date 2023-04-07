# # 您住在笛卡尔市，所有道路都以完美的网格布局。你提前十分钟到达约会，所以你决定趁机去散步。该市在手机上为其市民提供了一个步行生成应用程序 
# # - 每次您按下按钮时，它都会向您发送一个代表步行方向的单字母字符串数组（例如。['n'， 's'， 'w'， 'e']）。对于每个字母（方向），
# # 您总是只走一个街区，并且您知道穿越一个城市街区需要一分钟，因此创建一个函数，如果应用程序为您提供的步行将花费您正好十分钟（您不想早或晚！）
# # 并且会返回true，当然， 将您返回到起点。否则返回 false。
# # 注意：您将始终收到一个包含随机方向字母分类的有效数组（仅限“n”、“s”、“e”或“w”）。它永远不会给你一个空数组（这不是散步，那是静止不动！

# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, 
# so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones 
# -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
# You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, 
# of course, return you to your starting point. Return false otherwise.

# Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). 
# It will never give you an empty array (that's not a walk, that's standing still!).

def is_valid_walk(walk):
    x=0
    y=0
    a=(x,y)
    for i in walk:
        if i=='s':
            y=y+1
        if i=='e':
            x=x+1
        if i=='n':
            y=y-1
        if i=='w':
            x=x-1
    if len(walk)==10 and x==0 and y==0:
        return True
    else:
        return False

walk=('w','w','w','e','e','w','w','e','e','e')
print(is_valid_walk(walk))
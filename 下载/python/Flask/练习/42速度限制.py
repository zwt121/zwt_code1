# 警方已经放置了雷达，可以检测那些在该道路上超过限速的车辆。如果驾驶员的速度超过限速，罚款将是美元，如果超过罚款将是美元，如果超过30公里/小时，罚款将是美元。10km/h to 19km/h10020km/h to 29km/h250500

# 您将获得带有雷达的道路的速度限制，作为速度限制的集合，驾驶员的速度在所有道路上都相同，并且永远不会为负数，罚款金额将累积示例。[90,100,110,120,....]95km/h

# 例 (Speed=100, Signals=[110,100,80]-> 250)
def speed_limit(speed, signals):
    a=0
    if signals!=None:
        money=[]
        for i in signals:
            if 10<=int(speed)-int(i)<=19:
                money.append(100)
            if 20<=int(speed)-int(i)<=29:
                money.append(250)
            if int(speed)-int(i)>=30:
                money.append(500)
        if money==[]:
            return 0
        else:
            for x in money:
                a=a+x
        return a

print(speed_limit(60, [80, 70, 60]))
print(speed_limit(100, [110, 100, 80]))
print(speed_limit(130, [140, 130, 100]))
print(speed_limit(110, [120, 110, 100]))
print(speed_limit(220, [120, 110, 100]))
print(speed_limit(100, [70, 80, 90, 100]))
print(speed_limit(0, [15, 25, 35, 46]))
print(speed_limit(60, []))
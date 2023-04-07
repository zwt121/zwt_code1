#鸡兔同笼
def animals(heads, legs):
    
    if heads!=0 or legs!=0:
        if 1000>=heads>0 and 1000>=legs>0:
            if (legs%4)%2==0:
                Cows=legs//2-heads
                Chickens=heads-Cows
                if Chickens>=0 and Cows>=0:

                    return (Chickens,Cows)
                else:
                    return "No solutions"
            else:
                return "No solutions"
        else: 
            return "No solutions"
    else: 
        return (0,0)
    
print(animals(54, 956))
print(956%4%2)
# 编写一个方法，该方法将一个参数作为名称，然后问候该名称，大写并以感叹号结尾。

# 例：

# "riley" --> "Hello Riley!"
# "JACK"  --> "Hello Jack!"
a='riley'
print(a[0:1:1].upper())
print(a)
def greet(name): 
    name=name.lower()
    return f'Hello {name[0:1:1].upper()}{name[1::]}!'
print(greet(a))
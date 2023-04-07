# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.

# Going to one direction and coming back the opposite direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

# How I crossed a mountainous desert the smart way.
# The directions given to the man are, for example, the following (depending on the language):

# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
# or
# { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
# or
# [North, South, South, East, West, North, West]
# You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

# ["WEST"]
# or
# { "WEST" }
# or
# [West]
# Other examples:
# In , the direction is going north and coming back right away. ["NORTH", "SOUTH", "EAST", "WEST"]"NORTH" + "SOUTH"

# The path becomes , now and annihilate each other, therefore, the final result is (nil in Clojure).["EAST", "WEST"]"EAST""WEST"[]

# In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

# Task
# Write a function which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).dirReduc

# The Haskell version takes a b of directions with . data Direction = North | East | West | South
# The Clojure version returns nil when the path is reduced to nothing.
# The Rust version takes a slice of .enum Direction {North, East, West, South}
# See more examples in "Sample Tests:"
# Notes
# Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
# if you want to translate, please ask before translating.

# 曾几何时，在穿越古老的荒野西部山区的路上,...
# ...一个人被指示从一个点到另一个点。方向是“北”，“南”，“西”，“东”。显然，“北”和“南”是相反的，“西”和“东”也是对立的。

# 去一个方向，马上又回到相反的方向，是不必要的努力。由于这是狂野的西部，天气恶劣，水不多，所以为自己节省一些能量很重要，否则你可能会渴死！

# 我如何以聪明的方式穿越多山的沙漠。
# 例如，给男人的指示如下（取决于语言）：

# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
# or
# { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
# or
# [North, South, South, East, West, North, West]
# 你可以立即看到去“北”和立即“南”是不合理的，最好留在同一个地方！ 所以任务是给这个人一个简化版本的计划。在这种情况下，更好的计划很简单：
# ["WEST"]
# or
# { "WEST" }
# or
# [West]
# 其他例子：
# 在 中，方向是向北移动，然后马上回来。["NORTH", "SOUTH", "EAST", "WEST"]"NORTH" + "SOUTH"

# 路径变成，现在并相互湮灭，因此，最终结果是（在Clojure中为零）。["EAST", "WEST"]"EAST""WEST"[]

# 在[“北”、“东”、“西”、“南”、“西”、“西]中，”北“和”南“不是直接对立的，而是在”东“和”西“缩小后变成正对的，所以整个路径可以简化为[”西“、”西“]。

# 任务
# 编写一个函数，该函数将接受一个字符串数组并返回一个字符串数组，并删除了不必要的方向（W<->E 或 S<->N 并排）。dirReduc

# Haskell版本采用带有.data Direction = North | East | West | South
# 当路径减少为零时，Clojure 版本返回 nil。
# Rust 版本需要一部分 .enum Direction {North, East, West, South}
# 请参阅“示例测试：”中的更多示例
# 笔记
# 并非所有路径都可以变得更简单。 路径 [“北”、“西”、“南”、“东”] 不可简化。“北”和“西”，“西”和“南”，“南”和“东”不是直接对立的，不能变成这样。因此，结果路径本身是：[“北”，“西”，“南”，“东”]。
# 如果您想翻译，请在翻译前询问。
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
b=[]
west=-1
east=1
north=2
south=-2
for i in a:
    if i=='NORTH':
        i=north
    if i=='SOUTH':
        i=south
    if i=='WEST':
        i=west
    if i=='EAST':
        i=east
    b.append(i)
print(b)

    


            




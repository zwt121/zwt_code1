# 完成解决方案，使其去除传入的一组注释标记后面的所有文本。行尾的任何空格也应去除。

# 例：

# 给定一个输入字符串：

# apples, pears # and bananas
# grapes
# bananas !apples
# 预期的输出将是：

# apples, pears
# grapes
# bananas
# 代码将像这样调用：

# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"

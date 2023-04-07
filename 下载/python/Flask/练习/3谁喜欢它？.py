#您可能从Facebook和其他页面上知道“喜欢”系统。人们可以“喜欢”博客文章、图片或其他项目。我们希望创建应该显示在此类项目旁边的文本。

# 实现一个函数，该函数采用一个数组，其中包含喜欢某个项目的人的姓名。它必须返回显示文本，如示例中所示：
# []                              -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# 注意：对于 4 个或更多名称，其中的数字只会增加。"and 2 others"
def likes(names):
    if len(names)==0:
        return ("no one likes this")
    if len(names)==1:
        return(names[0]+' like this')
    if len(names)==2:
        return (names[0]+' and '+names[1]+' like this')
    if len(names)==3:
        return (names[0])+f', {names[1]}'+ f' and {names[2]} '+'like this'
    if len(names)>=4:
        return (names[0])+f', {names[1]} and {len(names)-2} other like this'

names=['zhuwt','th','ld','xyx','qwj']
print(likes(names))
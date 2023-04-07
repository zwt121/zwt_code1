# 您的任务是从字符串中删除所有连续的重复单词，只留下第一个单词条目。例如：

# "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
import re 
s="alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
print(re.search(pattern='(\w+) ',string=s))
def remove_consecutive_duplicates(s):
    pass
print(remove_consecutive_duplicates(s))
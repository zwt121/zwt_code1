# 营销团队花费了太多时间输入主题标签。
# 让我们用我们自己的标签生成器帮助他们！

# 这是交易：

# 它必须以井号标签 （） 开头。#
# 所有单词的首字母必须大写。
# 如果最终结果超过 140 个字符，则必须返回 。false
# 如果输入或结果为空字符串，则必须返回 .false
# 例子
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false
def generate_hashtag(s):
    if 0<len(s)<=140:
        list_s=str(s).split(' ')
        str_tag='#'
        for i in list_s:
            str_tag=str_tag+(i.capitalize())
        return str_tag
    else:return False
s='hjkl zdfvasdf zdfgsdfg'
print(generate_hashtag(s))
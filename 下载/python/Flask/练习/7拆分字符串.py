# 描述：
# 完成解决方案，以便将字符串拆分为两个字符对。如果字符串包含奇数个字符，则应将最后一对中缺少的第二个字符替换为下划线('_')。

# 例子：

# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']
import re 
string1='zhwuttzasdaasdasd'
string2='zhuutt'
b=[]
a=list(string1)
x=0

        

def solution(s):
    if len(s)%2==0:
        a=re.findall(pattern='\w{2}',string=s)
        return a
    if len(s)%2!=0:
        a=re.findall(pattern='\w{2}',string=s)
        b=list(s)
        c=(b[len(b)-1])+'_'
        a.append(c)
        return a
print(solution(string1))


 
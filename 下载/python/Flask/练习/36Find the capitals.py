# Instructions
# Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

# Example
# Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );

import re
def capitals(word):
    list_index=[]
    list_capitals=re.findall(pattern='[A-Z]',string=word)
    print(list_capitals)
    for i in list_capitals:
        list_index.append(word.index(i))
    return list_index
print(capitals('CWfZphDCVdMHguyPPTaNKeuM'))
        
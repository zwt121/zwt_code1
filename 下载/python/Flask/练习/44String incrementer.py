# DESCRIPTION:
# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.
import re
def increment_string1(strng):
    letter=re.findall(pattern='.+[\D]+',string=strng)
    print(letter,'===========letter===========')

    num=re.findall(pattern='[0-9]+',string=strng)
    print(num,'===========num===========')
    if letter==[] and num==[]:
        return '1'
    if letter==[]:
        strng=str(int(num[0])+1)
        return ('0'*(len(num[0])-len(strng)))+strng
    elif num==[]:
        return letter[0]+'1'

    else:
        strng=str(int(num[len(num)-1])+1)
        return letter[0]+('0'*(len(num[len(num)-1])-len(strng)))+strng
# print(increment_string("foo"))# "foo1"
# print(increment_string("foobar001"))# "foobar002"
# print(increment_string("foobar1"))# "foobar2"
# print(increment_string("foobar00"))# "foobar01"
# print(increment_string("foobar99"))# "foobar100"
# print(increment_string("foobar099"))# "foobar100"
# print(increment_string("fo99obar99"))# "fo99obar100"
# print(increment_string("001"))# "fo99obar100"
# print(increment_string("99"))# "fo99obar100"
# print(increment_string(""))# "fo99obar100"foobar00999
print(increment_string1("nk_&!{ZIE8884sCP?}E4A621707457z;883284560<{8bC$mEI\\=wrxo91270819J+PI1D960648331K^8e I?[00"))# "fo99obar100"foobar00999


#better
def increment_string2(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
print(increment_string2("nk_&!{ZIE8884sCP?}E4A621707457z;883284560<{8bC$mEI\\=wrxo91270819J+PI1D960648331K^8e I?[00"))# "fo99obar100"foobar00999

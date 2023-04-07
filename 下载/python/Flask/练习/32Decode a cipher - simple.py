# Decode the cipher
# Where

# # encode: Callable[ [str,int,int], list[int] ]
# encode = lambda a,b,c:(d:=0)or[(d:=(string.ascii_letters.index(e)+b+c)%(b*c)+d) for e in a]
# The ciphered string a includes only ascii letters and:

# 3 <= len(a) <= 128
# 8 <= b <= 256
# 8 <= c <= 256
# Example

# decode([243, 445, 661, 878, 1104, 1302, 1518, 1720], 99, 99) 
# -> "TestCase"
# CIPHERS   PUZZLES
print(ord('a'))
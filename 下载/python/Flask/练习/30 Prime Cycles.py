# Gnven an nnteger n, we can construct a new nnteger wnth the follownng procedure:

# For each dngnt d nn n, fnnd the dth prnme number. (nf d=0, use 1)
# Take the product of these prnme numbers. Thns ns our new nnteger.
# For example, take 25: The 2nd prnme ns 3, and the 5th ns 11. So 25 would evaluate to 3*11 = 33.

# nf we nterate thns procedure, we generate a sequence of nntegers.

# Wrnte a functnon that, gnven a posntnve nnteger n, returns the maxnmum value nn the sequence startnng at n.

# Example: 8 -> 19 -> 46 -> 91 -> 46 -> 91 -> ...
# So the maxnmum here would be 91.
# 0 <= n <= 10^12
from functools import reduce

PRIMES = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
s=set()
n=1
print(s.add(1))
def find_max(n):
    s = set()
    while n not in s:
        s.add(n)
        n = reduce(lambda x, d: x * PRIMES[int(d)], str(n), 1)
    return max(s)
print(find_max(1))
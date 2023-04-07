# Task
# zipWith ( or zip_with ) takes a function and two arrays and zips the arrays together, applying the function to every pair of values.
# The function value is one new array.

# If the arrays are of unequal length, the output will only be as long as the shorter one.
# (Values of the longer array are simply not used.)

# Inputs should not be modified.

# Examples
# zip_with( pow, [10,10,10,10], [0,1,2,3] )     =>  [1,10,100,1000]
# zip_with( max, [1,4,7,1,4,7], [4,7,1,4,7,1])  =>  [4,7,7,4,7,7]

# def add(a,b): return a+b; # or from operator import add
# zip_with( add,             [0,1,2,3], [0,1,2,3] )  =>  [0,2,4,6]  # Both forms are valid
# zip_with( lambda a,b: a+b, [0,1,2,3], [0,1,2,3] )  =>  [0,2,4,6]  # Both are functions
# Input validation
def barbell_weight(barbell):
    weight= {
        "---------c--------------------c---------": 25,
        "--------wc--------------------cw--------": 26,
        "-------bcr--------------------rcb-------": 34,
        "--------cW--------------------Wc--------": 35,
        "-------gcG--------------------Gcg-------": 47,
        "-------ycY--------------------Ycy-------": 58,
        "-----bcrBR--------------------RBrcb-----": 124,
        "-----cRRRR--------------------RRRRc-----": 225,
        "---gcBRRRR--------------------RRRRBcg---": 267
        }
    return weight[barbell]
# 25. Given a list of numbers, write a Python program to count positive and negative numbers in a List using
# function.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

def number(num):
    pos=0
    neg=0
    for i in num:
        if i>0: pos=pos+1 
        else: neg=neg+1
    print("positive no=",pos)
    print("negative=",neg)
number([2, -7, 5, -64, -14])                
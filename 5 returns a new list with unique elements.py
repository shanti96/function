# Q5.Write a Python function that takes a list and returns a new list with unique elements of the
# first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def list(num):
    num1=[]
    for i in num:
        if i not in num1:
            num1.append(i)
    print(num1)
list([1,2,3,3,3,3,4,5])            
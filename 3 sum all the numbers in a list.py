# Q3.Write a Python function to sum all the numbers in a list.

def add(*a):
    sum=0
    for i in a: 
        sum=sum+i
    print(sum)
add(8, 2, 3, 0, 7)        
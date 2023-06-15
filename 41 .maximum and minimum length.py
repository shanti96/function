# 41. Write a Python program to find the list with maximum and minimum length.
# Original list:[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])

def lenght(num):
    max=1
    min=1
    for i in num:
        if len(i)>=max:
            max=len(i)
            n=i
        if len(i)<=min:
            min=len(i)
            k=i
    print(max,n)  
    print(min,k)      
a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
lenght(a)                            
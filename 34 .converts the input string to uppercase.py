# Write a function which converts the input string to uppercase.
# For example:-
# [10, 14, 2, 23, 19] --> 42 (= 23 + 19)
# [99, 2, 2, 23, 19] --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.

def uppercase(list):
    a=0
    b=0
    for i in list:
        if a<i:
            a=i
        elif a!=b and b<i: 
            b=i
    sum=a+b
    print(str(sum))
num=[]    
for j in range(0,5):
    inte=int(input("enter the number"))    
    num.append(inte)
uppercase(num)               
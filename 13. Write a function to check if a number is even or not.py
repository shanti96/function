# 13.Write a function to check if a number is even or not.

def number(num):
    if num%2==0:
        print("even number=",num)
    else:
        print("not even number=",num)
a=int(input("take a number"))

number(a)             
# 49. Write a flowchart which takes an input N. Then input N numbers. Then for each of the N numbers, print
# “even” if the number is even or and “odd” if the number is odd.

def number(n):
    for i in range(0,n+1):
        num=int(input("take a number"))
        if num%2==0:
            print("Even")
        else:
            print("Odd")
a=int(input("take a number"))
number(a)                
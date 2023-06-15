# Q6.Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_number(num1):
    a=[]
    for i in num1:
        if i%2==0:
           a.append(i)
    print("even number=",a)
even_number([1, 2, 3, 4, 5, 6, 7, 8, 9])           
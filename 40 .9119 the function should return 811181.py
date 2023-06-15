# 40. Write a function For example, if we give 9119 the function should return 811181, as the square of 9
# is 81 and square of 1 is 1.

def square(num):
    a=""
    for i in range(0,len(num)):
        b=int(num[i])
        c=b*b
        a=a+str(c)
    return a
n=input('enter number') 
print(square(n))       

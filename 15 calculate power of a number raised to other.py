# 15.Write a function to calculate power of a number raised to other ( a b ) .

def num_power(a,b):
    c=0
    for i in range(a,b):
        if a<=b:
            c=c+1
    print("power of a number raised=",c)
num_power(2,4)            
# 16.Print multiplication table of 12 using function.

def table(num):
    for i in range(1,11):
        b=i*num 
        print(num,"*",i,"=",b)
a=int(input("take a number"))
table(a)        

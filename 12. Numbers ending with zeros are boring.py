# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105

def number(num):
    num=str(num)
    n=""
    for i in range(-1,-(len(num)+1),-1):
        if num[i]>"0":
            n=n+num[i]
            
        else:
            
a=int(input("enter the number"))
number(a)

# nested function practice set questions in python 
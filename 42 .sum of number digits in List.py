# 42. Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]

def digit(num):
    a=[]
    for i in num:
        b=0
        p=str(i)
        for j in range(0,len(p)):
            b=b+int(p[j])
        a.append(b)
    return a
n=[15, 81, 11, 234] 
print(digit(n))           
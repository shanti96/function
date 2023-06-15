# 31. Your goal is to return multiplication table for number that is always an integer from 1 to
# 10.For example, a multiplication table (string) for number == 5 looks like below:- 1 * 5 =5
# 2 * 5 =10
# 3 * 5 =15
# .
# .
# 10 * 5=50.

def table(num):
    for i in range(1,10+1):
        p=i*num
        print(i,"*",num,"=",p)
a=int(input("take a number"))
table(a)        
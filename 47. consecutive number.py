# 47. Draw a flowchart to take a list of 7 numbers from the user, print True if the complete list consists of
# consecutive numbers with any constant difference between numbers. Print False otherwise.

def consecutive(num):
    a=num[0]
    b=0
    for k in range(a,num[1]):
        b=b+1 
        k=k
    for i in num:
        if i==a:
            flag=True 
            a=b+a
        else:
            flag=False
            break
    if flag== True:
        print(True)
    else:
        print(False) 
n=[-5 ,-6 ,-7 ,-8] 
consecutive(n)                  
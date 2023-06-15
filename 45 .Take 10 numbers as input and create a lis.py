# 45. Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the user and update
# each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1

def multi(num):
    for i in num:
        if i%2==0:
            print(i*100)
        else:
            print(i*-1)
n=[]            
for j in range(0,10):
    p=int(input("take a number"))
    n.append(p)
multi(n)     
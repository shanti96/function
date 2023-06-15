# 44.Bonus - Given the same list, print the last ‘N’ elements in reverse order.
# Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]

def element(num):
    a=['a',1,'2',5,'b','q']
    for i in range(-1,-(num+1),-1):
        print(a[i])
n=int(input("take a number"))
element(n)        
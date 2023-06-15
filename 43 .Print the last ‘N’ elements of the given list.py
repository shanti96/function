# 43. Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. Print the last ‘N’ elements of the given list. ‘N’ is accepted from
# the user

def func(num):
    list1=['a',1,'2',5,'b','q']
    for i in range(-num,0,1):
        print(list1[i])
n=int(input("take a number"))
func(n)        
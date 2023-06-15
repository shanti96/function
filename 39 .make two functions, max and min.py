# 39. Your task is to make two functions, max and min (maximum and minimum in PHP and
# Python, maxi and mini in Julia) that take a(n) array/vector of integers list as input and outputs,
# respectively, the largest and lowest number in that array/vector.
# maximun([4,6,2,1,9,63,-134,566]) returns 566
# minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
# maximun([5]) returns 5.

def max_num(m):
    maximum=0
    for i in m:
        if maximum<i:
            maximum=i
    return maximum
a=[1,9,3,4,-134,63,566] 
print(max_num(a)) 

def min_num(min):
    minimum=0
    for j in min:
        if minimum>j:
            minimum=j
    return minimum
b=[-52,56,30,29,-54,0,-110]
print(min_num(b))            
# 38. Your task is to create function is Divided By (or is_divide_by) to check if an integer
# number is divisible by each out of two arguments.

def func(a,b,c):
    if a%b==0 and a%c==0:
        print(True)
    else:
        print(False) 
func(12,2,6)           
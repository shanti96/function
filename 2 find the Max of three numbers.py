# Q2. Write a Python function to find the Max of three numbers.
def max(a):
    count=0
    for i in a:
        if count<i:
            count=i
    print("maximum number=",count)           
max([12,3,9])           
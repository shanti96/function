# 46. Draw a flowchart to take a list of N numbers from the user, print True if the complete list consists of
# consecutive numbers with a difference of one. Print False otherwise.

def number(num):
    a=num[0] 
    for i in num:
        if i==a:
            flag=True
            a=a+1
        else:
            flag=False
            break
    if flag==True:
        print(True)
    else:
        print(False)        
n=[45 ,46 ,47 ,48 ,49 ,51 ,52] 
number(n)             
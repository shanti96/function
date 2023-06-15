# 48. Two numbers are entered through the keyboard. Write a flowchart to find the value of the
# raised to the power of another.

def keyboard(num1,num2):
    a=num1**num2
    return a
a=int(input("take a number"))
b=int(input("take the number"))
print(keyboard(a,b))    
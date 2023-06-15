# Q9.Write a Python program to generate and print a list of first and last 5 elements where
# the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

def square_value(num1,num2): 
    m=[] 
    a=[] 
    b=[] 
    for i in range(num1,num2+1): 
        if i<=5: 
            a.append(i*i) 
    m.append(a)        
    for j in range(num2,0,-1): 
        if j>=26: 
            b.append(j*j) 
    b.sort() 
    m.append(b) 
    print(tuple(m))                                            
square_value(1,30)            
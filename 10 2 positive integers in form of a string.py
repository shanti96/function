# Q10.Create a function that takes 2 positive integers in form of a string as an input, and outputs the
# sum (also as a string):
# "4", "5" --> "9"
# "34", "5" --> "39"
# Notes:
# If either input is an empty string, consider it as zero.

def num1(a,b):
    if a==" " and b==" ": 
        print("0")  
    elif a==" ":
        sum=0+int(b)
        print(str(sum))
    elif b==" ": 
        sum=0+int(a) 
        print(str(sum))      
    else:    
       sum=int(a)+int(b) 
       print(str(sum)) 
a=input("enter a number") 
b=input("enter b number")  
num1(a,b)  
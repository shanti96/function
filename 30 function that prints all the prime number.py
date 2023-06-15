# 30. Write a function that prints all the prime numbers between 0 and limit where limit is a
# parameter

# def prime_num(n):
#     for i in range(0,n+1): 
#         flag=True
#         for j in range(2,i+1): 
#             if i%j==0 and i!=j:
#                 flag=False
#                 break
#         if flag==True:
#             print("prime number=",i)    
# a=int(input("enter a number"))
# prime_num(a)                   

def prime_num(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
           count=count+1
    if count<=2:
        print("prime")
    else:
        print("not prime") 
n=int(input("enter the number"))         
prime_num(n)                  
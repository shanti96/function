# 14.Write a function to check if a number is prime or not.

def prime_no(num):
    a=2
    while a<=num//2:
        if num%a==0:
           print("not prime number",num)
           break
        a=a+1
    else:
        print("its prime number",num)
n=int(input("take a number"))           
prime_no(n)              
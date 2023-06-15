# 17. Write a function to tell user if he/she is able to vote or not.
# ( Consider minimum age of voting to be 18. )

# short heand if_else:#

def able_voting(age):
        print("able to voting")if age>=18 else print("not able for voting")
year=int(input("enter your age"))
able_voting(year)            

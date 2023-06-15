# Q1.Write a Python program to count the number of strings where the string length is 2
# the first and last characters are the same from a given list of strings.

#a=['abc', 'xyz', 'aba', '1221'] 
def count(a):
    result=0
    for i in a:
        if len(i)>=2 and i[0]==i[-1]:
            result=result+1
    print(result)
count(['abc', 'xyz', 'aba', '1221'])             
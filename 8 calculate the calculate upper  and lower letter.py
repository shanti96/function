# Q8.Write a Python function that accepts a string and calculate the number of upper case letters and
# lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12

def letter(string):
    upper=0
    lower=0
    for i in range(0,len(string)):
        valu=string[i]
        if valu>='A' and valu<='Z':
            upper=upper+1
        elif valu>='a' and valu<='z':
            lower=lower+1
    print("number of upper letter=",upper)
    print("number of lower letter=",lower)
letter('The quick Brow Fox')                
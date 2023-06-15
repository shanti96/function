def calculator(num1,num2,operation):
    if operation=="add":
        print(num1+num2)
    elif operation=="subtract" :
        print(num1-num2)
    elif operation=="multiply":
        print(num1*num2) 
    elif operation=="divid":
        print(num1/num2)
add=calculator(20,25,"add")
sub=calculator(40,3,"subtract")
multi=calculator(10,4,"multiply")
divid=calculator(40,4,"divid")            
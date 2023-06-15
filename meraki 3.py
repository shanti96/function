def check_number_list(num1,num2):
    if len(num1)==len(num2):
        for i in range(0,len(num1)):
            if num1[i]%2==0 and num2[i]%2==0:
                print("both are even number")
            else:
                print("both are not even number") 
check_number_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3,87]) 


# def add_numbers(number1, number2):
#   print("I will add two numbers.") 
#    print(number1 + number2) 
#  add_numbers(120, 50)
# num_x = 134 
# name = "Rinki"
# add_numbers(num_x, name)
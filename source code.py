#making a variable for results/outputs, to gather stuff in it
output = 0

# Asking What numbers you want using print command and it will repeat the question if the user doesn't put in a number
while True:
    #will try to get the number
    try:
        num1 = float(input("Hello, What is your First Number? "))
        num2 = float(input("Your Second Number? "))
        #will break the loop when user puts the right input(numbers)
        break
    #if user puts the wrong kinf of input, exception will be rised then loop will repeat the question 
    except ValueError:
        print("number needs to be a number")

# If selected operation is the following then do the following
def op():
    operation = input("Operation (+, -, *, /)?")
    if operation == "+":
        output=num1+num2
    elif operation == "-":
        output=num1-num2
    elif operation == "*":
        output=num1*num2
    elif operation == "/":
        output=num1/num2
    #if operation input is wrong, repeat the question
    else:
        op()
        print("wrong operation")
#print the result
print (output)


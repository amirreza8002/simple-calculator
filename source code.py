#so first we make an empty variable so we can put our result inside it

output = 0

# now we need to ask the user what numbers they want to work with, but since user might misclick and put in something other than a number
#we put a "while True" function, which will repeat the question forever

while True:

#"try" is a fuction we use when we expect something goes wrong, this will try what you want, and if it doesn't work, raises an exception
    try:
        #now we get numbers from user, and use the "float" methode to turn their input to actual numbers, because an input is always a str unless we make it otherwise
        num1 = float(input("Hello, What is your First Number? "))
        num2 = float(input("Your Second Number? "))
 #now we need to add a break, this will break the loop if user inputs numbers, so the loop doesn't go on forever
        break
    #if user puts the wrong kind of input, an exceptaion will be raised that will tell the user what they have done wrong
    except ValueError:
        print("number needs to be a number")

# now we make a function to get ask user what kind of operation they want to operate on those numbers
#the reason we don't do "try" and "except" here is because we cen't raise a value error, becuase we are not converting the input to numbers
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
    #if operation input is wrong:
    else:
        #tell the use what they have done wrong:
        print("wrong operation")
        #repeat the question of operation
        op()


#print the result
print (output)
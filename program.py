num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))


addition = num1 + num2
sub = num1 - num2
prod = num1 * num2
quo = num1 / num2


operation = input(("Choose operation you want to perform : \na.Sum\nb.Difference\nc.product\nd.quotient"))

if operation == "a":
    print("This is the sum of the two numbers : ", addition)
elif operation == "b":
    print("This is the difference of the two numbers : ", sub)          
elif operation == "c":
    print("This is the product of the two numbers", prod)         
elif operation == "d":
    print("This is the quotient from the division of the two numbers: ", quo)                                                    


n1 = int(input("Enter first number: "))
operation = input("Which operation would you like to perform? +, -, /, * : ")
n2 = int(input("Enter second number: "))

if operation == "+":
    print(n1+n2)
elif operation == "-" and n2>n1:
    print("First number should be greater than the second.")
elif operation=="-":
    print(n1-n2)
elif operation == "*":
    print(n1*n2)
elif operation == "/" and n2==0:
    print("Division by zero not possible.")
elif operation == "/":
    print(n1/n2)
else:
    print("Invalid operator")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /,  %, **): ")
if operator == '+':
    result = num1 + num2
    print(f"\nResults:\n{num1} + {num2} = {result} ")
elif operator == '-':
    result = num1 - num2
    print(f"\nResults:\n{num1} - {num2} = {result} ")
elif operator == '*':
    result = num1 * num2
    print(f"\nResults:\n{num1} * {num2} = {result} ")
elif operator == '/':
    result = num1 / num2
    print(f"\nResults:\n{num1} / {num2} = {result} ")
elif operator == '%':
    result = num1 % num2
    print(f"\nResults:\n{num1} % {num2} = {result} ")
elif operator == '**':
    result = num1 ** num2
    print(f"\nResults:\n{num1} ** {num2} = {result} ")
else:
    print("Oga you dey stress me biko ")


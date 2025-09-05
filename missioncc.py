num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+,-,*,/,%,**):)
if operator =='+':
    print(f"\nResults: ")
    print(f"{num1} + {num2} = {sum_result} ")
elif operator == '-':
    print(f"\nResults: ")
    print(f"{num1} - {num2} = {sub_result} ")
elif operator == '*':
    print(f"\nResults: ")
    print(f"{num1} * {num2} = {mult_result} ")
elif operator =='/':
    print(f"\nResults: ")
    print(f"{num1} / {num2} = {div_result} ")
elif operator == '%':
    print(f"\nResults: ")
    print(f"{num1} % {num2} = {mod_result} ")
elif operator == '**':
    print(f"\nResults: ")
    print(f"{num1} ** {num2} = {pow_result} ")
else:
    print ("oga no dey stress me biko. ")

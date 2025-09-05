while True:
	print("\n Simple Calculator ")
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	operation = input("Choose operation (+, -, *, /): ")
	if operation == "+":
		result = num1 + num2
	elif operation == "-":
		result = num1 - num2
	elif operation == "*":
		result = num1 * num2
	elif operation == "/":
		if num2 != 0:
			result = num1 / num2
		else:
			result = "Error! Division by zero."
	else:
		result = "invalid operation"
	print("Result: ", result)
	Choice = input("Do you want to continue ? (yes/no): ")
	if Choice.lower() == "no":
		print("Goodbye!")
	break

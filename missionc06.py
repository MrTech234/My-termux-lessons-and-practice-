while true:
	try:
		num1 = int(input("Enter the first number: "))
		num2 = int(input("Enter the second number: "))
		operator = input("+,-,/,*, ")
	except ValueErrors:
		print("invalid answer, try again. ")

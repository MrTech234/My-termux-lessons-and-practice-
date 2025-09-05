while True:
	try:
		num = int(input("Enter a number: "))
		print(f"Thanks! You entered: {num} ")
		break
	except valueError:
		print("Invalid input, try again. ")

try:
	score = int(input("Enter your score "))
	if score > 50:
		print("pass ")
	else:
		print("You are a failure, you can never make it! ")
except ValueError:
	print("Invalid input,please input your score ")


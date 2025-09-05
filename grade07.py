try:
	score = int(input("Enter the student's score (0-100) "))
	if score < 0 or score > 100:
		print("invalid number, please type a number between 0-100 ")
	elif score >= 90:
		print("Grade: A ")
	elif score >= 80:
		print("Grade: B ")
	elif score >= 70:
		print("Grade: C ")
	elif score >= 60:
		print("Grade: D ")
	else:
		print("Grade: F ")
except ValueError:
	print("Invalid input, please enter a number ")

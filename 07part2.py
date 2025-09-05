try:
	Class =int(input("How many students are in class "))
	if Class < 0 or Class > 100:
		print("Invalid number ")
	if Class > 50:
		print("score = 25 ")
	elif Class > 40:
		print("score = 40 ")
	elif Class > 30:
		print("score = 80 ")
	elif Class > 20:
		print("score = 30 ")
	else:
		print("12 ")
except ValueError:
	print("Invalid input, please enter the number of students present in class ")


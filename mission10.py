correct_username = "Ebubu"
correct_password ="1234"
attempts = 0
while attempts <3:
	username = input("Enter username: ")
	password = input("Enter password: ")
	if username == correct_username and password == correct_password:
		print("login successful ")
		break
	else:
		print("Incorrect, try again ")
		attempts += 1
if attempts == 3:
	print("Too many attempts. Access denied, yahoo boy go hustle ")


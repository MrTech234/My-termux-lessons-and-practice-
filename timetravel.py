age = int(input("Enter your age: "))
if age < 0:
    print("You're not even born yet. ")
elif age < 18:
    print("You're a teenager. ")
elif age < 60:
    print("You're an adult. ")
elif age < 100:
    print("You're a senior citizen. ")
else:
    print("You must be a vampire or a time traveler. ")

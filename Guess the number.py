import random

user_range1 = int(input("Enter the starting number of the range: "))
user_range2 = int(input("Enter the ending number of the range: "))
right_number = random.randint(user_range1, user_range2) #selecting a random integer from the range accepted.
print("I'm thinking of a number between " + str(user_range1) + " and " + str(user_range2) + ".")
s = 0

while True:
	user_guess = int(input("Enter your guess: "))
	if user_guess < right_number:
		print("You gussed too low")
		s += 1
	elif user_guess > right_number:
		print("You gussed too high")
		s += 1
	else:
		print("You gussed right!")
		s += 1
		break
print("You took", s, "gussess to guess the right number")
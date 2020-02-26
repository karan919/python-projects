import random

print("Guess the number between 0 and 20\n")
num = random.randint(0, 20)
user_input = input("Enter the number: ")
while num != user_input:
	if 0 > user_input or user_input > 20:
		print("Number not valid. Enter number between 0 and 20.")
		user_input = input("Enter the number: ")
	elif num > user_input:
		print("Guess is too low")
		user_input = input("Enter the number: ")
	elif num < user_input:
		print("Guess is too high")
		user_input = input("Enter the number: ")
print("Your guess is correct")


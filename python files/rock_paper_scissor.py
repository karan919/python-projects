import random

print("Rock, Paper & Scissor Game")
print("1 = Rock\n2 = Paper\n3 = Scissor\n")
play = 'y'
while play == 'y' or play == 'Y':
	choice = random.randint(1,3)
	user_input = input("Enter your choice: ")

	if user_input != choice:
		print("U Lose :(")
	else:
		print("U Win :)")
	play = input("Do you want to play again (y/n) :")

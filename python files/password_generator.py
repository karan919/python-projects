import random
import string

def randomPassword(len):
	pass_chars = string.ascii_letters + string.digits + string.punctuation
	return ''.join(random.choice(pass_chars) for i in range(len))

def generator():
	print("Password Generator\n")
	pass_len = int(input("Enter the number of length of the password you want: "))
	if pass_len < 6:
		pass_len = 6
	print(f"Password is : {randomPassword(pass_len)}")

generator()

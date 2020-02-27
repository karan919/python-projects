import random

def pick_random_word():
	with open('sowpods.txt', 'r') as f:
		words = list(f)
		return random.choice(words).strip()

def ask_user_for_next_letter():
	letter = input("Guess your letter: ")
	return letter.strip().upper()

def generate_word_string(word, guessed_letter):
	output = []
	for letter in word:
		if letter in guessed_letter:
			output.append(letter.upper())
		else:
			output.append("_")
	return "  ".join(output)

if __name__ == '__main__':
	WORD = pick_random_word()
	print(WORD)

	letters_to_guess = set(WORD)
	correct_letters_guessed = set()
	incorrect_letters_guessed = set()
	num_guesses = 0

	print("Welcome to hangman!")
	while len(letters_to_guess) > 0 and num_guesses < 6:
		guess = ask_user_for_next_letter()
		if guess in correct_letters_guessed or \
				guess in incorrect_letters_guessed:
			print("You already guessed that letter.")
			continue

		if guess in letters_to_guess:
			letters_to_guess.remove(guess)
			correct_letters_guessed.add(guess)
		else:
			incorrect_letters_guessed.add(guess)
			num_guesses+=1

		word_string = generate_word_string(WORD, correct_letters_guessed)
		print(word_string)
		print("You have {} guesses left".format(6 - num_guesses))

	if num_guesses < 6:
		print("Congratulations! You correctly guessed the word {}".format(WORD))
	else:
		print("Sorry, you list! Your word was {}".format(WORD))


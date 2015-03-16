#04_04_hangman_words
import random

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']

def pick_a_word():
	return random.choice(words)

print(pick_a_word())
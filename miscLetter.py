'''words that never appear double in wordlist'''

import scrabble
import string

letter_not_twice = []
for letter in string.ascii_lowercase:
	appears_twice = False
	for word in scrabble.wordlist:
		if letter*2 in word:
			appears_twice = True
			break
	if not appears_twice:
		print (letter)
		
for word in scrabble.wordlist:
	if word == word[::-1]:
		print (word + " is a palindrome")



# This python code acts as a Pig Latin Translator
# All you have to do is type in a word and it
# will translate it for you.

# pyg is going to be our placeholder for our 'ay' ending
pyg = 'ay'

# We use word here as a place holder inside of the if / else
# block that check for the first letter being a vowel or
# a consonant
word = ''

# This is how we get the promprt asking the user to input a word
original = raw_input('Enter Word Please: ')

# if / else block with a nested if / else block
# The outer if / else block checks to make sure that
# the user input a word of at least 1 letter and that it
# is actually a letter and not something else.
# The inner if / else block takes the first letter of the word
# and checks to see if it is a vowel or not. If it is, it adds
# the appropriate ending. If it is a consonant it takes
# first and moves it to the end of the word and adds the pyg ending
if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
		new_word = str(word) + pyg
		print new_word
	else:
		new_word = word[1:len(original)] + first +  pyg
		print new_word
else:
	print "empty"

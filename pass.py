import string
def passgen(a):
	s = string.ascii_letters
	s += string.ascii_digits
	s += string.ascii_punctuation
	i = 0
	while i<a:
		random.choice(s)

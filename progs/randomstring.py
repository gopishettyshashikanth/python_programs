import random
import string

n = input("enter a number")

for i in range(n):
	char_set = string.ascii_uppercase + string.digits
	print "Username : ", ''.join(random.sample(char_set*6, 6))

	char_set = string.ascii_uppercase
	"Password : ", ''.join(random.sample(char_set*6, 6))
	
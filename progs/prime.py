num = input("enter a number")

if num > 1:

	for i in range(2, num):
		if num % i == 0:
			print("not aprime")
			break	
	else:
		print("prime")
else:
	print("not aprime")



myNum=input("what you want to do + - / * :")
print(myNum)

num1 = input("enter first number :")
num2 = input("enter second number :")


if(myNum == "+"):
	num = int(num1) + int(num2)
	print(num)
elif(myNum == "-"):
	num = int(num1) - int(num2)
	print(num)
elif(myNum == "*"):
	num = int(num1) * int(num2)
	print(num)
elif(myNum == "/"):
	num = int(num1) / int(num2)
	print(num)	
else:	
	print("invalid operation")

 
numbers=[]
num = input("enter number of elements : ")
for i in range(num): 
	num1 =input("enter a number : ") 
	numbers.append(num1)

odd=[]
even=[]
for j in numbers:
	if(j%2 == 0):
		even.append(j)
	else:
		odd.append(j)

print("The even list",even)
print("The odd list",odd)

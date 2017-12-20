num=[]
num1=input("enter number of elements: ")

for i in range(num1):
	num2 = input("enter a number : ")
	num.append(num2)
	
num.sort()
print(num[num1-1])

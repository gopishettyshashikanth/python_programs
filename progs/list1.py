class Lists:

	empcount = 0
	def __init__(self,id,name,add):
		self.id=id
		self.name=name
		self.add=add
		empcount=empcount+1


	def __del__(self):
		print("destructor")	

e1 = Lists(1,'a','z')
e2 = Lists(2,'b','x')
print("Total no of employes : ", empcount)
class obj:
	count = 0
	def __init__(self,id,name):
		print("init")
		self.id=id
		self.name=name
		obj.count += 1


	def display(self):
		print "ID : ", self.id,  ", Name: ", self.name
		
	def objcount(self):
		print "Number of Employes :",obj.count

ob1 = obj(1,"abc")
ob2 = obj(2,"xyz")
ob1.display()
ob2.display()
ob1.objcount()


class Demo:

	def __init__(self):
		
		self.a=100
		self.b=200
		print("init")

	def dispaly(self):
		print(self.a)
		print(self.b)

	def modify(self):
		print("after modify")
		self.a = self.a +100
		self.b = self.b +100		

ob=Demo()
ob.dispaly()
ob.modify()
ob.dispaly()


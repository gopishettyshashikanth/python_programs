class Cust:

	def __init__(self,cname,cacno,cadd,cbal):
		self.cname = cname
		self.cacno = cacno
		self.cadd = cadd
		self.cbal = cbal

	def deposit(self,cd):
		self.cbal = self.cbal+cd

	def withdraw(self,cw):

		if (cw < self.cbal) :
		  	self.cbal = self.cbal-cw
		else:
		 	print "amount is more cbal"

	def display(self):
		print self.cbal

c=Cust("shashi",100,"IN",1000)
c.deposit(100)
c.withdraw(200)
c.display()			

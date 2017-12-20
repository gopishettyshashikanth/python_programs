class test:

	def __init__(self):
		print("initialization")

	def dis(self):
		print("display")

	def __del__(self):
		print("delete")	

t=test()
t.dis()
t=test()


class rectangle():
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		print(self.length*self.breadth)
obj=rectangle(10,20)
obj.area()

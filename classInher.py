class BaseClass:
	def __init__(self, myName = None):
		self.name = myName
		self.nLeg = 2
	
	def disp(self):
		print("name is ",self.name)
		print("Base nLegs is", self.getmylegs())
	
	def getmylegs(self):
		return self.nLeg
	
class Child1Class(BaseClass):
	def __init__(self, noOfLegs = 4):
		#does not work 
		#BaseClass.__init__("legged")
		#error AttributeError: 'str' object has no attribute 'name'
		BaseClass.__init__(self)
		self.name = "legged"
		self.nLeg = noOfLegs
	
	def disp(self):
		print("child's name is",self.name)
		print(", no of legs=", self.getmylegs())
	
	def getmylegs(self):
		return self.nLeg
		

bc = BaseClass("Shweta")
bc.disp()

cc1 = Child1Class(8)
cc1.disp()
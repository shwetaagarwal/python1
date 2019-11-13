class BasicClass:
	def __init__(self, myName = None):
		self.name = myName
	
	def disp(self):
		print("name is ",self.name)
	
bc = BasicClass("Shweta")
bc.disp()
print(bc.__class__)
#print( bc.__name__)
print(bc.__bases__)
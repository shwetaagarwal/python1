class Girl:
	#static attribute,must be initialised, shared by all objects of the class? if assigned using object then it reamins changed?
	#so is it just a way to give a default initial value to all objects initialised
	gender = 'unknown'
	def __init__(self,name):
		#instance attribute, do not belong to the class
		self.name = name
	
	def getName(self):
		print(self.name)

r = Girl('Rachel')
s = Girl('Stanky')
print(r.gender)
print(s.gender)
r.getName()
s.getName()
r.name = 'abc'
r.getName()
#the following is not an error/exception, but not advised.
#r.gender = 'm'
print(r.gender)
print(s.gender)
Girl.gender = 'female'
print(r.gender)
print(s.gender)
print('Girl.gender',Girl.gender)

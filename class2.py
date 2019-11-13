class Employee:
	def __init__(self,fname,sname,pay):
		self.fname = fname
		self.sname = sname
		self.pay = pay
		
emp1_data = ['reema','khana',4000]
emp2_data = ['seema','Dhana',8000]

emp1 = Employee(*emp1_data)
emp2 = Employee(*emp2_data)

print(emp1.pay)
emp1.pay = 6000
print(emp1.pay)

# declare a class
class myClass():

	# declare a varaible
	legs = 0


	# declare a method with parameter
	def name(self, arg):
		self.legs = arg
		print(self.legs)




# instentiate a class
x = myClass()

# calling a method from class
x.name(10)








# inheritate a class. In bracket (), you must right the name of the class 
# from where you want to inheritant 

class newClass(myClass):

	# calling a methon from parent class
	def test(self, myInp):
		myClass.name(self, myInp)




# instentiate the child class
y = newClass()

# calling mehtod from child class
y.test(100)

		






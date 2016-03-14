'''
 * -----------------------------------------------
 * 	Class for Linked List algorithm
 * -----------------------------------------------
 * 	This class working for Linked list algorithm 
 * 	with python programming laguage. Its working 
 * 	for lists and recursion method. 
'''




# declaring a class name node
class nodeClass(object):

	# call a constructor of for this class that will 
	# instentiate during calling the class. 
	# The constructor has 2 parameters where both of 
	# the parameters take none value by default.  

	def __init__(self, cargo=None, next=None):
	    self.cargo = cargo
	    self.next  = next

	def __str__(self):
		return str(self.cargo)





# instentiate or creating object for the class
# due to OOP you are able to create different 
# objects as much as you want 

node1 = nodeClass("IIUM # 1")
node2 = nodeClass("IIUM # 2")
node3 = nodeClass("IIUM # 3")
node4 = nodeClass("IIUM # 4")
node5 = nodeClass("IIUM # 5")
node6 = nodeClass("IIUM # 6")
node7 = nodeClass("IIUM # 7")



# linking one object with next object by assing 
# whole class in the next property in the class
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7



# defining a fucntion for prining value from last value
def print_backward(list):
	
	# if list is empty then represent by Non that is an empty list
	if list == None: return

	# putting the element in list array as head
	head = list

	# whatever is in head, add next element of head as tail
	tail = list.next

	# now print this function here with tail variable as a parameter that return the last value
	print_backward(tail)
	print(head)




# Calling the function to print everything
print_backward(node1)
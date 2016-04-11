'''
 * -----------------------------------------------
 * 	Class for Linked List algorithm
 * -----------------------------------------------
 * 	This class working for Linked list algorithm 
 * 	with python programming laguage. Its working 
 * 	for removing 2nd elements from list
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



	def removeSecond(self, list):
		if list == None: return
		first = list
		second = list.next

		# make the first node refer to the third
		first.next = second.next

		# separate the second node from the rest of the list
		second.next = None
		return second




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




# defining a function for printing list
def print_my_whole_list(node):

	# implimenting while loop if node parameter is not empty
	while node:

		# print node parameter whatever it containes as value
	    print(node),
	    node = node.next


print_my_whole_list(node1)
print("-----------------------")



myNode = nodeClass()

myNode.removeSecond(node1)



# finally calling the function with the first link from where linking will be statrted
print_my_whole_list(node1)
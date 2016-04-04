# Binary Search
# ----------------------------------------
# the following code will work search item 
# in the list whether it is available in 
# the list or not. this program will 
# equally divided the whole list
# and go ahed until found or
# not found in the list


# this function will work as a binar search

def binarySearch(myItem, myList):
	found = False
	bottom = 0
	top = len(myList)-1

	while bottom <= top and not found:
		middle = (bottom+top)//2

		if myList[middle] == myItem:
			found = True
		elif myList[middle] < myItem:
			bottom = middle + 1
		else:
			top = middle - 1

	# return true or false
	return found




# next line will execute all the codes in this file
if __name__ == "__main__":

	# defined list
	versity = [10, 20, 30, 40, 50, 60, 70, 80, 90]

	# convert the input into intiger
	item = int(input("What item you are looking for? "))

	isItFound = binarySearch(item, versity)
	
	if isItFound:
		print("Your item is in the list")
	else:
		print("Your item is not in the list")

# Linear search
# -------------------------
# the following code will work search item 
# in the list whether it is available in 
# the list or not


# this function will work as a linear search
def linearSearch(myItem, myList):
	found = False
	position = 0

	while position < len(myList) and not found:
		if myList[position] == myItem:
			found = True
		position = position + 1
	return found



# next line will execute all the codes in this file
if __name__ == "__main__":

	# defined list
	versity = ["IIUM", "UM", "UTM", "UPM", "UKM"]
	item = input("What item you are looking for? ")

	isItFound = linearSearch(item, versity)
	
	if isItFound:
		print("Your item is in the list")
	else:
		print("Your item is not in the list")

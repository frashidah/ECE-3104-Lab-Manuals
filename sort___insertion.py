# /**
#  *    This program will do insertion with python. 
#  *    For example,  
#  *    [11, 22, 44, 33, 55, 95, 65, 75]
#  *	[11, 22, *, *, *, *, *, *]
#  *	[11, 22, 44, *, *, *, *, *]
#  *	[11, 22, 33, 44, *, *, *, *]
#  *	[11, 22, 33, 44, 55, *, *, *]
#  *	[11, 22, 33, 44, 55, 95, *, *]
#  *	[11, 22, 33, 44, 55, 65, 95, *]
#  *	[11, 22, 33, 44, 55, 65, 75, 95]
#  */   



def insertionSort(myList):

	for indexnumber in range(1,len(myList)):
		currentvalue = myList[indexnumber]
		position = indexnumber

		while position > 0 and myList[position-1] > currentvalue:
			myList[position] = myList[position-1]
			position = position-1

		myList[position]=currentvalue

myList = [54,26,93,17,77,31,44,55,20]
insertionSort(myList)
print(myList)

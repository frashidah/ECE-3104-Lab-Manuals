# /**
#  *    This program will do Selection Sort with python. 
#  *    For example,  
#  *    [11, 22, 44, 33, 55, 95, 65, 75]
#  *	[11, 22, 44, 33, 55, 75, 65, 95]
#  *	[11, 22, 44, 33, 55, 65, 75, 95]
#  *	[11, 22, 44, 33, 55, 65, 75, 95]
#  *	[11, 22, 33, 44, 55, 65, 75, 95]
#  *	[11, 22, 33, 44, 55, 65, 75, 95]
#  * 	[11, 22, 33, 44, 55, 65, 75, 95]
#  */   



def selectionSort(myList):
	for lastValue in range(len(myList)-1, 0, -1):
		positionOfMaxValue = 0

		for location in range(1, lastValue+1):
			if myList[location] > myList[positionOfMaxValue] :
				positionOfMaxValue = location

		temp = myList[lastValue]
		myList[lastValue] = myList[positionOfMaxValue]
		myList[positionOfMaxValue] = temp


myList = [51, 45, 88, 41, 35, 66, 99, 69, 71]


selectionSort(myList)

print(myList)
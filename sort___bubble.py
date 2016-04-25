# /**
#  *    This program will do bubble sort with python. 
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



def bubbleSortImplementation(myList):

	#for (i= length(myList)-1; i > 0; i-- )
    for slicedNumber in range(len(myList)-1,0,-1):

    	# for (i = 0; i < slicedNumber; i++)
        for i in range(slicedNumber):

        	# if( array[0] > array[1] )
            if myList[i] > myList[i+1]:
                # store in temporary list
                temp = myList[i]
                # store small value in first position
                myList[i] = myList[i+1]

                # make temp = small value
                myList[i+1] = temp



myList = [11, 22, 44, 33, 55, 95, 65, 75]
bubbleSortImplementation(myList)
print(myList)

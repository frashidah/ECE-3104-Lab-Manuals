# /**
#  *    This program will do merge sort with python. 
#  *    For example,  
#  *    [11, 22, 44, 33, 55, 95, 65, 75]
#  *    [11, 22, 44, 33]        [55, 95, 65, 75]
#  *    [11, 22] [44, 33]       [55, 95] [65, 75]
#  *    [11] [22]   [44] [33]   [55] [95]   [65] [75]
#  *    [11] [22]   [33] [44]   [55] [95]   [65] [75]
#  *    [11, 22] [33, 44]       [55, 95] [65, 75]
#  *    [11, 22, 33, 44]        [55, 65, 75, 95]
#  *    [11, 22, 33, 44, 55, 65, 75, 95]
#  */   




def mergeSort(myList):
    print("Splitting ", myList)

    # execute if length is more than 1
    if len(myList) > 1:

        # find the middel point and make it floor
        mid = len(myList)//2

        # getting first part of the list
        lefthalf = myList[:mid]

        # getting last part of the list
        righthalf = myList[mid:]

        # calling self function for left split
        mergeSort(lefthalf)

        # calling self function for right portion split
        mergeSort(righthalf)

        i=0
        j=0
        k=0


        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                myList[k]=lefthalf[i]
                i=i+1
            else:
                myList[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            myList[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            myList[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ", myList)

myList = [11, 22, 44, 33, 55, 95, 65, 75, 85, 105, 155, 145, 135, 115, 125]
mergeSort(myList)

print(myList)
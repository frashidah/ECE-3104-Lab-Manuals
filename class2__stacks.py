

# creating a list
myList = [1024, 3, True, 6.5]

# append an item in the list
myList.append("IIUM")


# insert an item in specific position
myList.insert(2, 'UM')


# pop an item
myList.pop()


# pop an item from specific position
myList.pop(2)


# count the length of the list
print(len(myList))




# check whether a list is empty or  not. There are two ways to check this. 

# if len(listName)==0:
# 	Your condition

# another way is-

# if not listName:
# 	Your condition

if len(myList) == 0:
	print("Its empty")
else:
	print('not empty')

# alternative way

if not myList:
	print("Its empty")
else:
	print('not empty')



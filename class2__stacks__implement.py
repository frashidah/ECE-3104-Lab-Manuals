
# declare a variable
size = 5

# define an empty list
myList = []



# starting while loop to check wheather length of current array is less than 
# our defined size or not. If less than, will take item from user untill it
# reached to end of the defined size

while len(myList) < size:
	# ask user to give input
	newItem = input("Add Your Item: ")

	# append new user input
	myList.append(newItem)

	# print updated list
	print(myList)
	




# check whether the length of myList is equal to defined size or not
if len(myList) == size:
	print("You need to pop an item to add more.")
	confirm = input("Do you want to pop the last item? (y/n) :")


	# check whether user key in y or not
	if confirm == 'y':
		print("Your last item has poped out")

	# if user key in n 
	elif confirm == 'n':
		print("Thank you for keeping your list alive")
		print("Sorry, You can not add more element because your list has overflown already")





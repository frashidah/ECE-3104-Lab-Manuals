'''
---------------------------------------------
	ARRAY ( 1st Class with Python)
---------------------------------------------
| This program will give a basic idea of
| array or list in Python. It code has 
| written only for ECE 3104 Students in 
| Engineering in IIUM. 
|

'''


# receive username
username = input("What is your name? ")

counter = len(username)


for i in range(0, counter):
	print(username[counter-1])
	counter = counter - 1


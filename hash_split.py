# /**
#  * put a list of date into a varibale
#  * @type {String}
#  */
demoLine = "077, Mr X, Malaysia, 167cm, Male, 70"


# define an empty dictionary
stuff = {}


# assign value in stuff dictionary
(stuff['code'], stuff['name'], stuff['home'], stuff['height'], stuff['gender'], stuff['weightkg']) = demoLine.split(",")



# displaying all the elements from the dictionary
print("your code is: " + stuff['code'])
print("your name is: " + stuff['name'])
print("your home is: " + stuff['home'])
print("your height is: " + stuff['height'])
print("your gender is: " + stuff['gender'])
print("your weightkg is: " + stuff['weightkg'])

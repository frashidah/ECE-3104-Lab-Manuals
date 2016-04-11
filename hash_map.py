# /*
# |--------------------------------------------------------------------------
# | HashMap Class
# |--------------------------------------------------------------------------
# |
# | This is the HashMap class to implement Hash Mapping implimentation 
# | for python programming lanagauge. This code only for educational
# | purpose for ECE 3104 Lab Class in Enginnering of IIUM.
# |
# */



# defining the class
class HashMap(object):

	# defining the constructor for the class 
	# that always call during class intentiontion
	def __init__(self):
		self.size = 6

		# defining the map size none by force
		# for eample-
		#  -----------------------
		# | 0 | 1 | 2 | 3 | 4 | 5 |
		#  -----------------------
		# | 0 | 0 | 0 | 0 | 0 | 0 |   
		self.map  = [None] * self.size




	# declare a private class called hash 
	# that make hashing given parameter
	def _get_hash(self, key):
		hash = 0

		# separte each letter from given pararmeter 
		for char in str(key):

			# Given a string of length one, return 
			# an integer representing the Unicode 
			# code and add into hash variable.
			# For example, ord(a) return 
			# integer 97.
			hash += ord(char)

		# for exmple, it will return 97%6 = 1
		return hash % self.size






	# define function add with two paraemter that need to be added 
	# and where given value should be added
	def add(self, key, value):

		# make hash of given key
		key_hash = self._get_hash(key)
		
		# now store key_value as a value and key
		key_value = [key, value]


		if self.map[key_hash] is None:

			# if map is not empty then create a list with key_value
			# for example ['name' = 'alex']
			self.map[key_hash] = list([key_value])
			return True

		else: 
			for pair in self.map[key_hash]:
				if pair[0] == key:
					pair[1] = value
					return True
			self.map[key_hash].append(key_value)
			return True




	# define a method to get a particulr value 
	# with a key in list
	def get(self, key):
		key_hash = self._get_hash(key)
		if self.map[key_hash] is not None:
			if pair[0] == key:
				return pair[1]
		return None




	# delete a key from the list with  particular position
	def delete(self, key):
		key_hash = self._get_hash(key)

		if self.map[key_hash] is None:
			return False

		for i in range(0, len(self.map[key_hash])):
			if self.map[key_hash][i][0] == key:
				self.map[key_hash].pop(i)
				return True



	# printing all the values
	def echo(self):
		print('--- Phonebook ---')

		for item in self.map:
			if item is not None:
				print(str(item))







# instentiate the class and make it an object 
h = HashMap()



# add value in list by calling add
h.add('Bob', '525-5689')
h.add('Alex', '525-8579')
h.add('Alex', '525-8578')
h.add('Jeffrey', '525-9657')
h.add('Way', '525-8579')
h.add('Mark', '525-9567')
h.add('Suchi', '525-8578')


# priting all the elemenent from list
h.echo()


# delete a particular item from list based on key
h.delete('Suchi')

# print whole list after deletion a particular item
h.echo()
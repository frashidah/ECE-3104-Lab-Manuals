#Initialize a table of zeros. 10 is the table size.
table = [0] * 10


# define hash function that return parameter % by 10
def hash_function(x): 
	return x % 10


# define a insert function that will takes 3 parameter
# where first is table name, 2nd the input that need 
# to be hash and 3rd the value that will be 
# stored associated with input
def insert(table,input,value): 
	table[hash_function(input)] = value




# now call the insert function and add value with 
# a particular list position . 
insert(table, 1,'apple')
insert(table, 3,'banana')
insert(table, 4,'tangerine')


# Now print the whole table list
print(table)
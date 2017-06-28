import this

# STRINGS
this_is_string = 'hello'
this_is_string += ' world'

this_is_string.upper()
this_is_string.lower()
this_is_string.capitalize()

# NUMBERS
number = 42

number - 1
number * 2

other_number = 10
number + other_number	

float_number = 40.2

# NONE
this_is_none = None

# BOOLEAN

this_is_false = False
this_is_true = True
this_is_true = not this_is_false

# LIST / slicing

this_is_list = [1,2,3,4]
this_is_list.append('coisa')
 
this_is_list[5]
this_is_list[2:4]
this_is_list[-1]

# DICT
this_is_dict = {
	'key': 'value'
	'another_key': 'another_value'
	1: 'value!'
}


# OPERATORS
a = 1
a == 1
a in [1,2,3]

a < 2
a >= 1

# Math
a + 2
a - 2
a * 2
a ** 2
a / 2
a % 2

# Boolean
a = True
b = False
a or b
a and b
a is True
b is None


# Functions

def do_stuff():
	print('doing stuff!')

def return_stuff():
	return 'stuff'

def do_stuff_with_my_stuff(x):
	return x * 2

def do_stuff_with_many_stuff(x, y, z=10):
	return (x + y) * z

def do_stuff_with_variable_stuff(*args, **kwargs):
	print(args)
	print(kwargs)

a = do_stuff()
print(a)

a = return_stuff()
print(a)

x = 10
y = do_stuff_with_my_stuff(x)
print(x)
print(y)

a = do_stuff_with_many_stuff(1,1)
print(a)

# CONTROL FLOW

a = True

if a:
	print('success!')
else:
	print('error')

def classify(a):
	if a < 5:
		print('{} is smaller then 5'.format(a))
	elif 5 <= a <= 15:
		print('{} is between 5 and 15'.format(a))
	else:
		print('{} is more then 15'.format(a))

# REPETITION

a = range(10)
a = [0,1,2,3,4,5,6,7,8,9]

for value in a:
	print "#"*value

total = 10

while total > 0:
	print "#"*total
	total -=1


# CLASSES AND OO 
class Animal:
	def __init__(self, name):
		self.name = name
		self.age = None

	def noise(self):
		pass

	def set_age(self, age):
		self.age = age

class Dog(Animal):
	def noise(self):
		print("{}: woof!".format(self.name))

	def set_age(self,age):
		self.age = age * 7

class Cat(Animal):
	def noise(self):
		print("{}: meow!".format(self.name))

	def set_age(self,age):
		self.age = age * 10

d = Dog('Fuba')
c = Cat('Pamonha')

d.noise()
c.noise()

d.set_age(5)
c.set_age(5)

print(d.age)
print(c.age)

#!/usr/bin/python
#MITx 600SC Introduction to Computer Science and Programming

#LEC2
#Branching Program
#Limited im what can be done
#Length of time to run, based on size of program.

def branching_program():
	x = int(raw_input('Branch, Enter an integer :'))
	if x%2 == 0:
		print 'Even'
	else:
		print 'Odd'
	if x%3 != 0:
		print 'And not by 3'


#Looping Construct
#Turimg Complete
#Find the cube root of a perfect cube

#Exhastive Enumeration while loop
def looping_program():
	x = int(raw_input('Loop, Enter an Integer :'))
	ans = 0
	while ans*ans*ans < abs(x):
		ans = ans + 1
		#print 'current guess =', ans
	if ans*ans*ans != abs(x):
		print x, 'is not a perfect cube'
	else:
		if x < 0:
			ans = -ans
		print 'Cube root of ' + str(x) + ' is ' + str(ans)


#LEC3
#Decrimenting Function
#1)Map set of program variables to an integer
#2)Starts with a non-negative number
#3)when value is <= 0 it terminates
#4)Decreaed each iteration.

#In this case its 8

#Exhastive Enumeration for loop
def forloop_program():
        x = int(raw_input('Forloop, Enter an Integer :'))
        ans = 0
        for ans in range(0, abs(x)+1):
		#print 'current guess =', ans
        	if ans**3 == abs(x):
			break
        if ans**3 != abs(x):
                print x, 'is not a perfect cube'
        else:
                if x < 0:
                        ans = -ans
                print 'Cube root of ' + str(x) + ' is ' + str(ans)

#Range (x,y) = (x,x+1,....,y-1)
#For loops make life easier than while loops, shorthand. Nothing wrong with while loops

#Approximation
#Find a y such thant y*y = x+-E
#Square root
def forloopfloat_program():
	x = 12345
	epsilon = 0.01
	numGuesses = 0
	ans = 0.0
	while abs(ans**2 - x) >= epsilon and ans <= x:
		ans += 0.00001
		numGuesses += 1
	print ' numGuesses =', numGuesses
	if abs(ans**2 - x) >= epsilon:
		print 'Failesd on Square root of', x
	else:
		print ans, 'is close to square root of', x


#Bisection Serach
#1)Cut search space in half each iteration
def bisect_program():
        x = 0.5
        epsilon = 0.01
        numGuesses = 0
	low = 0.0
	high = max(x, 1.0) 
        ans = (high + low)/2.0
        while abs(ans**2 - x) >= epsilon and ans <= x:
		print 'low =', low, 'high =',high, 'ans =',ans
		numGuesses += 1
                if ans**2 < x:
			low = ans
		else:
			high = ans
		ans = (high + low)/2.0
      	print ' numGuesses =', numGuesses
	print ans, 'is close to square root of', x

#LEC4
#Functions
#Decomposition - Creates structure into modules - Self-Contained, Reusable.
#Abstraction - Supresses Detail
#Functions have, a name, paramaters, body
def function_example():
	def withinEpsilon(x, y, epsilon):
		 """x,y,epsilon floats. epsilon > 0.0
		    returns True if x is within epsilon of y"""
		 return abs(x - y) <= epsilon

	#print withinEpsilon(3,2,1)
	#val = withinEpsilon(2,3,0.5)
	#print val

	def f(x):
		x = x + 1
		print 'x =', x
		return x
	x = 3
	z = f(x)
	print 'z =', z
	print 'x =', x

#1) The formal paramater, X, is bound to the value of the actual paramater, X
#2)Upon entry of the function, a new scope is created

#A scope is a mapping from names to objects
#Scopes are evaluated into stack frames, main scope, function scope, sub function scope, when sub
#function completes it exits the tack


#LEC5
#Tuples, Lists, Dictionaries.

#Test = (1, 2, 3, 4, 5)
#print Test[1] 
#print Test[-1]
#len(test)

def tuple_example(): 
	x = 100
	divisors = ()
	for i in range(1,x):
		#print divisors
		if x%i == 0:
			divisors = divisors+(i,)
			print divisors
	print divisors[1: 3]
	print len(divisors)

#Slice - Subsequence of tuple or list
#Lists, more usefel than tuples and more complicated.
#Tuples are immutable, cannot change values in tuple
#Lists are mutable, can change values in object - Mutability
#Append is a Method in python - an alternative syntax to writing a function.
#append(L, e) L.append(e) - Mutates L, i,e, side effect

def lists_example():
	Techs = ['MIT' ,'Cal Tech']
	Ivys = ['Harvard' ,'Yale', 'Brown']
	Univs = []
	Univs.append(Techs)
	print 'Univs =', Univs

	Univs.append(Ivys)
	print 'Univs =', Univs
	for e in Univs:
		print 'e =', e

	flat = Techs + Ivys
	print flat
	
	Arts = ['Art Center', 'Harvard']
	for x in Arts:
		if x in flat:
			flat.remove(x)
	print flat

	flat.sort()
	print flat
	flat[1] = 'Umass'
	print flat

#Need to be aware of peril when using mutations.
def lists_example2():
	L1 = [2]
	L2 = [L1, L1]
	print 'L2 =', L2
	L1[0] = 3
        print 'L2 =', L2
	L2[0] = 'a'
	print 'L2 =', L2
	L1 = [2]
	print 'L2 =', L2

#Alias - one object with multiple names, with Immutable aliasing aliasing is harmles
#with multiple names for same mutable object, its something to worry about.
def copy_list():
	def copyList(lsource, ldest):
		for e in lsource:
			ldest.append(e)
			print 'ldest =', ldest
	L1 = []
	L2 = [1,2,3]
	copyList(L2,L1)
	print L1
	print L2

#Dictionaries
#1)elements are not ordered
#2)indicies (keys) can be any immutable type, not just integers.
#dict is a set of key value pairs
#Dictionaries are sets not sequences 

def dictionary_example():
	e2f = {'one': 'un', 'two': 'deux', 'pi': '3.14159',\
		'wine': 'du vin'}
	print e2f


dictionary_example()
#copy_list()
#lists_example2()
#lists_example()
#function_example()
#bisect_program()
#forloop_program()
#branching_program()
#looping_program()
#forloopfloat_program()

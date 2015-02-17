#Assignment 1 python : program to find and test gcd
def gcd(a,b):

	#Exception checking
	x = (((type(a) == int) or (type(a) == long)) and((type(b) == int) or (type(b) == long)))
	try:
		if (x!= True):
			raise TypeError
		elif(a<0 or b<0):
			raise ValueError
		else:
		#program to find gcd
			while(b!= 0):
				a,b = b,a%b
			print "GCD calculated successfully"
			return a
	
	#Exception Handling
	except TypeError:
		if((type(a) == int) or (type(a) == long)): 	#Type of a is right
			print "Type Error in b"
		else:
			if((type(b) == int) or (type(b) == long)): #Type of b is right
				print "Type Error in a"
			else: 		#Type of a & b is wrong 
				print "Type Error in a and b"
		return "TypeError"

	except ValueError:
		if(a<0 and b<0):
			print "Value Error: Both a and b arguements are negative"
		elif(a<0):
			print "Value Error: a is negative"
		else:
			print "Value Error: b is negative"
		return "ValueError"	
#EOF program

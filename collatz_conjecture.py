# this first function cwill be called automatically when running 
# 'python collatz.conjecture.py' into the terminal 

def collatz(n):
	"""
	This function will return everything: 
	- the number of steps between n and the last number (always 1)
	- the sequence or serie of numbers from the given number n and 1
	You will get a message to explain which values are returned.
	"""
	# when n is not defined from start as an integer (but floating number)
	if isinstance(n, int) == False:
		n = int(n)
		print(f"You need an integer for starting value, so your input will be {n}")

	assert n >=1, "You need an integer >= 1"

	steps = 0
	serie = [n]

	while n != 1:
		if n % 2 == 0:
			n = int(n/2)

		else:
			n = int(3*n+1)
		serie.append(n)
		steps += 1

	else:
		print(f"You reached the end of the Collatz sequence with {steps} steps and the serie:\n{serie}")

# This part is to run the function directly from the terminal
n = input("which number would you like to start with?>")
collatz(n)



## shorter function to only get the values
def collatz_sequence(n: int):
	"""
	The function will return the serie of values between n (given starting point, in the argument)
	to the final value 1
	"""
	assert n >=1, "You need an integer >= 1"

	serie = [n]

	while n != 1:
		if n % 2 == 0:
			n = int(n/2)

		else:
			n = int(3*n+1)
		serie.append(n)

	return serie

def collatz_step_number(n: int):
	"""
	This function will return the number of steps between n 
	(starting given value in argument and the last number (always 1)
	"""
	assert n >=1, "You need an integer >= 1"

	steps = 0

	while n != 1:
		if n % 2 == 0:
			n = int(n/2)

		else:
			n = int(3*n+1)
		steps += 1

	return steps



def fibonacci(n: int):
	if n == 1 or n == 0:
		return n
	return fibonacci(n-1) + fibonacci(n-2)

# This part is for when you run the file directly from the terminal
#n = input("which number would you like to start with?>")
#fibonacci(n)
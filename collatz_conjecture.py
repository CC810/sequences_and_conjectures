def collatz_sequence(n):

	if isinstance(n, int) == False:
		n = int(n)
		print(f"You need an integer for starting value, so your input will be {n}")

	assert n >=1, "You need an integer >= 1"

	steps = 0

	while n != 1:
		if n % 2 == 0:
			n = int(n/2)

		else:
			n = int(3*n+1)
		print(n)
		steps += 1

	else:
		print(f"You reached the end of the Collatz sequence with {steps} steps.")

# This part is to run the file directly from the terminal
n = input("which number would you like to start with?>")
collatz_sequence(n)
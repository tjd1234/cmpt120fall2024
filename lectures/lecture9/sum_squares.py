# sum_squares.py

def sum_squares(begin, end):
	""" Returns the sum of the squares of the numbers from begin to end.
	Demonstrates the accumulator pattern.

    For example, sum_squares(8, 11) returns the value of 8**2 + 9**2 + 10**2 + 11**2.
	"""
	total = 0
	for i in range(begin, end + 1):
		total += i ** 2    # += means "add to"

	return total
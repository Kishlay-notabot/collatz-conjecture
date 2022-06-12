def HailstoneNumbers(N, c):
	print(N, end=" ")
	if (N == 1 and c == 0):

		return c
	elif (N == 1 and c != 0):

		c = c + 1
	elif (N % 2 == 0):

		c = c + 1
		c = HailstoneNumbers(int(N / 2), c)
	elif (N % 2 != 0):

		c = c + 1
		c = HailstoneNumbers(3 * N + 1, c)
	return c
endpoint = int(input('Enter end point: '))
startpoint = int(input('Enter start point: '))
for N in range (startpoint, endpoint+1):
	print('\n')
	HailstoneNumbers(N, endpoint)
print('\n')
input('Press ENTER to exit')


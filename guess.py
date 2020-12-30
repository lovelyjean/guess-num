import random

r = random.randint(1, 100)

while True:
	num = input('please guess a number: ')
	num = int(num)
	if num == r:
		print('Correct!')
		break
	else:
		if num > r:
			print('the answer is smaller than ', num)
		else:
			print('the answer is larger than ', num)
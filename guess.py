import random

r = random.randint(1, 100)
cnt = 0

while True:
	num = input('please guess a number: ')
	num = int(num)
	cnt = cnt + 1
	if num == r:
		print('Correct!')
		print('you have guessed ', cnt , 'times')
		break
	else:
		if num > r:
			print('the answer is smaller than ', num)
		else:
			print('the answer is larger than ', num)

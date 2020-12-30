import random
start = input('please define the start number: ')
end = input('please define the end number: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
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
	print('you have guessed ', cnt , 'times')		
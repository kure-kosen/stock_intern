print('数値を入力')
num = input('>>>  ')
for i in range(1, int(num)+1):
	if ((i % 3 == 0) and (i % 5 == 0)):
		print('fizzbuzz')
	elif (i % 3 == 0):
		print('fizz')
	elif (i % 5 == 0):
		print('buzz')
	else:
		print(i)
		

import random

random_str = ''

number_lenth = input('Please enter the lenth of the random number: ')

for i in range(int(number_lenth)):
	i = random.randint(0, 9)
	random_str += str(i)

print(random_str)

import random
print("Welcome to the Dice Roller! \n")
pick = ""
def four():
	roll = random.randint(1, 4)
	return roll
def six():
	roll = random.randint(1, 6)
	return roll
def eight():
	roll = random.randint(1, 8)
	return roll
def ten():
	roll = random.randint(1, 10)
	return roll
def twelve():
	roll = random.randint(1, 12)
	return roll
def twenty():
	roll = random.randint(1, 20)
	return roll
def perc():
	roll = random.randint(1, 100)
	return roll
def dandd():
	a = six()
	b = six()
	c = six()
	roll = a + b + c
	return roll
def choice():
	print("""
	Which die to you wish to cast: \n
	1 = 4 Sided \n
	2 = 6 Sided \n
	3 = 8 Sided \n
	4 = 10 Sided \n
	5 = 12 Sided \n
	6 = 20 Sided \n
	7 = Percentile 
	8 = 3D6 \n
	0 = QUIT
	""")
	pick = input()
	if pick == '1': 
		print(four())
	elif pick == '2':
		print(six())
	elif pick == '3':
		print(eight())
	elif pick == '4':
		print(ten())
	elif pick == '5':
		print(twelve())
	elif pick == '6':
		print(twenty())
	elif pick == '7':
		print(perc())
	elif pick == '8':
		print(dandd())
	elif pick == '0':
		print("Thanks for playing!")
		exit = True
	else:
		print("Your choice doesn't make sense! Try again, Please.")
while pick != '0':
	choice()

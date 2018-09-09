#this goes with sudoku - this cranks out lines consisting of 81 random 1 -9's separated by commas to use with sudoku
import random
import math
def crunchOutNums():
	print("This is the number cruncher, It will create strings of numbers you can use with sudoku checker,")
	# prob rendundant, but code opens file and truncates it to delete old content, then reopens
	file = open("nums.txt", "r+")
	file.truncate(0)
	cycles = input("Enter the number of sudoku checker lines to generate: ")
	cycles = int(cycles)
	numsLength = 81
	numStr = ""
	snip =""
	def genNums():#returns random num between 1 and 9
		cNum = random.randint(1,9)
		return cNum
	def passNums():#not smart enough to randomly create passing num string, so we're faking it
		numStr ="4,5,2,3,9,1,8,7,6,3,1,8,6,7,5,2,9,4,6,7,9,4,2,8,3,1,5,8,3,1,5,6,4,7,2,9,2,4,5,9,8,7,1,6,3,9,6,7,2,1,3,5,4,8,7,9,6,8,5,2,4,3,1,1,8,3,7,4,9,6,5,2,5,2,4,1,3,6,9,8,7"
		return numStr
	if math.isnan(cycles) is True:
		print("You didn't enter a number, try again")
	elif cycles < 0 or cycles > 100:
		print("number too high or too low, try again")
	for x in range(cycles):
		luck = genNums()#gen random
		if luck % 2 == 0:# evaluates random - if even, get's faked passing string (4 out of 9 chance)
			numStr = passNums()
		else:
			for y in range(numsLength):
				current = genNums()
				if y == 80:
					snip = str(current)
				else:
					snip= str(current)+","
				numStr = numStr + snip
		numStr = numStr + "\r"
		file.write(numStr)
		numStr = ""
	file.close()
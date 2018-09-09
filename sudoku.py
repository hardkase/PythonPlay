#intent - read in string of 81 nums comma separated
#for loop to read lines
# either split each line into 81 element list by replacing ',' or strip non numbers into long string
#messy, but do lists or arrays for rows 1-9, cols A - I, and grid 1-9 (27 lists!!!)
#first for loop reads each string/list, puts value in col
#second foor loop evals by 9(or 8 with list indexing), placing in column
#third for loop, or nested if, evaluates line index by 3s to place grids
# first job, call each row array and check for dupes - if yes, return False
#second job, call each col array and check for dupes - if yes, return False
#third job, check each grid array and check for dupes - if yes, return False
#if no dupes found return True
#pass in numcrunch as module and run first?
#have any False break and return?
import numcrunch
import collections
import re
numcrunch.crunchOutNums()
file = open("nums.txt", "r+")
row1 = list()
row2 = list()
row3 = list()
row4 = list()
row5 = list()
row6 = list()
row7 = list()
row8 = list()
row9 = list()
colA = list()
colB = list()
colC = list()
colD = list()
colE = list()
colF = list()
colG = list()
colH = list()
colI = list()
grid1 = list()
grid2 = list()
grid3 = list()
grid4 = list()
grid5 = list()
grid6 = list()
grid7 = list()
grid8 = list()
grid9 = list()
def makePuzzle():
	puzzle = list()
	puzzle.append(row1)
	puzzle.append(row2)
	puzzle.append(row3)
	puzzle.append(row4)
	puzzle.append(row5)
	puzzle.append(row6)
	puzzle.append(row7)
	puzzle.append(row8)
	puzzle.append(row9)
	puzzle.append(colA)
	puzzle.append(colB)
	puzzle.append(colC)
	puzzle.append(colD)
	puzzle.append(colE)
	puzzle.append(colF)
	puzzle.append(colG)
	puzzle.append(colH)
	puzzle.append(colI)
	puzzle.append(grid1)
	puzzle.append(grid2)
	puzzle.append(grid3)
	puzzle.append(grid4)
	puzzle.append(grid5)
	puzzle.append(grid6)
	puzzle.append(grid7)
	puzzle.append(grid8)
	puzzle.append(grid9)
	return puzzle
def checkForDupes(puzzle):#this isn't working...!
#let's try another example
	"""
	def FindDuplicates(in_list):  
		unique = set(in_list)  
		for each in unique:  
			count = in_list.count(each)  
			if count > 1:  
				print 'There are duplicates in this list'  
				return True  
		print 'There are no duplicates in this list'  
		return False  
	"""
	global validate
	validate = True
	for x in puzzle:
		dupes = set(x)
		if len(dupes) < len(x):
			print("Culprit!: " + str(x))
			validate = False
			break
		dupes.clear()
	return validate
	
for x in file:
	x = re.sub("[^0-9\,]","", x)
	#print(x)
	rawNums = x.split(",")
	rawNums = [int(i) for i in rawNums]
	#for y in rawNums:
	#print(rawNums)
	#print(len(rawNums))
	#for idx, val in enumerate(ints):
	for idx, val in enumerate(rawNums):
		#print(idx)
		#print("[" +str(val)+ "]")
		if idx >= 0 and idx < 9:
			row1.append(val)
			if idx >= 0 and idx < 3:
				grid1.append(val)
				if idx == 0:
					colA.append(val)
				elif idx == 1:
					colB.append(val)
				else:
					colC.append(val)
			elif idx >=3 and idx < 6:
				grid2.append(val)
				if idx == 3:
					colD.append(val)
				elif idx == 4:
					colE.append(val)
				else:
					colF.append(val)
			elif idx >=6 and idx <9:
				grid3.append(val)
				if idx == 6:
					colG.append(val)
				elif idx == 7:
					colH.append(val)
				else:
					colI.append(val)
		elif idx >= 9 and idx < 18:
			row2.append(val)
			if idx >= 9 and idx < 12:
				grid1.append(val)
				if idx == 9:
					colA.append(val)
				elif idx == 10:
					colB.append(val)
				else:
					colC.append(val)
			elif idx >=12 and idx < 15:
				grid2.append(val)
				if idx == 12:
					colD.append(val)
				elif idx == 13:
					colE.append(val)
				else:
					colF.append(val)
			else:
				grid3.append(val)
				if idx == 15:
					colG.append(val)
				elif idx == 16:
					colH.append(val)
				else:
					colI.append(val)
		elif idx >= 18 and idx < 27:
			row3.append(val)
			if idx >= 18 and idx < 21:
				grid1.append(val)
				if idx == 18:
					colA.append(val)
				elif idx == 19:
					colB.append(val)
				else:
					colC.append(val)
			elif idx >=21 and idx < 24:
				grid2.append(val)
				if idx == 21:
					colD.append(val)
				elif idx == 22:
					colE.append(val)
				else:
					colF.append(val)
			else:
				grid3.append(val)
				if idx == 24:
					colG.append(val)
				elif idx == 25:
					colH.append(val)
				else:
					colI.append(val)
		elif idx >= 27 and idx < 36:
			row4.append(val)
			if idx >= 27 and idx < 30:
				grid4.append(val)
				if idx == 27:
					colA.append(val)
				elif idx == 28:
					colB.append(val)
				else:
					colC.append(val)
			elif idx >=30 and idx < 33:
				grid5.append(val)
				if idx == 30:
					colD.append(val)
				elif idx == 31:
					colE.append(val)
				else:
					colF.append(val)
			else:
				grid6.append(val)
				if idx == 33:
					colG.append(val)
				elif idx == 34:
					colH.append(val)
				else:
					colI.append(val)
		elif idx >= 36 and idx < 45:
			row5.append(val)
			if idx >= 36 and idx < 39:
				grid4.append(val)
				if idx == 36:
					colA.append(val)
				elif idx == 37:
					colB.append(val)
				else:
					colC.append(val)
			elif idx >=39 and idx < 42:
				grid5.append(val)
				if idx == 39:
					colD.append(val)
				elif idx == 40:
					colE.append(val)
				else:
					colF.append(val)
			else:
				grid6.append(val)
				if idx == 42:
					colG.append(val)
				elif idx == 43:
					colH.append(val)
				else:
					colI.append(val)
		elif idx >= 45 and idx < 54:
			row6.append(val)
			if idx >= 45 and idx < 48:
				grid4.append(val)
				if idx == 45:
					colA.append(val)
				elif idx == 46:
					colB.append(val)
				else:
					colC.append(val)
			elif idx >=48 and idx < 51:
				grid5.append(val)
				if idx == 48:
					colD.append(val)
				elif idx == 49:
					colE.append(val)
				else:
					colF.append(val)
			else:
				grid6.append(val)
				if idx == 51:
					colG.append(val)
				elif idx == 52:
					colH.append(val)
				else:
					colI.append(val)
		elif idx >= 54 and idx < 63:
			row7.append(val)
			if idx >= 54 and idx < 57:
				grid7.append(val)
				if idx == 54:
					colA.append(val)
				elif idx == 55:
					colB.append(val)
				else:
					colC.append(val)
			elif idx >=57 and idx < 60:
				grid8.append(val)
				if idx == 57:
					colD.append(val)
				elif idx == 58:
					colE.append(val)
				else:
					colF.append(val)
			else:
				grid9.append(val)
				if idx == 60:
					colG.append(val)
				elif idx == 61:
					colH.append(val)
				else:
					colI.append(val)
		elif idx >= 63 and idx < 72:
			row8.append(val)
			if idx >= 63 and idx < 66:
				grid7.append(val)
				if idx == 63:
					colA.append(val)
				elif idx == 64:
					colB.append(val)
				else:
					colC.append(val)
			elif idx >=66 and idx < 69:
				grid8.append(val)
				if idx == 66:
					colD.append(val)
				elif idx == 67:
					colE.append(val)
				else:
					colF.append(val)
			else:
				grid9.append(val)
				if idx == 69:
					colG.append(val)
				elif idx == 70:
					colH.append(val)
				else:
					colI.append(val)
		else:
			row9.append(val)
			if idx >= 72 and idx < 75:
				grid7.append(val)
				if idx == 72:
					colA.append(val)
				elif idx == 73:
					colB.append(val)
				else:
					colC.append(val)
			elif idx >=75 and idx < 78:
				grid8.append(val)
				if idx == 75:
					colD.append(val)
				elif idx == 76:
					colE.append(val)
				else:
					colF.append(val)
			else:
				grid9.append(val)
				if idx == 78:
					colG.append(val)
				elif idx == 79:
					colH.append(val)
				else:
					colI.append(val)
	puzzle = makePuzzle()
	validate = checkForDupes(puzzle)
	if validate is True:
		print("GO! Sudoku! :-D")
	elif validate is False:
		print("NO GO, SUDOKU!! :-( ")
	# pack 27 lists into a list (puzzle[])
	#function checkForDupes(puzzle[]) which calls check on each list for dupes
	# dupe detection breaks and returns false ending algo
	print(row1)
	print(row2)
	print(row3)
	print(row4)
	print(row5)
	print(row6)
	print(row7)
	print(row8)
	print(row9)
	print("\r****************************\r")
	row1.clear()
	row2.clear()
	row3.clear()
	row4.clear()
	row5.clear()
	row6.clear()
	row7.clear()
	row8.clear()
	row9.clear()
	colA.clear()
	colB.clear()
	colC.clear()
	colD.clear()
	colE.clear()
	colF.clear()
	colG.clear()
	colH.clear()
	colI.clear()
	grid1.clear()
	grid2.clear()
	grid3.clear()
	grid4.clear()
	grid5.clear()
	grid6.clear()
	grid7.clear()
	grid8.clear()
	grid9.clear()

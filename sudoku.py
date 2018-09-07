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
for x in file:
	x = re.sub("[^0-9\,]","", x)
	print(x)
	rawNums = x.split(",")
	#for y in rawNums:
	print(rawNums)
	print(len(rawNums))
	
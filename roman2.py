#second try on Dec to Roman conversion. This version works.
#simple, brute force method using subtraction.
import sys
import math
RomanString =""
inputString = ""
inputText = open("decimal.txt", "rt")
inputList = list()
for x in inputText:
	print(x)
	inputList.append(x)
for y in inputList:
	rawInput = y
	input = int(rawInput)
	ognum = input
	if (input > 3999) or (input < 0):
		print("Number to big or is negative, try again!")
	elif math.isnan(input) is not False:
		print("Hey, Dude, try using a number this time!")
	else:
		while input >= 1000:
			RomanString= RomanString +"M"
			input -=1000
		while input >= 500:
			if input >= 900:
				RomanString= RomanString +"CM"
				input -= 900
			else:
				RomanString= RomanString +"D"
				input -= 500
		while input >= 100:
			if input >= 400:
				RomanString= RomanString +"CD"
				input -= 400
			else:
				RomanString= RomanString +"C"
				input -= 100
		while input >= 50:
			if input >= 90:
				RomanString= RomanString +"XC"
				input -= 90
			else:
				RomanString= RomanString +"L"
				input -= 50
		while input >= 10:
			if input >= 40:
				RomanString= RomanString +"XL"
				input -= 40
			else:
				RomanString= RomanString +"X"
				input -= 10
		while input >= 5:
			if input >= 9:
				RomanString= RomanString +"IX"
				input -= 9
			else:
				RomanString= RomanString +"V"
				input -= 5
		while input > 0:
			if input >= 4:
				RomanString= RomanString +"IV"
				input -= 4
			else:
				RomanString= RomanString +"I"
				input -= 1
		print(ognum)
		print(RomanString)
		RomanString = ""
#second try
import math
RomanString =""
RunApp = True
while RunApp is not False:
	usernum = int(input("Enter a number between 1 and 3999. Enter '0' to Quit"))
	ognum = usernum
	if usernum == 0: 
		RunApp = False
	elif (usernum > 3999) or (usernum < 0):
		print("Number to big or is negative, try again!")
	elif math.isnan(usernum) is not False:
		print("Hey, Dude, try using a number this time!")
	else:
		while usernum >= 1000:
			RomanString= RomanString +"M"
			usernum -=1000
		while usernum >= 500:
			if usernum >= 900:
				RomanString= RomanString +"CM"
				usernum -= 900
			else:
				RomanString= RomanString +"D"
				usernum -= 500
		while usernum >= 100:
			if usernum >= 400:
				RomanString= RomanString +"CD"
				usernum -= 400
			else:
				RomanString= RomanString +"C"
				usernum -= 100
		while usernum >= 50:
			if usernum >= 90:
				RomanString= RomanString +"XC"
				usernum -= 90
			else:
				RomanString= RomanString +"L"
				usernum -= 50
		while usernum >= 10:
			if usernum >= 40:
				RomanString= RomanString +"XL"
				usernum -= 40
			else:
				RomanString= RomanString +"X"
				usernum -= 10
		while usernum >= 5:
			if usernum >= 9:
				RomanString= RomanString +"IX"
				usernum -= 9
			else:
				RomanString= RomanString +"V"
				usernum -= 5
		while usernum > 0:
			if usernum >= 4:
				RomanString= RomanString +"IV"
				usernum -= 4
			else:
				RomanString= RomanString +"I"
				usernum -= 1
		print("Your original number was: ")
		print(ognum)
		print("Your Roman number is: " + RomanString)
		RomanString = ""
#Dec to Roman converter --- LOGIC IS WRONG, rework or go with subtraction version
#VARS
#usernumber = user input value, exception if number is >5000, cast to int if decimal value
#thousands = user input divided by 1000, this is the amount of M's in result string
#mremainder = modulus by 1000 to get remainder
#fhundreds = mremainder divided by 500 this is the amount of M's in result string
#dremainder = mremainder modulus 500 to get remainder
#hundreds = dremainder divided by 100, this is the amount of C's in result string
#cremainder = dremainder moduls by 100 to get remainder
#fifties = cremainder divided by 50, this is the amount of L's in result string
#lremainder = cremainder modulus 50 to get remainder
#tens = lremainder divided by 10, this is the amount of X's in the result string
#xremainder = lremainder modulus 10 to get remainder
#fives = xremainder divided by 5, this is the amount of V's in the result string
#vremainder = xremainder modulus 5 to get remainder
#ones = vremainder divided by 1, this is the amount of I's in the result string
#iremainder = vremainder modulus 1, this is a check to determine no remainder
print("Welcom to Patrick Collins' decimal to Roman Numeral converter! Let's get started!")
run = True
while run is not False:
	roman = ""
	userCapture = int(input("Please enter a whole number between 1 and 4999. Enter 0 to quit: \n"))
	usernumber = userCapture
	if (usernumber > 4999) or (usernumber < 0):
		print("You didn't follow instructions, try again!")
	elif usernumber == 0:
		run = False
	thousands = usernumber//1000
	mremainder = usernumber % 1000
	fhundreds = mremainder//500
	dremainder = mremainder % 500
	hundreds = dremainder//100
	cremainder = dremainder % 100
	fifties = cremainder//50
	lremainder = cremainder % 50
	tens = lremainder//10
	xremainder = lremainder % 10
	fives = xremainder // 5
	vremainder = xremainder % 5
	ones = vremainder // 1
	iremainder = vremainder % 1
	for i in range (0, thousands, 1):
		roman = roman + 'M'
	if mremainder >= 900:
		roman = roman + "CM"
	else:
		for i in range (0, fhundreds, 1):
			roman = roman + "D"
	if dremainder >= 400:
		roman = roman + "CD"
	else:
		for i in range(0, hundreds, 1):
			roman = roman + "C"
	if cremainder >= 90:
		roman = roman + "XC"
	else:
		for i in range(0, fifties, 1):
			roman = roman + "L"
	if lremainder >= 40:
		roman = roman + "XL"
	else:
		for i in range(0, tens, 1):
			roman = roman + "X"
	if xremainder == 9:
		roman = roman + "IX"
	else:
		for i in range(0, fives, 1):
			roman = roman + "V"
	if vremainder == 4:
		roman = roman + "IV"
	else:
		for i in range(0, ones, 1):
			roman = roman + "I"
	displayNum = str(usernumber)
	print("The number you entered was: " + displayNum + "\n")
	print("The Roman Numeral version of " + displayNum + "is: " + roman )


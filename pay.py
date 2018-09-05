import sys
import re
paymentText = open("payment.txt", "rt")
inputList = list()
ogInput =""
changeString = ""
for x in paymentText:
	print(x)
	inputList.append(x)
for y in inputList:
	ogInput = y
	workingList = y.split(";")
	rawPrice = workingList[0]
	rawPay = workingList[1]
	priceString = re.sub("[^0-9\.]","", rawPrice)
	payString = re.sub("[^0-9\.]","", rawPay)
	fltPrice= float(priceString)
	price = abs(fltPrice)
	#price = round(float(priceString), 2)
	#price = round(price, 2)
	#pay = round(float(payString), 2)
	fltPay = float(payString)
	pay = abs(fltPay)
	#pay = round(float(price, 2), 2)
	change = pay - price
	change = round(change, 2)
	print("TESTING: "+ str(change))
	#change = round(workingChange, 2)
	print("TESTING " + str(price))
	print("TESTING " + str(pay))
	print(change)
	strChange = str(change)
	changeSplit = strChange.split(".")
	dollars = int(changeSplit[0])
	cents = int(changeSplit[1])
	print ("TESTING Dollars: " + str(dollars))
	print ("TESTING cents: " + str(cents))
	if dollars == 0 and cents == 0:
		changeString = changeString + "No Change"
	while dollars >= 100.0:
		changeString = changeString + "One Hundred"
		dollars -= 100.0
		if dollars >= 0 and cents > 0 :
			changeString = changeString + ", "
	while dollars >= 50.0:
		changeString = changeString + "Fifty"
		dollars -= 50.0
		if dollars >= 0 and cents > 0 :
			changeString = changeString + ", "
	while dollars >= 20.0:
		changeString = changeString + "Twenty"
		dollars -= 20.0
		if dollars >= 0 and cents > 0 :
			changeString = changeString + ", "
	while dollars >= 10.0:
		changeString = changeString + "Ten"
		dollars -= 10.0
		if dollars >= 0 and cents > 0 :
			changeString = changeString + ", "
	while dollars >= 5.0:
		changeString = changeString + "Five"
		dollars -= 5.0
		if dollars >= 0 and cents > 0 :
			changeString = changeString + ", "
	while dollars >= 2.0:
		changeString = changeString + "Two"
		dollars -= 2.0
		if dollars >= 0 and cents > 0 :
			changeString = changeString + ", "
	while dollars >= 1.0:
		changeString = changeString + "One"
		dollars -= 1.0
		if dollars >= 0 and cents > 0 :
			changeString = changeString + ", "
	while cents >= 50:
		changeString = changeString + "Half Dollar"
		cents -= 50
		if cents > 0:
			changeString = changeString + ", "
	while cents >= 25:
		changeString = changeString + "Quarter"
		cents -= 25
		if cents > 0:
			changeString = changeString + ", "
	while cents >= 10:
		changeString = changeString + "Dime"
		cents -= 10
		if cents > 0:
			changeString = changeString + ", "
	while cents >= 5:
		changeString = changeString + "Nickel"
		cents -= 5
		if cents > 0:
			changeString = changeString + ", "
	while cents >= 1:
		changeString = changeString + "Penny"
		cents -= 1
		if cents > 0:
			changeString = changeString + ", "
	print(re.sub("[^0-9\.\;]","", ogInput))
	print(changeString)
	changeString = ""
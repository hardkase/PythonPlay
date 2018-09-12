# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re

def solution(N):
    binN = bin(N)
    #binlist = [int(x) for x in bin(N)[2:]]
    binStr=str(binN)
    print(binStr)
    for m in binStr:
	    print(m)
    binStr1 = re.sub("0b","",binStr, 1)
    print(binStr1)
    gapList = list()
    maxi =0
    trigger = False
    gap = False
    countz = 0
    for i in reversed(binStr1):
        print("current char: " + str(i))
        if i == '0':
            print("Zero encountered")
            if trigger:
                gap = True
                print("gap started")
                countz = countz + 1
                print("0 counted")
                print("Gap detected and counted")
        else:
            if not gap:
                trigger = True
                print(trigger)
                print("trigger enabled!")
            elif gap:
                gapList.append(countz)
                countz =0
                gap = False
                print("gap ended!")
    for j in gapList:
        if j > maxi:
            maxi = j
    print("Max: " + str(maxi))
    return maxi
test = solution(1041)
print("Test: " + str(test))
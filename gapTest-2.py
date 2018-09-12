def solution(N):
    binNum = bin(N)
    binStr = str(binNum)
    print(binStr)
    gaps = "{0:b}".format(N).split('1')[1:-1]
    return len(max(gaps)) if gaps else 0
testNum = 781203650542
test = solution(testNum)
print(test)
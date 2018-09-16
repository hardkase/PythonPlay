import re
#so with some quiet thought and reflection, handled this codility test after the fact in about 2 hours of coding
def solution(S,T):
    """
    given 2 times in format HH:MM:SS, first time is start, second is finish
    provide a count of interesting times possible
    interesting times are ones that feature only 1 digit or any combination of 2 digits
    """
    interesting = 0
    start = S.split(":",3)
    finish = T.split(":",3)
    """
    hours = [start[0], finish[0]]
    minutes = [start[1], finish[1]]
    seconds = [start[2], finish[2]]
    """
    stopHours = int(finish[0])
    stopMins = int(finish[1])
    stopSecs = int(finish[2])
    runTime = "00:00:00"
    strHours = start[0]
    strMins = start[1]
    strSecs = start[2]
    runHours = int(strHours)
    runMins = int(strMins)
    runSecs = int(strSecs)
    hRange = 24
    mRange = 60
    sRange = 60
    run = True
    #hdiff = hours[1]-hours[0]
    z =0
    while run:
    #while z < 600:
        if z %83 ==0:#weird mod # so it doesn't print very often
            print("Current Time: " + strHours+":"+strMins+":"+strSecs)
        if runHours == stopHours:
            if runMins == stopMins:
                if runSecs == stopSecs:
                    print("Stop!")
                    run = False
        runTime = strHours + ":"+strMins+":"+strSecs
        runTime2 = re.sub(":", "", runTime)
        if len(set(runTime2)) == 1 or len(set(runTime2)) == 2:
            interesting = interesting +1
            print("*****INTERESTING TIME FOUND: " + strHours+":"+strMins+":"+strSecs+"*****")
        if runSecs < 60:
            runSecs = runSecs + 1
            if runSecs >= 10:
                strSecs = str(runSecs)
            else: 
                strSecs = "0"+str(runSecs)
        elif runSecs == 60:
            runSecs = 0
            strSecs = "0" + str(runSecs)
            runMins = runMins +1
            if runMins >= 10:
                strMins = str(runMins)
            else:
                strMins = "0" + str(runMins)
        if runMins == 60:
            runMins = 0
            strMins = "0" + str(runMins)
            runHours = runHours +1
            if runHours >= 10:
                strHours = str(runHours)
            else:
                strHours = "0"+str(runHours)
        if runHours == 24:
            runHours = 0
            strHours = "0" + str(runHours)
        z = z + 1
    return interesting
result = solution("00:00:01", "23:59:33")
print(str(result))
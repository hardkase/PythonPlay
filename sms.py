def solution(S, K):
    #get substring of k-1 from S
    #backtrack substring for first whitespace
    #increment count
    #truncate examined data from S
    #wash, rinse, repeat
    
    copyS = S
    strLen = len(copyS)
    snippet = ""
    count = 0
    run = True  #- restore later/ RESTORED
    #z = 0
    #while z < 8:
    print("Original String: " + copyS)
    #take first snippet, strip, strip remainder of copyS of leading space
    #check for white spaces bracketing snippet in remainder, maybe before cutting
    #effectively, avoid short clips like 'fava' instead of 'fava beans'
    #basically, logic should only have to walk back to whitespace if a word carries over
    while run:
        #take snippet of K length
        #test for white space as last char (maybe first too)
        #if yes, take snippet and strip
        # if no, reverse iterate through snippet to next whitespace and clip there
        #final if, if last, count and stop - problem, if long word or short K, could f things up...
        if copyS.find("") == 0 and len(copyS) <=K:
                count = count +1
                print("Last Segment:" + copyS)
                print("STRING OVER")
                copyS =""
                run = False
        snippet = copyS[:K]
        snippet.strip()
        print("First Snippet of S: " + snippet)
        snipLen = len(snippet)
        csLen = 0;#clipped snippet length
        for v in range(snipLen-1, -1, -1):
            if snippet[v] == " ":
                snippet = snippet[:v+1]
                print("Clipped snippet: " + snippet)
                csLen = len(snippet)
                count = count + 1
                print("Count: " + str(count))
                copyS = copyS[csLen:]
                print("Remainder of S:" + copyS)
                break
        #z = z + 1
    return count
    pass
print("***FIRST PASS***")   
string = "the path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of greedy men"
limit = 24
answer = solution(string, limit)
print("Segments: "+ str(answer))
print("****SECOND PASS****")
str2 = "I find your lack of faith disturbing"
lim2 = 11
answer2 = solution(str2, lim2)
print("Segments: "+ str(answer2))
print("*****THIRD PASS*****")
str3 = "I ate his liver with fava beans and a nice Chianti Yummy"
lim3 = 9
answer3 = solution(str3, lim3)
print("Segments: "+ str(answer3))

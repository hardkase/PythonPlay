def solution(S, K):
    #sms is a mess, starting over similar logic with sms2
    #this one seems to work - hyphenation a bit dodgy
    #next up, just using nums
    copyS = S
    snippet = ""
    count = 0
    run = True
    #z = 0
    #while z < 8:
    while run:
        copyS.strip()
        if len(copyS) <= K: # if decremented copyS is shorter or equal to KeyError
            #this is to get the last chunk of text and 0 out copyS and kill while loop
            #do stuff
            print("S length less or equal K")
            count = count + 1
            copyS = ""
            print("DONE: "+ str(count))
            run = False
            break
        snippet = copyS[:K]
        if snippet[(len(snippet)-1)] == " " or copyS[K] == " ":#if the last char in snip is whitespace, strip and use snippet
            print("Snippet of S ends with whitespace")
            snippet.strip()
            print("Snippet: " + snippet)
            count = count + 1
            print(str(count))
            copyS = copyS[len(snippet):]
            print("Remainder of S: " + copyS)
        elif snippet.find(" ") == -1: #and len(copyS) > K: <- don't need as this is first IF; hyphenate long continuous text or for small K-1
            print("hyphenate long text")
            snippet2 = snippet[:K-2]+'-'
            print("hyphenated snippet2: "+ snippet2)
            #snippet= snippet.replace(snippet[len(snippet)-1], '-')
            snippet = snippet2
            print("hyphenated snippet: "+ snippet)
            copyS = copyS[len(snippet)+1:]
            print("Remainder of S: " + copyS)
            count = count + 1
            print(str(count))
        else: #reverse iterate through snippet to first whitespace and cut snippet and copyS accordingly
            print("Start snippet: " + snippet)
            snipLen = len(snippet)
            csLen = 0 #clipped snippet length
            for v in range(snipLen-1,-1,-1):#reverse iterate through snippet
                if snippet[v] == " ":
                    snippet = snippet[:v+1]
                    print("Clipped snippet: " + snippet)
                    csLen = len(snippet)
                    copyS = copyS[csLen:]
                    print("S minus clipped snippet: "+ copyS)
                    count = count + 1
                    print(str(count))
                    break
        #z = z + 1
    return count
print("***FIRST PASS***")   
string = "the path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of greedy men"
limit = 18
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
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
        if len(copyS) <=K:#doing this first to avoid overhead (?) - <REMOVED no whitespace AND> length of decrementing string <= K (logic fuzzy here I think)
                #all we should need care about here is that the remainder of copyS is less/equal to K
                count = count +1#increment
                print("Last Segment:" + copyS)#debug - this is the last segment
                print("STRING OVER")#string is done!
                copyS =""#blizt copyS
                run = False#turn off while
        #snippet = copyS[:K]#copy the first K elements of copyS to a new string
        if len(copyS) > K:
            snippet = copyS[:K-1]
            if snippet[len(snippet)-1]==" " or copyS[K]==" ":
                snippet = copyS[:K-1]
                snippet.strip()
                copyS = copyS[K-1:]
                print("Whole snippet = "+ snippet)
                count = count +1
        elif " " in snippet == False:
            snippet = copyS[:K-1]
            snippet[K-1]="-"
            snippet.strip()
            print("hyphenated snippet: " + snippet)
            copyS = copyS[K-2:]
            print ("Remainder of S: " + copyS)
            count = count +1
            #Do Stuff - take whole K of copy S, strip bookend whitespace, and crunch...
        #else: don't need conditions, otherwise back up to prior whitespace and clip
        #note to self - do I need a conditional to handle long words (if K is short for example) to hyphenate? Not a bad idea...
        #(if snippet doesn't contain any whitespaces only letters/nums, clip at K-2, sub hyphen at k-1...bit tricky but doable)
        else:
            snipLen = len(snippet)#get length of snippet
            csLen = 0;#clipped snippet length, initialized to 0
            for v in range(snipLen-1, -1, -1):#for range = len snippet -1, iterate until v = 0 in steps of -1 
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

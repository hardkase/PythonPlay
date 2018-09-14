def solution(S,T):
	start = S.split(":",3)
	finish = T.split(":",3)
	hours = [start[0], finish[0]]
	minutes = [start[1], finish[1]]
	seconds = [start[2], finish[2]]
	print(hours)
	print(minutes)
	print(seconds)
result = solution("06:05:40", "12:15:21")
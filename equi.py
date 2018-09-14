def solution(a):
    sum_left, sum_right = 0, sum(a)
    for index,value in enumerate(a):
        sum_right -= value
        if sum_left == sum_right:
            yield index
        sum_left += value
        print(index)
a = list(solution([-7, 1, 5, 2, -4, 3, 0])) 
def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if issosu(nums[i]+nums[j]+nums[k]):
                    answer += 1

    return answer
def issosu(n):
    sqr = int(n**(0.5))
    for i in range(2, sqr+1):
        if n % i == 0:
            return 0
        elif i == sqr:
            return 1
def solution(nums):
    answer = 0
    set_ = set(nums)
    set_ = list(set_)
    
    if len(set_) > len(nums)//2:
        if len(nums)%2:
            answer = (len(nums)//2 + 1)
        else:
            answer = (len(nums)//2)
    else:
        answer = len(set_)        
    return answer
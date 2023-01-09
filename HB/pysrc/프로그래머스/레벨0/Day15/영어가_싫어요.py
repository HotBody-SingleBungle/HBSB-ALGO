def solution(numbers):
    answer = 0
    a=['zero','one', 'two','three','four', 'five', 'six','seven','eight','nine']
    while len(numbers):
        if (numbers[0:3]) in a:
            answer=answer*10+a.index(numbers[0:3])
            numbers=numbers[3:]
        elif (numbers[0:4]) in a:
            answer=answer*10+a.index(numbers[0:4])
            numbers=numbers[4:]
        elif (numbers[0:5]) in a:
            answer=answer*10+a.index(numbers[0:5])
            numbers=numbers[5:]
    return answer
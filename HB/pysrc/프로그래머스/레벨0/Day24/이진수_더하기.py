def solution(bin1, bin2):
    answer = ''
    b = 0
    bin = str(int(bin1)+int(bin2))[::-1]
    for i in range(len(bin)):
        a = ((int(bin[i])) + b)%2
        answer += str(a)
        b = (int(bin[i])+b)//2
        a=0
        if i == len(bin)-1 and b == 1:
            answer += '1'
    return answer[::-1]
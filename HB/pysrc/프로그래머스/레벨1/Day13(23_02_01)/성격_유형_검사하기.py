def solution(survey, choices):
    answer = ''
    rtcfmjan = [0,0,0,0]
    for i in range(len(survey)):
        if "R" in survey[i]:
            if survey[i][0] == 'R':
                rtcfmjan[0] += choices[i] - 4
            else:
                rtcfmjan[0] -= choices[i] - 4
        elif "C" in survey[i]:
            if survey[i][0] == 'C':
                rtcfmjan[1] += choices[i] - 4
            else:
                rtcfmjan[1] -= choices[i] - 4
        elif "J" in survey[i]:
            if survey[i][0] == 'J':
                rtcfmjan[2] += choices[i] - 4
            else:
                rtcfmjan[2] -= choices[i] - 4
        elif "A" in survey[i]:
            if survey[i][0] == 'A':
                rtcfmjan[3] += choices[i] - 4
            else:
                rtcfmjan[3] -= choices[i] - 4
    if rtcfmjan[0] > 0:
        answer += 'T'
    else:
        answer += 'R'
    if rtcfmjan[1] > 0:
        answer += 'F'
    else:
        answer += 'C'
    if rtcfmjan[2] > 0:
        answer += 'M'
    else:
        answer += 'J'
    if rtcfmjan[3] > 0:
        answer += 'N'
    else:
        answer += 'A'
    return answer
def solution(letter):
    answer = ''
    letter_=letter.split(" ")
    morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    for i in range(len(letter_)):
        #print(morse.index(letter_[0]))
        answer+=chr(97+morse.index(letter_[i]))
    return answer
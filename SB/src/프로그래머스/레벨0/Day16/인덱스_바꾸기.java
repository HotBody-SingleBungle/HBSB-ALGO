package 프로그래머스.레벨0.Day16;

public class 인덱스_바꾸기 {
    class Solution {
        public String solution(String my_string, int num1, int num2) {
            String str[] = my_string.split("");

            String temp = str[num1];
            str[num1] = str[num2];
            str[num2] = temp;

            String answer = String.join("", str);

            return answer;
        }
    }
}

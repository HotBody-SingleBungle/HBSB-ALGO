package 프로그래머스.레벨0.Day7;

public class 문자열_뒤집기 {
    class Solution {
        public String solution(String my_string) {
            String answer = "";
            for (int i = 0; i < my_string.length(); i++) {
                answer += my_string.charAt(my_string.length() - 1 -i);
            }
            return answer;
        }
    }
}

package 프로그래머스.레벨0.Day16;

public class 중복된_문자_제거 {
    class Solution {
        public String solution(String my_string) {
            String answer = "";

            for (int i = 0; i < my_string.length(); i++) {
                if (!answer.contains(String.valueOf(my_string.charAt(i)))) {
                    answer += my_string.charAt(i);
                }
            }
            return answer;
        }
    }
}

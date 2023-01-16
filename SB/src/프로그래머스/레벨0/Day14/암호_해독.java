package 프로그래머스.레벨0.Day14;

public class 암호_해독 {
    class Solution {
        public String solution(String cipher, int code) {
            String answer = "";
            // for (int i = code -1; i < cipher.length(); i += code) {
            //     answer += cipher.charAt(i);
            // }
            for (int i = code; i <= cipher.length(); i += code) {
                answer += cipher.substring(i-1, i);
            }
            return answer;
        }
    }
}

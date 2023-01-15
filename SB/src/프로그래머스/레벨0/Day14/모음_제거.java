package 프로그래머스.레벨0.Day14;

public class 모음_제거 {
    class Solution {
        public String solution(String my_string) {
            String answer = "";
            answer = my_string.replaceAll("[aeiou]", "");
            return answer;
        }
    }

}

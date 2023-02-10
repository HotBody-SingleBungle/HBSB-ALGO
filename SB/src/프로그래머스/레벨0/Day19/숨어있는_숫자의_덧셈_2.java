package 프로그래머스.레벨0.Day19;

public class 숨어있는_숫자의_덧셈_2 {
    class Solution {
        public int solution(String my_string) {
            int answer = 0;
            String sArr[] = my_string.replaceAll("[a-zA-Z]", " ").split(" ");
            for (int i = 0; i < sArr.length; i++) {
                if(!sArr[i].equals(""))
                    answer += Integer.parseInt(sArr[i]);
            }
            return answer;
        }
    }
}

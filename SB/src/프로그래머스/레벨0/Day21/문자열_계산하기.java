package 프로그래머스.레벨0.Day21;

public class 문자열_계산하기 {
    class Solution {
        public int solution(String my_string) {
            String sArr[] = my_string.split(" ");
            int answer = Integer.parseInt(sArr[0]);

            for (int i = 1; i < sArr.length; i++) {
                if (sArr[i].equals("+")) {
                    answer += Integer.parseInt(sArr[i + 1]);
                } else if (sArr[i].equals("-")) {
                    answer -= Integer.parseInt(sArr[i + 1]);
                }
            }

            return answer;
        }
    }
}

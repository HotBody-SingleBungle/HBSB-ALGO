package 프로그래머스.레벨0.Day22;

public class 이진수_더하기 {
    class Solution {
        public String solution(String bin1, String bin2) {
            int a = Integer.parseInt(bin1, 2);
            int b = Integer.parseInt(bin2, 2);

            String answer = Integer.toBinaryString(a+b);
            return answer;
        }
    }
}

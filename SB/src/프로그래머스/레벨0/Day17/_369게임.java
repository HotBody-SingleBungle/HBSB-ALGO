package 프로그래머스.레벨0.Day17;

public class _369게임 {
    class Solution {
        public int solution(int order) {
            int answer = 0;
            String strOrder = String.valueOf(order);
            for (int i = 0; i < strOrder.length(); i++) {
                if (strOrder.charAt(i) == '3' || strOrder.charAt(i) == '6' || strOrder.charAt(i) == '9') {
                    answer++;
                }
            }
            return answer;
        }
    }
}

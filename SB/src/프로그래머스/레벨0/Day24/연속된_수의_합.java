package 프로그래머스.레벨0.Day24;

public class 연속된_수의_합 {
    class Solution {
        public int[] solution(int num, int total) {
            int[] answer = new int [num];

            int start = (total / num) - ((num - 1) / 2);

            for (int i = 0; i < num; i++) {
                answer[i] = start + i;
            }

            return answer;
        }
    }
}

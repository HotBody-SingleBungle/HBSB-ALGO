package 프로그래머스.레벨0;

public class 배열_자르기 {
    class Solution {
        public int[] solution(int[] numbers, int num1, int num2) {
            int[] answer = new int[num2 - num1 + 1];
            int cnt = 0;
            for (int i = num1; i <= num2; i++) {
                answer[cnt++] += numbers[i];
            }
            return answer;
        }
    }
}

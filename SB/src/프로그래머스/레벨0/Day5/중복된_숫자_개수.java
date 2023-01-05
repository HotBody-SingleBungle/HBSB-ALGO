package 프로그래머스.레벨0.Day5;

public class 중복된_숫자_개수 {
    class Solution {
        public int solution(int[] array, int n) {
            int answer = 0;
            for (int i = 0; i < array.length; i++) {
                if (array[i] == n)
                    answer++;
            }
            return answer;
        }
    }
}

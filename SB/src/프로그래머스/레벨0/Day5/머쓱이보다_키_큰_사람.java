package 프로그래머스.레벨0.Day5;

public class 머쓱이보다_키_큰_사람 {
    class Solution {
        public int solution(int[] array, int height) {
            int answer = 0;
            for (int i = 0; i < array.length; i++) {
                if (array[i] > height)
                    answer++;
            }
            return answer;
        }
    }
}

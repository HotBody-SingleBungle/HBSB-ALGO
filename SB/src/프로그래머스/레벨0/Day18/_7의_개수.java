package 프로그래머스.레벨0.Day18;

public class _7의_개수 {
    class Solution {
        public int solution(int[] array) {
            int answer = 0;

            for (int i = 0; i < array.length; i++) {
                int temp = array[i];
                while (temp > 0) {
                    if (temp % 10 == 7) {
                        answer++;
                    }
                    temp /= 10;
                }

            }
            return answer;
        }
    }
}

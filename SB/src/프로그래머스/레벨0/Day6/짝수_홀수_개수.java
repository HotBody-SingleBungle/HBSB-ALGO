package 프로그래머스.레벨0.Day6;

public class 짝수_홀수_개수 {
    class Solution {
        public int[] solution(int[] num_list) {
            int[] answer = {0, 0};
            // int evenNum = 0;
            // int oddNum = 0;

            for (int i = 0; i < num_list.length; i++) {
                if (num_list[i] % 2 == 0)
                    answer[0]++;
                    // evenNum++;
                else
                    // oddNum++;
                    answer[1]++;
            }
            return answer;
        }
    }
}

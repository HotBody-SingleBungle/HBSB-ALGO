package 프로그래머스.레벨0.Day12;

public class _2차원으로_만들기 {
    class Solution {
        public int[][] solution(int[] num_list, int n) {
            // int[][] answer = new int[num_list.length / n][n];
            // int cnt = 0;
            // for (int i = 0; i < num_list.length / n; i++){
            //     for (int j = 0; j < n; j ++) {
            //         answer[i][j] = num_list[cnt++];
            //     }
            // }
            // return answer;
            int[][] answer = new int[num_list.length / n][n];

            for (int i = 0; i < num_list.length; i++) {
                answer[i / n][i % n] = num_list[i];
            }

            return answer;
        }
    }
}

package 프로그래머스.레벨0.Day19;
import java.util.*;
public class 안전지대 {

    class Solution {
        static int dx[] = {0, 0 ,-1, 1, -1, 1, 1, -1};
        static int dy[] = {1, -1, 0, 0, -1, -1, 1, 1};
        public int solution(int[][] board) {
            int result = 0;
            int [][] answer = new int[board.length][board.length];
            for (int i = 0; i < board.length; i++) {
                for (int j = 0; j < board.length; j++) {
                    if (board[i][j] == 1) {
                        answer[i][j] = 1;
                        for (int d = 0; d < 8; d++) {
                            int nr = i + dx[d];
                            int nc = j + dy[d];
                            if (nr >= 0 && nc >= 0 && nr < board.length && nc < board.length) {
                                answer[nr][nc] = 1;
                            }
                        }
                    }
                }
            }


            for (int i = 0; i < answer.length; i++) {
                for (int j = 0; j < answer.length; j++) {
                    // System.out.print(answer[i][j] + " ");
                    if (answer[i][j] == 0) {
                        result++;
                    }
                }
                // System.out.println();
            }


            return result;
        }
    }



// class Solution {

//     static int[] dx = { -1, 0, 1, 1, 1, 0, -1, -1 };
//     static int[] dy = { -1, -1, -1, 0, 1, 1, 1, 0 };
//     static boolean[][] visit;
//     static int answer;
//     public int solution(int[][] board) {
//         answer = 0;

//         List<int[]> al = new ArrayList<>();
//         visit = new boolean[board.length][board.length];
//         for(int i = 0; i < board.length; i++){
//             for(int j = 0; j < board.length; j++){
//                 if(board[i][j] == 1){
//                     al.add(new int[]{i, j});
//                     answer++;
//                 }
//             }
//         }

//         for(int i = 0; i < al.size(); i++){
//             int[] tmp = al.get(i);
//             dfs(tmp[0], tmp[1], board.length, board);
//         }

//         return (board.length*board.length) - answer;
//     }
//     static void dfs(int r, int c, int len, int[][] board){
//         visit[r][c] = true;
//         for(int i = 0; i < 8; i++){
//             int nr = r + dx[i];
//             int nc = c + dy[i];
//             if(nr < 0 || nc < 0 || nr >= len || nc >= len){
//                 continue;
//             }
//             if(!visit[nr][nc] && board[nr][nc] == 0){
//                 visit[nr][nc] = true;
//                 board[nr][nc] = 1;
//                 answer++;
//             }
//         }
//     }
// }

}

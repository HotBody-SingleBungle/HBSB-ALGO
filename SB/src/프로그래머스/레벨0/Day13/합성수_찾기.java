package 프로그래머스.레벨0.Day13;

public class 합성수_찾기 {
    class Solution {
        public int solution(int n) {
            int answer = 0;
            int cnt = 0;
            for (int i = 1; i <= n; i++) {
                cnt = 0;
                for (int j = 1; j <= n; j++) {
                    if (i % j == 0)
                        cnt ++;
                }
                if (cnt >= 3)
                    answer++;
            }
            return answer;
        }
    }
}

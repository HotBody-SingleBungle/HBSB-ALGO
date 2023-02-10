package 프로그래머스.레벨0.Day25;

public class 저주의_숫자_3 {
    class Solution {
        public int solution(int n) {

            for (int i = 1; i <= n; i++) {
                if (i % 3 == 0 || String.valueOf(i).contains("3")) {
                    n++;
                }
            }

            return n;
        }
    }

}

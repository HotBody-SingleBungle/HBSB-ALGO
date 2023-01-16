package 프로그래머스.레벨0.Day12;

public class 구슬을_나누는_경우의_수 {
    class Solution {
        static int N, R, CASE = 0;
        static int numbers[];
        static int input[];

        public int solution(int balls, int share) {
            int answer = 0;
            N = balls;
            R = share;
            numbers = new int[N];
            input = new int[R];

            for (int i = 0; i < N; i++) {
                numbers[i] = i + 1;
            }

            combination(0, 0);
            return CASE;
        }

        private static void combination(int cnt, int start) {
            if (R == cnt) {
                CASE++;
                return;
            }

            for (int i = start; i < N; i++) {
                input[cnt] = numbers[i];

                combination(cnt + 1, i + 1);
            }
        }
    }
}

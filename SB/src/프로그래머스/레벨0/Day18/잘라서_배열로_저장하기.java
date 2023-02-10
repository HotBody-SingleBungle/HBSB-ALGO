package 프로그래머스.레벨0.Day18;

public class 잘라서_배열로_저장하기 {
    class Solution {
        public String[] solution(String my_str, int n) {
            String[] answer;
            if (my_str.length() % n == 0) {
                answer = new String[my_str.length() / n];
            } else {
                answer = new String[(my_str.length() / n) + 1];
            }
            int cnt = 0;
            for (int i = 0; i < my_str.length(); i += n) {
                if (my_str.length() - (i + n) > 0) {
                    answer[cnt++] = my_str.substring(i, i + n);
                } else {
                    answer[cnt++] = my_str.substring(i, my_str.length());
                }
            }

            return answer;
        }
    }
}

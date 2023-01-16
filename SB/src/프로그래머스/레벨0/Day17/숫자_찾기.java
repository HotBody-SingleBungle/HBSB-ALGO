package 프로그래머스.레벨0.Day17;
/*
문자열 + 숫자 = 문자열
 */

public class 숫자_찾기 {
    class Solution {
        public int solution(int num, int k) {
            int answer = 0;
            String str = String.valueOf(num);
            String strK = String.valueOf(k);

            if (str.indexOf(strK) == -1)
                answer = -1;
            else
                answer = str.indexOf(strK) + 1;
            return answer;
            // return ("-" + num).indexOf(String.valueOf(k));
        }
    }

}

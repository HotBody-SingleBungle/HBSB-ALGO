package 프로그래머스.레벨0.Day13;

public class 팩토리얼 {
    class Solution {
        public int solution(int n) {
            int answer = 1;
            int i = 1;
            while(true) {
                if (answer <= n) {
                    answer *= i + 1;
                    i++;
                } else
                    break;
            }
            return i - 1;


            // for (int i = 2 ; i <= 10; i++) {
            //     answer *= i;
            //     if (answer > n)
            //         return i -1;
            //     else if (answer == n)
            //         return i;
            // }
            // return answer;
        }


    }
}

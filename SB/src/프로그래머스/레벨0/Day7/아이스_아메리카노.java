package 프로그래머스.레벨0.Day7;

public class 아이스_아메리카노 {
    class Solution {
        static int answer[];
        public int[] solution(int money) {
            answer = new int [2];
            fun(money);

            return answer;
        }

        static void fun (int money) {
            if (money >= 5500) {
                money -= 5500;
                answer[0]++;
                answer[1] = money;
                fun(money);
            } else {
                answer[1] = money;
            }


        }
    }
}

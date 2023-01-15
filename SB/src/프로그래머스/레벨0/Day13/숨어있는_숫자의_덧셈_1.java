package 프로그래머스.레벨0.Day13;

public class 숨어있는_숫자의_덧셈_1 {
    class Solution {
        public int solution(String my_string) {
            int answer = 0;
            // for (int i = 0; i < my_string.length(); i++) {
            //     // System.out.println(my_string.charAt(i) - 48);
            //     int num = my_string.charAt(i) - 48;
            //     // System.out.println(num);
            //     if (num > 0 && num <= 9) {
            //         answer += num;
            //     }
            // }
            for (int i = 0; i < my_string.length(); i++) {
                if (Character.digit(my_string.charAt(i), 10) > 0)
                    answer += Character.digit(my_string.charAt(i), 10);
            }
            return answer;
        }
    }
}

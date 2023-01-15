package 프로그래머스.레벨0.Day12;

public class 공_던지기 {
    class Solution {
        public int solution(int[] numbers, int k) {
//         int answer = 0;

//         for (int i = 1; i < k; i++) {
//             answer += 2;
//             if (answer > numbers.length) {
//                 answer -= numbers.length;
//             }
//         }

//         return answer + 1;
            return numbers[((k - 1) * 2) % numbers.length];
        }
    }


}

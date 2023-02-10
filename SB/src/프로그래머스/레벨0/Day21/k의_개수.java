package 프로그래머스.레벨0.Day21;

public class k의_개수 {
    // class Solution {
//     public int solution(int i, int j, int k) {
//         int answer = 0;
//         for (int x = i; x <= j; x++) {
//             String st = String.valueOf(x);
//             // 문자열을 문자배열에 넣고 비교

//             String stCharArr[] = st.split("");
//             for (int a = 0; a < stCharArr.length; a++) {
//                 if (stCharArr[a].equals(String.valueOf(k))) {
//                     answer++;
//                 }
//             }
//         }
//         // System.out.println(String.valueOf(i));
//         return answer;
//     }
// }

    class Solution {
        public int solution(int i, int j, int k) {
            int answer = 0;
            for(int a = i; a <= j; a++) {
                int x = a;
                while (x != 0) {
                    if (x % 10 == k) {
                        answer++;
                    }
                    x /= 10;
                }
            }

            return answer;
        }
    }
}

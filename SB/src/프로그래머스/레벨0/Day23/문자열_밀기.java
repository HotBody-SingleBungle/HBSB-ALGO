package 프로그래머스.레벨0.Day23;

public class 문자열_밀기 {
    class Solution {
        public int solution(String A, String B) {
            int answer = 0;

            //순방향
            String tA = A;

            if(tA.equals(B))
                return answer;

            for(int i = 0; i < A.length(); i++) {
                String a = tA.substring(tA.length()-1);
                tA = a + tA.substring(0, tA.length()-1);
                answer++;
            }

            return -1;
        }
    }


// class Solution {
//     public int solution(String A, String B) {
//         String temp = "";
//         if (A.equals(B)) {
//             return 0;
//         } else {
//             temp += A.charAt(A.length() - 1);
//             for (int i = 0; i < A.length() - 1; i++) {
//                 temp += A.charAt(i);
//             }
//             if (temp.equals(B))
//                 return 1;
//             else
//                 return -1;

//         }

//     }
// }
}

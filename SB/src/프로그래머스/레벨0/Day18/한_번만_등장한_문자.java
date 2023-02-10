package 프로그래머스.레벨0.Day18;

public class 한_번만_등장한_문자 {
    class Solution {
        public String solution(String s) {
            int arr[] = new int[26];
            for (int i = 0; i < s.length(); i++) {
                arr[s.charAt(i) - 97] ++;
            }
            String answer = "";

            for (int i = 0; i < arr.length; i++) {
                if (arr[i] == 1) {
                    answer += (char)(i + 97);
                }
            }

            return answer;
        }
    }
}

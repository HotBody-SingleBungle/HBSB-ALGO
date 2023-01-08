package 프로그래머스.레벨0.Day9;

public class 자릿수_더하기 {
    public class Solution {
        public int solution(int n) {
            int answer = 0;
            String s = Integer.toString(n); //int n을 String으로 변환

            for(int i=0; i<s.length(); i++){
                answer += Integer.parseInt(s.substring(i, i+1));
            }
            return answer;
        }
    }
}

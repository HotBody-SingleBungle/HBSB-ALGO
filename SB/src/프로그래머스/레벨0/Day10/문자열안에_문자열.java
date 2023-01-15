package 프로그래머스.레벨0.Day10;

public class 문자열안에_문자열 {
    class Solution {
        public int solution(String str1, String str2) {
            return str1.contains(str2) ? 1 : 2;
        }
    }
}

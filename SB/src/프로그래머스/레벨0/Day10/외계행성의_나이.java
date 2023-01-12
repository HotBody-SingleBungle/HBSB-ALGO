package 프로그래머스.레벨0.Day10;

public class 외계행성의_나이 {
    class Solution {
        public String solution(int age) {
            String answer = "";

            String s = String.valueOf(age);
            String arr[] = s.split("");

            for (int i = 0; i < arr.length; i++) {
                answer += (char) (Integer.parseInt(arr[i]) + 97);
            }



            return answer;
        }
    }
}

//    String answer = "";
//    String[] alpha = new String[]{"a","b","c","d","e","f","g","h","i","j"};
//
//        while(age>0){
//                answer = alpha[age % 10] + answer;
//                age /= 10;
//                }
//
//                return answer;
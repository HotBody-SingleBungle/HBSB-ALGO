package 프로그래머스.레벨0.Day17;
import java.util.*;
public class 문자열_정렬하기_2 {
    class Solution {
        public String solution(String my_string) {
            char c[] = my_string.toLowerCase().toCharArray();

            Arrays.sort(c);

            return new String(c);
//         String answer = "";
//         String my_stringArr[] = my_string.split("");

//         for (int i = 0; i < my_stringArr.length; i++) {
//             if (Character.isUpperCase(my_string.charAt(i))) {
//                 my_stringArr[i] = String.valueOf(my_string.charAt(i)).toLowerCase();
//             }
//         }
//         Arrays.sort(my_stringArr);

//         return String.join("", my_stringArr);

        }
    }
}

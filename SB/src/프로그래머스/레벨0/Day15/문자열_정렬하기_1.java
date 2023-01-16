package 프로그래머스.레벨0.Day15;
import java.util.*;
public class 문자열_정렬하기_1 {

    class Solution {
        public ArrayList solution(String my_string) {
            ArrayList<Integer> list = new ArrayList<>();

            for (int i = 0; i < my_string.length(); i++) {
                if (!Character.isLowerCase(my_string.charAt(i))) {
                    list.add(my_string.charAt(i)-48);
                }
            }
            Collections.sort(list);

            return list;
        }
    }
}

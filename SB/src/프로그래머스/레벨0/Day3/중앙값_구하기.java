package 프로그래머스.레벨0.Day3;
import java.util.*;
public class 중앙값_구하기 {
    class Solution {
        public int solution(int[] array) {
            Arrays.sort(array);
            return array[array.length/2];
        }
    }
}

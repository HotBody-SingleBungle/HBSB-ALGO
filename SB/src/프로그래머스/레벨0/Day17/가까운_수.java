package 프로그래머스.레벨0.Day17;
import java.util.*;
public class 가까운_수 {

    class Solution {
        public int solution(int[] array, int n) {
            int answer = 0;
            int min = 1000;
            int arr[] = new int [array.length];
            Arrays.sort(array);
            for (int i = 0; i < array.length; i++) {
                if (Math.abs(n - array[i]) < min) {
                    answer = array[i];
                    min = n - array[i];
                }
            }

            return answer;
        }
    }

}

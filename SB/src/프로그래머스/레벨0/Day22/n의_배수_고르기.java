package 프로그래머스.레벨0.Day22;
import java.util.ArrayList;
public class n의_배수_고르기 {

    class Solution {
        public int[] solution(int n, int[] numlist) {
            ArrayList<Integer> list = new ArrayList<>();

            for (int i = 0; i < numlist.length; i++) {
                if (numlist[i] % n == 0) {
                    list.add(numlist[i]);
                }
            }
            int answer[] = new int[list.size()];
            for (int i = 0; i < list.size(); i++) {
                answer[i] = list.get(i);
            }

            return answer;
        }
    }
//         int cnt = 0;
//         String s = "";
//         for (int i = 0; i < numlist.length; i++) {
//             if (numlist[i] % n == 0) {
//                 s += numlist[i];
//                 System.out.println(s);
//                 cnt++;
//             }
//         }
//         int[] answer = new int[cnt];

//         for (int i = 0; i < cnt; i++) {
//             answer[i] = Iteger.parsint(s);
//         }
//         return answer;


}

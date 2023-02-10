package 프로그래머스.레벨0.Day22;

public class 영어가_싫어요 {
    class Solution {
        public long solution(String numbers) {
            // numbers = numbers.replaceAll("zero","0");
            // numbers = numbers.replace("one","1");
            // numbers = numbers.replace("two","2");
            // numbers = numbers.replace("three","3");
            // numbers = numbers.replace("four","4");
            // numbers = numbers.replace("five","5");
            // numbers = numbers.replace("six","6");
            // numbers = numbers.replace("seven","7");
            // numbers = numbers.replace("eight","8");
            // numbers = numbers.replace("nine","9");
            String arr[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

            for (int i = 0; i < arr.length; i++) {
                numbers = numbers.replaceAll(arr[i], String.valueOf(i));
            }

            long answer = Long.parseLong(numbers);
            return answer;
        }
    }
}

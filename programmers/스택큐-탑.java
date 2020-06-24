public class Solution {
    public static int[] solution(int[] heights) {
        int[] answer = new int[heights.length];
        for(int i = heights.length - 1; i >= 0; i--) {            
            int recv_top_number = 0;
            for(int j = i - 1; j >= 0; j--) {
                if(heights[j] > heights[i]) {
                    int recv_top_idx = j;
                    recv_top_number = j + 1;
                    break;
                }
            }
            answer[i] = recv_top_number;
        }
        return answer;
    }
}
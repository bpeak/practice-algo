package algoexam;

import java.util.ArrayList;
import java.util.Stack;

public class Crain {
    public int solution(int[][] board, int[] moves) {
        ArrayList<Integer> basket = new ArrayList<>();
        int score = 0;
        for(int move : moves) {
            int idx = move - 1;
            for(int[] row : board){
                if(row[idx] != 0){
                    basket.add(row[idx]);
                    row[idx] = 0;
                    break;
                }
            }
            int basketSize = basket.size();
            if(basketSize >= 2 && basket.get(basketSize - 1) == basket.get(basketSize - 2)) {
                basket.remove(basketSize - 1);
                basket.remove(basketSize - 2);
                score +=2 ;
            }
        }
        Stack<Integer> bas = new Stack<>();
        bas.add(1);
        bas.add(2);
        bas.add(3);
        bas.get(3);
        
        return score;
    }
}

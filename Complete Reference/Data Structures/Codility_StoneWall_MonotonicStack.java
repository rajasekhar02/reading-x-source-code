// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int solution(int[] H) {
        // Implement your solution here
        int minBlocks = 0;
        Stack<Integer> monotonicStack = new Stack<Integer>(); 
        for(int i: H){
            while(!monotonicStack.isEmpty() && monotonicStack.peek() > i){
                monotonicStack.pop();
            }
            if(monotonicStack.isEmpty() || i > monotonicStack.peek()){
                minBlocks++;
                monotonicStack.push(i);
            }
        }  
        return minBlocks;
    }
}

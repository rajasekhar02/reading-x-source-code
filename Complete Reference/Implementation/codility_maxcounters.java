// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public int[] solution(int N, int[] A) {
        // Implement your solution here
        int max_element = 0;
        int max_val_at_max_indicator = 0;
        int max_indicator = N+1;
        boolean max_indicator_occurred = false;
        int[] resultArr = new int[N];
        for (int i=0;i<A.length;i++){
            if(A[i] < max_indicator){
                if(resultArr[A[i]-1]<max_val_at_max_indicator){
                    resultArr[A[i]-1] = max_val_at_max_indicator + 1;
                } else {
                    resultArr[A[i]-1] += 1;
                }
                max_element = Math.max(resultArr[A[i]-1], max_element);
            } else {
                // System.out.println(Arrays.toString(resultArr));
                max_val_at_max_indicator = max_element;
            }
        }

        for(int i=0; i<N; i++){
            if(resultArr[i] < max_val_at_max_indicator){
                resultArr[i] = max_val_at_max_indicator;
            }
        }
        // System.out.println(Arrays.toString(resultArr));
        return resultArr;
    }
}

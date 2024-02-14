// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

/**
* Learnings:
* 1. Check for case when there are no majority elements in range 1 and range 2 which may resulted in counting an invalid solution
* 2. Starting S variable from 0 and using S+1 as ends in the function will result in counting an invalid solution.
* 3. Used -1 as a indicator for invalid solution but it could be valid solution as range of A[i] is between [-1000000000, 1000000000].
*/

// TC: O(SPositions * A.length)
// SPositions = A.length
interface MajorityElementUtils {
    int getMajorityElement(int start, int end);
}
class Solution {
    public int solution(int[] A) {
        // Implement your solution here
        final int noMajorElement = -1000000001; 
        MajorityElementUtils utils = (int start, int end)->{
            int count = 0;
            int ele = 0;
            int size = (end-start);
            for(int i=start;i<end;i++){
                if(count == 0){
                    count = 1;
                    ele = A[i];
                } else if(A[i] != ele){
                    count--;
                }else{
                    count++;
                }
            }
            count = 0;
            for(int i=start;i<end;i++){
                if(A[i] == ele){
                    count++;
                }
            }
            // System.out.println(count+" "+size+" "+ ele);
            return count > (size>>1) ? ele: noMajorElement;
        };
        int countEqui = 0;
        for(int S=1;S<A.length;S++){
            int range1 = utils.getMajorityElement(0,S);
            int range2 = utils.getMajorityElement(S, A.length);
            if(range1 != noMajorElement && range2 > noMajorElement){
                countEqui += range1 == range2 ? 1:0;
            }
        }
        return countEqui;
    }
}

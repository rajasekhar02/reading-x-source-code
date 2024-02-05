// Problem Statement: https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/
import java.util.*;

class Solution {
    public int solution2(int[] A) {
        // Implement your solution here
        // Time Complexity: O(nlogn)
        Arrays.sort(A);
        int idPosInt=0;
        int itr = 0;
        while((itr < A.length) && (A[itr]<=0)){
            itr++;
        }
        idPosInt = itr;
        if((itr == A.length) || (A[idPosInt]>1)){
            return 1;
        }
        int min = A[A.length-1]+1;
        int prev = A[idPosInt];
        for(int i=idPosInt+1;i<A.length;i++){
            if(prev == A[i]){
                continue;
            }
            if((prev+1) == A[i]){
                prev = A[i];
                continue;
            }
            min = Math.min(min, prev+1);
            break;
        }
        return min;
    }
    public int solution(int[] A) {
        // Implement your solution here
        // Time Complexity: O(n), Space Complexity: O(n) 
        boolean[] markNum = new boolean[1000001];
        for(int i=0;i<A.length;i++){
            if(A[i] <= 0){
                continue;
            }
            markNum[A[i]] = true;
        }
        
        for(int i=1;i<markNum.length;i++){
            if(!markNum[i]){
                return i;
            }
        }
        return (markNum.length+1);
    }
}

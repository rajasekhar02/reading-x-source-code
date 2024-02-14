// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
class MajorElement {
    public int val;
    public int count;
    public MajorElement(int val, int count){
        this.val = val;
        this.count = count;
    }
}

interface MajorityElementUtils {
    MajorElement getMajorityElement(int start, int end);
}

// O(A.length * Constant)
// Constant = 3
class Solution {
    public int solution(int[] A) {
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
            return count > (size>>1) ? new MajorElement(ele, count): new MajorElement(noMajorElement, count);
        };
        MajorElement majorEle = utils.getMajorityElement(0, A.length);
        int currLeaderOccurences = 0;
        int equiLeaderCnt = 0;
        for(int sPos=0;sPos<A.length;sPos++){
            if(A[sPos] == majorEle.val){
                currLeaderOccurences++;
            }
            int traversedLen = sPos+1;
            int unTraversedLen = A.length - traversedLen;
            boolean isOverallMajorIsMajorInTraversedLen = currLeaderOccurences > ((traversedLen) >> 1);
            boolean isOverallMajorIsMajorInUnTraversedLen = (majorEle.count-currLeaderOccurences) > (unTraversedLen >> 1);
            if(isOverallMajorIsMajorInTraversedLen && isOverallMajorIsMajorInUnTraversedLen){
                equiLeaderCnt++;
            }
        }
        return equiLeaderCnt;
    }
}

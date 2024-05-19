class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        sumVal = 0
        count = 0
        posMin = 1 << 30
        negMax = -1*(1<<30)
        for nodeValue in nums:
            operatedNodeValue = nodeValue ^ k
            sumVal += nodeValue
            netChange = operatedNodeValue - nodeValue
            if netChange > 0:
                posMin = min(posMin, netChange)
                sumVal += netChange
                count += 1
            else:
                negMax = max(negMax, netChange)
        """
            It can be observed that the value of count should always be even because "node[i]^k > node[i]" is performed on a pair of nodes.
        """
        if count % 2 == 0:
            return sumVal
        """
        Now, there can be two cases for the same:-
            1. If the sum of positiveMinimum and negativeMaximum is greater than zero, then the node value sum will be increased by including this pair. So, we include both elements.

            2. If the sum of positiveMinimum and negativeMaximum is less than or equal to zero, then the node value sum will be decreased or have no change on including this pair. So, we exclude this pair.
        """
        return max(sumVal - posMin, sumVal + negMax)
    def maximumValueSumGreedy(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # so in this problem the edges array is not needed
        # due to the fact that we can pair any two nodes and perform the XOR operations
        # and the nodes in between this pair will remain unchanged after performing the action
        n = len(nums)
        netChange = [(nums[i]^k)-nums[i] for i in range(n)]
        nodeSum = sum(nums)
        netChange.sort(reverse=True)
        for i in range(0, n, 2):
            # If netChange contains odd number of elements break the loop
            if i+1 == n:
                break
            pairSum = netChange[i] + netChange[i+1]
            # Include in nodeSum if pairSum is positive
            if pairSum > 0:
                nodeSum += pairSum
                    
        return nodeSum

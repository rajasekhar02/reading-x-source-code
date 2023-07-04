class Solution:
    def __init__(self):
        self.maxFulFilledRequests = 0
    
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        buildingLog = [0]*n
        self.recurse(requests, buildingLog, 0, 0)
        return self.maxFulFilledRequests
    
    def recurse(self, requests, buildingLog, iRequest, fulFilledRequestCount):
        if len(requests) == iRequest:
            for i in buildingLog:
                if i != 0:
                    return
            self.maxFulFilledRequests = max(fulFilledRequestCount, self.maxFulFilledRequests)
            return
        
        # fulfilling the current request
        buildingLog[requests[iRequest][0]]-=1
        buildingLog[requests[iRequest][1]]+=1
        newFulFilledRequestCount = fulFilledRequestCount + 1
        # continuing to process the other request
        self.recurse(requests, buildingLog, iRequest+1, newFulFilledRequestCount)

        # reverting the above changes to discard this request
        buildingLog[requests[iRequest][0]]+=1
        buildingLog[requests[iRequest][1]]-=1
        newFulFilledRequestCount = fulFilledRequestCount
        self.recurse(requests, buildingLog, iRequest+1, newFulFilledRequestCount)
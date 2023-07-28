class Solution:
    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # code here
        ans = 0
        meetings = []
        for id, i in enumerate(start):
            meetings.append([i, end[id], id + 1])
        """ 
            **Mistake One**: Should sort by start time and end time
        """
        # meetings = sorted(meetings, key= lambda x: (x[0],x[1]))

        meetings = sorted(meetings, key=lambda x: (x[1], x[2]))

        ans = 1
        prevMeetingEnd = meetings[0][1]
        for i in range(1, len(meetings)):
            if prevMeetingEnd < meetings[i][0]:
                ans += 1
                prevMeetingEnd = meetings[i][1]
            # if ans[-1][1] < meetings[i][0]:
            #     ans.append(meetings[i])
            # if i == (len(meetings) - 1):
            #     ans.append(meetings[i])
        return ans


N = 6
start = [1, 2, 3, 5, 8, 10]
end = [3, 4, 6, 9, 9, 11]
print(Solution().maximumMeetings(N, start, end))

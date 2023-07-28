class Solution:
    # Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self, Jobs, n):
        # code here
        Jobs = sorted(
            Jobs,
            key=lambda x: -x.profit,
        )
        # print(Jobs)
        maxDaysToWork = Jobs[0].deadline
        for i in range(1, n):
            if maxDaysToWork < Jobs[i].deadline:
                maxDaysToWork = Jobs[i].deadline
        days = [-1] * (maxDaysToWork)
        # print(days)
        profit = 0
        jobs_done = 0
        for i in Jobs:
            for j in range(i.deadline - 1, -1, -1):
                # print(j, days)
                if days[j] == -1:
                    days[j] = i.id
                    profit += i.profit
                    jobs_done += 1
                    break
        # print(days)
        return [jobs_done, profit]


N = 5
Jobs = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)]
print(Solution().JobScheduling(Jobs, N))

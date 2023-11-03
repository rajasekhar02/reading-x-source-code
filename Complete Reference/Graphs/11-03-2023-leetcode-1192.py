"""
DFS and Finding Bridges in a Graph. Uses DFS with entry times.
1. Finding whether a vertices of the edge has a back edge 
"""

class Solution:
    def __init__(self):
        self.visited = []
        self.entry_times = []
        self.min_reachable_ancestor_entry_time = []
        self.ans = []
        self.timer = 0
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.visited = [False]*n
        self.entry_times = [-1]*n
        self.min_reachable_ancestor_entry_time = [-1]*n
        adj_list = defaultdict(list)
        for i in connections:
            adj_list[i[0]].append(i[1])
            adj_list[i[1]].append(i[0])
        # print(adj_list)
        self.dfs(0, -1, adj_list)
        # print(self.min_reachable_ancestor_entry_time)
        return self.ans
      
    def dfs(self, curr_vertex, curr_vertex_parent, adj_list):
        self.visited[curr_vertex] = True
        self.timer += 1
        self.min_reachable_ancestor_entry_time[curr_vertex] = self.timer
        self.entry_times[curr_vertex] = self.timer
        for child in adj_list[curr_vertex]:
            if child == curr_vertex_parent: continue
            if self.visited[child]:
              # if the child is visited check whether the entry time is less than the curr_vertex oldest_ancestor_entry_time
                self.min_reachable_ancestor_entry_time[curr_vertex] = min(
                    self.min_reachable_ancestor_entry_time[curr_vertex],
                    self.entry_times[child]
                )
            else:
                self.dfs(child, curr_vertex, adj_list)
              # checking the child oldest ancestor entry time if there are any backedges from the child or from grand children
                self.min_reachable_ancestor_entry_time[curr_vertex] = min(
                    self.min_reachable_ancestor_entry_time[curr_vertex],
                    self.min_reachable_ancestor_entry_time[child]
                )
              
              """Q: why we should not check with min_reachable ancestor entry time ?
                if we check with the min_reachable ancestor entry time then it means we are judging the back edge for the oldest ancestor of the current node. which is totally wrong solution.
              """
              # Meaning: if there are no back edges then the child oldest ancestor entry time will be greater than the entry_time of the curr_vertex
                if self.min_reachable_ancestor_entry_time[child] > self.entry_times[curr_vertex]:
                    self.ans.append([curr_vertex, child])


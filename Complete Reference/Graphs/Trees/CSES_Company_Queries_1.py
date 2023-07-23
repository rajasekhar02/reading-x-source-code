import math
def solve(adjList, queries, n, q):
    max_levels = math.floor(math.log2(n)) + 1
    max_2_pow = math.floor(math.log2(max_levels)) + 1
    parents_at_2_pows = []
    for i in range(n):
        parents_at_2_pows.append([])
        # for j in range(max_2_pow):
        #     parents_at_2_pows[-1].append(0)
    print(max_levels, max_2_pow, len(parents_at_2_pows))
    for i in range(n-1, 0, -1):
        listParents = []
        curr_node = i
        for j in range(max_levels):
            if curr_node == 0:
                listParents.append(adjList[curr_node])
                break
            listParents.append(adjList[curr_node]-1)
            curr_node = adjList[curr_node]-1
        range_k = math.floor(math.log2(i))+1
        list_k_parents = []
        for k in range(0, range_k):
            kth_parent = 1<<k
            if kth_parent >= len(listParents):
                break
            list_k_parents.append(listParents[kth_parent-1])
        parents_at_2_pows[i] = list_k_parents


def main():
    [n,q] = list(map(int,input().split(" ")))
    adjList = list(map(int, ("1 "+input()).split(" ")))
    queries = []
    for i in range(0,q):
        query = list(map(int,input().split(" ")))
        queries.append(query)
    solve(adjList, queries, n, q)
if __name__ == "__main__":
    main()
    
import math


def solve1(adjList, queries, n, q):
    parents_at_2_pows = []
    for i in range(n):
        parents_at_2_pows.append([])
    print(len(parents_at_2_pows))
    for i in range(n - 1, 0, -1):
        """
        START
        This code block is calculating the all the parents for all the nodes
        if the tree is a unary tree or path:
            then the time complexity of this will be n
            and total time complexity will be n^2
            which results in time limit exceeded for the given constraints
        """
        listParents = []
        curr_node = i
        while True:
            if curr_node == 0:
                listParents.append(adjList[curr_node])
                break
            listParents.append(adjList[curr_node] - 1)
            curr_node = adjList[curr_node] - 1
        """
         END
        """
        # the below is for to store only parents which are at the distance pow 2's
        range_k = math.floor(math.log2(len(listParents))) + 1

        list_k_parents = []
        for k in range(0, range_k):
            kth_parent = 1 << k
            if kth_parent >= len(listParents):
                break
            list_k_parents.append(listParents[kth_parent - 1])
        parents_at_2_pows[i] = list_k_parents
    print(parents_at_2_pows)


def solve2(arr_immediate_parents, queries, n, q):
    global adj_list 
    adj_list= []
    for i in range(0, n + 1):
        adj_list.append([])
    adj_list[1] = [-1]
    for i in range(2, n + 1):
        adj_list[i].append(arr_immediate_parents[i - 2])
        adj_list[arr_immediate_parents[i - 2]].append(i)
    global parents_at_2_pows 
    parents_at_2_pows = []
    for i in range(0, n + 1):
        parents_at_2_pows.append([])
        for j in range(0, 20):
            parents_at_2_pows[-1].append(-1)
    fill_parents(1, -1)
    # print(parents_at_2_pows), adj_list, parents_at_2_pows
    ans = []
    for i in range(0, q):
        [node, parent_at] = queries[i]
        temp_parent_at = parent_at
        temp_node = node
        while True:
            found = False
            for i in range(19,-1, -1):
                if temp_parent_at & (1<<i) and parents_at_2_pows[temp_node][i] != -1:
                    found = True
                    temp_node = parents_at_2_pows[temp_node][i]
                    temp_parent_at = temp_parent_at - (1<<i)
                    break
            if not found:
                ans.append(-1)
                break
            if temp_parent_at == 0:
                ans.append(temp_node)
                break
            
                
    return ans                    
# adj_list, parents_at_2_pows
def fill_parents(node, parent_node):
    parents_at_2_pows[node][0] = parent_node
    for i in range(1, 20):
        if parents_at_2_pows[node][i - 1] == -1:
            break
        parents_at_2_pows[node][i] = parents_at_2_pows[parents_at_2_pows[node][i - 1]][
            i - 1
        ]

    for child in adj_list[node]:
        if child == parent_node:
            continue
        fill_parents(child, node)
# adj_list, parents_at_2_pows

def main():
    [n, q] = list(map(int, input().split(" ")))
    parentChildRelations = list(map(int, (input()).split(" ")))
    queries = []
    for i in range(0, q):
        query = list(map(int, input().split(" ")))
        queries.append(query)
    # solve(parentChildRelations, queries, n, q)
    # print(parentChildRelations)
    ans = solve2(parentChildRelations, queries, n, q)
    print("\n".join(map(str,ans)))

if __name__ == "__main__":
    main()

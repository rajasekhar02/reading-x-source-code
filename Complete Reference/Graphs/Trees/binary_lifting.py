"""
First I need to process the input and form a tree

"""
from typing import List, Dict


global time_in
global time_out
global max_levels
global adj_list
global ancestors


time_in: Dict[int, int]
time_out: Dict[int, int]
max_levels: int
adj_list: Dict[int, List[int]]
ancestors: Dict[int, List[int]]


def dfs(
    vertex: int,
    parent: int,
    timer: int,
):
    time_in[vertex] = timer + 1
    timer += 1
    ancestors[vertex][0] = parent
    for i in range(1, max_levels + 1):
        prev_parent = ancestors[vertex][i - 1]
        ancestors[vertex][i] = ancestors[prev_parent][i - 1]

    for i_child in adj_list[vertex]:
        if i_child != parent:
            dfs(
                i_child,
                vertex,
                timer,
            )
    time_out[vertex] = timer + 1
    timer += 1


def is_ancestor(vertex_u: int, vertex_v: int) -> bool:
    return (time_in[vertex_u] <= time_in[vertex_v]) and (
        time_out[vertex_u] >= time_out[vertex_v]
    )


def lca(vertex_u, vertex_v):
    if is_ancestor(vertex_u, vertex_v):
        return vertex_u

    if is_ancestor(vertex_v, vertex_u):
        return vertex_v

    for i in range(max_levels, -1, -1):
        """_logic intuition
        1: If the farthest node is not the ancestor then the nodes below that node cannot be a ancestor
         Eg:
            if ancestors[vertex_u][3] => 2^3 => 8th ancestor of vertex_u is not an ancestor of vextex_v
            then vertex_u is assigned to the 8th ancestor
        2:
        """
        if not is_ancestor(ancestors[vertex_u][i], vertex_v):
            vertex_u = ancestors[vertex_u][i]

    return ancestors[vertex_u][0]


if __name__ == "__main__":
    print("Binary Lifting")
    # define time_in: Dict[int, int]
    # define time_out: Dict[int, int]
    # define max_levels: int
    # define adj_list: Dict[int, List[int]]
    # define ancestors: Dict[int, List[int]]

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings = sorted(meetings,key=lambda x: (x[2], x[0],x[1]))
        meetingsGroupByTime = defaultdict(list);
        
        for aMeet in meetings:
            meetingsGroupByTime[aMeet[2]].append((aMeet[0], aMeet[1]))
        meetingsManager = DisjointSet(n);
        meetingsManager.union(0, firstPerson)
        for time in meetingsGroupByTime:
            meetingGroups = meetingsGroupByTime[time]
            for aGroup in meetingGroups:
                meetingsManager.union(aGroup[0], aGroup[1])
            
            for aGroup in meetingGroups:
                if not meetingsManager.connected(0, aGroup[0]) and not meetingsManager.connected(0, aGroup[1]):
                    meetingsManager.reset(aGroup[0])
                    meetingsManager.reset(aGroup[1])

        return [i for i in range(0, n) if meetingsManager.connected(0, i)]


class DisjointSet:
    """QuickFind Based Disjoint Set
    Disjoint set datastructure is optimized to find the root of a node quickly
        * Find Method to O(Height of Tree)
        * Union Method to O(Height of Tree)
        * Connected Method to O(Height of Tree)
    """

    def __init__(self, size):
        self.roots = [0] * size
        self.ranks = [0] * size
        # make each node root as itself initially
        for i in range(size):
            self.roots[i] = i
            self.ranks[i] = 1

    def findRoot(self, nodeX):
        """
        Using recursion and updating the child nodes intermediate root to main root

        Args:
            nodeX (int): nodeX
        """
        if self.roots[nodeX] == nodeX:
            return nodeX
        self.roots[nodeX] = self.findRoot(self.roots[nodeX])
        return self.roots[nodeX]

  

    def union(self, nodeX, nodeY):
        """
        In the union task,
            step 1: find the root of nodeX
            step 2: find the root ofnodeY
            step 3: If rootX == rootY: nothing to do
            step 4: if rootX != rootY: update the rootY to rootX (we are not updating all its child)
                    * Optimizing by maintaining a new array which indicates the rank (height of the tree)
                    * We always make the tree with larger height as the root
                    * if both the trees has same height then we increment the height and select rootX as the root for both the trees
        Args:
            nodeX (int): nodeX
            nodeY (int): nodeY
        """
        rootX = self.findRoot(nodeX)
        rootY = self.findRoot(nodeY)

        if rootX != rootY:
            if self.ranks[rootX] > self.ranks[rootY]:
                self.roots[rootY] = rootX
            elif self.ranks[rootX] < self.ranks[rootY]:
                self.roots[rootX] = rootY
            else:
                self.roots[rootY] = rootX
                self.ranks[rootX] += 1

    def connected(self, nodeX, nodeY):
        return self.findRoot(nodeX) == self.findRoot(nodeY)

    def reset(self, nodeY):
        self.roots[nodeY] = nodeY
        self.ranks[nodeY] = 0

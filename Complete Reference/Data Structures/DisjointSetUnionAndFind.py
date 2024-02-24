import unittest


class DisjointQuickUnionOptByRank:
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
        Need to iterate through the roots of nodes until we got a node which is root of itself

        Args:
            nodeX (int): a node

        Returns:
            int: root of the node
        """
        node = nodeX
        while self.roots[node] != node:
            node = self.roots[node]
        return node

    def findRootWithPathCompression(self, nodeX):
        """
        Using recursion and updating the child nodes intermediate root to main root

        Args:
            nodeX (int): nodeX
        """
        if self.roots[nodeX] == nodeX:
            return nodeX
        self.roots[nodeX] = self.findRootWithPathCompression(nodeX)
        return self.roots[nodeX]

    def findRootForDSQuickFind(self, nodeX):
        """
        As in the union method the root of a node is saved at the node position

        Args:
            nodeX (int): a node

        Returns:
            int: root of the node
        """
        return self.roots[nodeX]

    def unionForDSQuickFind(self, nodeX, nodeY):
        """
        In the union task,
            step 1: find the root of nodeX
            step 2: find the root ofnodeY
            step 3: If rootX == rootY: nothing to do
            step 4: if rootX != rootY: update the nodeY and its child to the rootX
        Args:
            nodeX (int): nodeX
            nodeY (int): nodeY
        """
        rootX = self.findRootForDSQuickFind(nodeX)
        rootY = self.findRootForDSQuickFind(nodeY)

        if rootX != rootY:
            totalNodeCnt = len(self.roots)
            for ithNode in range(totalNodeCnt):
                if self.roots[ithNode] == rootY:
                    self.roots[ithNode] = rootX

    def findRootForDSQuickUnion(self, nodeX):
        """
        Need to iterate through the roots of nodes until we got a node which is root of itself

        Args:
            nodeX (int): a node

        Returns:
            int: root of the node
        """
        node = nodeX
        while self.roots[node] != node:
            node = self.roots[node]
        return node

    def unionForDSQuickUnion(self, nodeX, nodeY):
        """
        In the union task,
            step 1: find the root of nodeX
            step 2: find the root ofnodeY
            step 3: If rootX == rootY: nothing to do
            step 4: if rootX != rootY: update the rootY to rootX (we are not updating all its child)
        Args:
            nodeX (int): nodeX
            nodeY (int): nodeY
        """
        rootX = self.findRootForDSQuickUnion(nodeX)
        rootY = self.findRootForDSQuickUnion(nodeY)

        if rootX != rootY:
            self.roots[rootY] = rootX

    def unionByRank(self, nodeX, nodeY):
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


class TestDisjoinQuickUnionOptByRank(unittest.TestCase):
    def setUp(self) -> None:
        self.uf = DisjointQuickUnionOptByRank(10)
        # 1-2-5-6-7 3-8-9 4
        self.uf.union(1, 2)
        self.uf.union(2, 5)
        self.uf.union(5, 6)
        self.uf.union(6, 7)
        self.uf.union(3, 8)
        self.uf.union(8, 9)

    def testConnectivityOfRootWithInternalNodeInSameTree(self):
        self.assertEqual(
            self.uf.connected(1, 5),
            True,
            "should true as there is a connectivity in 1-2-5-6-7 tree",
        )

    def testConnectivityOfInternalNodeWithLeafNodeInSameTree(self):
        self.assertEqual(
            self.uf.connected(5, 7),
            True,
            "should true as there is a connectivity in 1-2-5-6-7 tree",
        )

    def testConnectivityOfNodesInDifferentTrees(self):
        self.assertEqual(
            self.uf.connected(4, 9),
            False,
            "should False as 9(3-8-9-4 tree) and 4(4 tree) in two different sets",
        )

    def testUnionOfNodesInDifferentTrees(self):
        # 1-2-5-6-7 3-8-9-4
        self.uf.union(9, 4)
        self.assertEqual(
            self.uf.connected(4, 9),
            True,
            "should True as unioned 9(3-8-9-4 tree) and 4(4 tree) in two different sets",
        )

    def testUnionOfNodesInDifferentTreesToOne(self):
        # 1-2-5-6-7 3-8-9 => (1-2-5-6-7-3-8-9 or 1-2-5-6-7-9-8-3)
        self.uf.union(7, 9)
        self.assertEqual(
            self.uf.connected(7, 9),
            True,
            "should True as unioned 7(1-2-5-6-7 tree) and 9(3-8-9 tree) in two different sets",
        )


if __name__ == "__main__":
    unittest.main()

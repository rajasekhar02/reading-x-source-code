from collections import defaultdict


# index of strings ending at the given character,
class TrieNode:
    def __init__(self, char=""):
        self.child = [None] * 26
        self.endingStrCount = []
        self.char = char

    def __str__(self) -> str:
        return f"{self.char} {self.endingStrCount}"


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string, stringId):
        curr = self.root
        for i in string:
            childIndex = self.charToInt(i)
            # No Common Prefix
            if curr.child[childIndex] == None:
                curr.child[childIndex] = TrieNode(i)
            # Common Prefix
            curr = curr.child[childIndex]
        # Word Ending
        curr.endingStrCount.append(stringId)

    def insert2(self, string, stringId):
        ch = 0
        charInt = ord(string[ch]) - ord("a")
        prevNode = self.root
        tempNode = self.root.child[charInt]
        while tempNode != None and ch < len(string):
            charInt = ord(string[ch]) - ord("a")
            prevNode = tempNode
            tempNode = tempNode.child[charInt]
            ch += 1
        if ch == len(string):
            prevNode.endingStrCount.append(stringId)
            return
        while ch < len(string):
            charInt = ord(string[ch]) - ord("a")
            tempNode = TrieNode(string[ch])
            if ch == len(string) - 1:
                tempNode.endingStrCount.append(stringId)
            prevNode.child[charInt] = tempNode
            # prevNode.char = string[ch]
            prevNode = tempNode
            ch += 1

    def charToInt(self, char):
        return ord(char) - ord("a")

    def search(self, string) -> bool:
        curr = self.root
        for i in range(0, len(string)):
            ch = string[i]
            childIndex = self.charToInt(ch)
            # Non-Existent Word
            if curr.child[childIndex] == None:
                return False
            curr = curr.child[childIndex]

        # Word Exists as Substring
        if len(curr.endingStrCount) == 0:
            return False
        # String Found
        return True

    def delete(self, string):
        stack = []
        curr = self.root
        for i in range(0, len(string)):
            ch = string[i]
            childIndex = self.charToInt(ch)
            if curr.child[childIndex] == None:
                return
            stack.append(curr)
            curr = curr.child[childIndex]
        if len(curr.endingStrCount) == 0:
            return
        while len(stack) > 0:
            item = stack.pop()
            currChar = self.charToInt(curr.char)
            flag = 0
            for id, i in enumerate(item.child):
                if i is not None and id != currChar:
                    flag = 1
                    break
            item.child[currChar] = None
            if flag == 1:
                break
            curr = item

    def __str__(self) -> str:
        stack = [[0, self.root]]
        nodes = []
        while len(stack) > 0:
            level, item = stack.pop()
            nodes.append(f"{str(item).rjust(level*6,'-')}")
            for i in item.child:
                if i != None:
                    stack.append([level + 1, i])
        return "\n".join(nodes)


strings = [
    "aaaaaaaaaaaaaaaaaa",
    "ttttttttttteeeeeee",
    "aaaaaaaaaaaaaa",
    "aaaaaaaaaaaaaaaa",
    "tttttttttttttteeeeeeee",
    "iiiiiiiigggggggqqqqqqqq",
    "tttttttttteeeeeeeeeeeee",
    "iiiiiiiigggggqqqqqqqqqq",
    "iiiiiiiigggqqqqqqqqqqqq",
]

trie = Trie()
index = 0

# Insertion
for iStr in strings:
    trie.insert(iStr, index)
    index += 1

# Search
print(list(map(trie.search, ["three", "there"])))

# Deletion
print(trie.search("tttttttttteeeeeeeeeeeee"))
trie.delete("tttttttttttee")
print(trie.search("tttttttttteeeeeeeeeeeee"))
print(trie)

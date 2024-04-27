class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        ring_len = len(ring)
        key_len = len(key)
        
        # Find the minimum steps between two indexes of ring
        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)
        
        # HashMap to store the indices of occurrences 
        # of each character in the ring
        character_indicies = collections.defaultdict(list)
        for i, char in enumerate(ring):
            character_indicies[char].append(i)
        
        # Initialize the heap (priority queue) with the starting point
        # Each element of the heap is a tuple of integers representing:
        # totalSteps, ringIndex, keyIndex
        heap = [(0, 0, 0)]
        # tuple in seen: (ringIndex, keyIndex)
        seen = set()
        
        # Spell the keyword using the metal dial
        while heap:
            # Pop the element with the smallest total steps from the heap
            total_steps, ring_index, key_index = heapq.heappop(heap)

            # We have spelled the keyword
            if key_index == key_len:
                break

            # Continue if we have visited this character 
            # from this position in ring before
            if (ring_index, key_index) in seen:
                continue

            # Otherwise, add this pair to the visited list
            seen.add((ring_index, key_index))

            # Add the rest of the occurrences 
            # of this character in ring to the heap
            # Reason it works: This shortest path solution works because we always choose the next character with the shortest total steps, not the shortest next steps.
            for next_index in character_indicies[key[key_index]]:
                heapq.heappush(
                        heap, 
                        (total_steps + count_steps(ring_index, next_index),
                        next_index, key_index + 1))

        # Return the total steps and add keyLen to account for 
        # pressing the center button for each character in the keyword
        return total_steps + key_len
    def findRotateSteps1(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)
        curr = [inf for _ in range(ring_len)]
        prev = [0 for _ in range(ring_len)]

        # Find the minimum steps between two indexes of ring
        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        # For each occurrence of the character at keyIndex of key in ring
        # Stores minimum steps to the character from ring_index of ring
        for key_index in range(key_len - 1, -1, -1):
            curr = [inf for _ in range(ring_len)]
            for ring_index in range(ring_len):
                for character in range(ring_len):
                    if ring[character] == key[key_index]:
                        curr[ring_index] = min(curr[ring_index],
                                1 + count_steps(ring_index, character)
                                + prev[character])
            prev = curr.copy()

        return prev[0] 
    def findRotateSteps2(self, ring: str, key: str) -> int:
        dictRingCharInds = defaultdict(list)
        ringLen = len(ring)
        keyLen = len(key)
        dp = [[-1] * keyLen for i in range(ringLen)]
        for i in range(3):
            for j in range(len(ring)):
                dictRingCharInds[ring[j]].append(i*ringLen + j)
        newRing = ring + ring + ring
        def recurse(currPos, keyCharInd):
            if keyCharInd == keyLen:
                return 0
            if currPos < ringLen:
                currPos = currPos + ringLen
            if currPos >= ((ringLen << 1)):
                currPos = currPos - ringLen
            if dp[(currPos - ringLen)][keyCharInd] != -1:
                return dp[(currPos - ringLen)][keyCharInd]
            if newRing[currPos] == key[keyCharInd]:
                dp[(currPos - ringLen)][keyCharInd] = 1 + recurse(currPos, keyCharInd + 1)
                return dp[(currPos - ringLen)][keyCharInd]
            
            availPosInRing = dictRingCharInds[key[keyCharInd]]
            i = 0
            lenAvailPosInRing = len(availPosInRing)
            while i < lenAvailPosInRing:
                if currPos < availPosInRing[i]:
                    break
                i += 1
            # print(currPos, keyCharInd, key[keyCharInd], i, availPosInRing)
            if i == 0:
                dist = availPosInRing[i] - currPos
                dp[(currPos - ringLen)][keyCharInd] = 1 + dist + recurse(availPosInRing[i], keyCharInd + 1)
                return dp[(currPos - ringLen)][keyCharInd]
            if i == lenAvailPosInRing:
                dist = currPos - availPosInRing[i-1]
                dp[(currPos - ringLen)][keyCharInd] = 1 + dist + recurse(availPosInRing[i-1], keyCharInd + 1)
                return dp[(currPos - ringLen)][keyCharInd]
            dist1 = currPos - availPosInRing[i-1]
            dist2 = availPosInRing[i] - currPos
            dp[(currPos - ringLen)][keyCharInd] = 1 + min(
                recurse(availPosInRing[i-1], keyCharInd + 1) + dist1,
                recurse(availPosInRing[i], keyCharInd + 1) + dist2
                )
            return dp[(currPos - ringLen)][keyCharInd]

        currPos = ringLen

        return recurse(currPos, 0)

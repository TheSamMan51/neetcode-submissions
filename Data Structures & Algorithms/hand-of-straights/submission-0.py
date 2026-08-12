import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            while min_heap and count[min_heap[0]] == 0:
                heapq.heappop(min_heap)
            
            if not min_heap:
                break
            
            first = min_heap[0]

            for card in range(first, first + groupSize):
                if count[card] == 0:
                    return False
                count[card] -= 1

        return True
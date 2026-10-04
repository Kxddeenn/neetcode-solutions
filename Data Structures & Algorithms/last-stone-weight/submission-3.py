class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x < y:
                y = x - y 
                heapq.heappush(stones, y)

        stones.append(0) #edge cases where last two stones are the same weight
        return abs(stones[0])
        
        
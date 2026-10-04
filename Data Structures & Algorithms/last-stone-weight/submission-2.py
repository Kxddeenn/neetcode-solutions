class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # turns list into all -1
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if y > x:
                y = x - y
                heapq.heappush(stones, y)
            
        stones.append(0)
        return abs(stones[0])     
            
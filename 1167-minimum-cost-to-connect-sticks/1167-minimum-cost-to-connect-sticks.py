class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0
        
        heap = sticks
        heapq.heapify(heap)
        
        cost = 0
        while len(heap) > 1:
            smallest_stick1 = heapq.heappop(heap)
            smallest_stick2 = heapq.heappop(heap)
            
            cost = cost + smallest_stick1 + smallest_stick2
            heapq.heappush(heap, smallest_stick1 + smallest_stick2)
        
        return cost
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        pq = [(0,0)]
        for (start, end) in intervals:
            (soonest_available, _) = pq[0]
            
            if start >= soonest_available:
                heapq.heappushpop(pq, (end, start))
            else:
                heapq.heappush(pq, (end, start))
        
        return len(pq)
        
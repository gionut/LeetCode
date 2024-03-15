class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        print(intervals)
        pq = [(-1,-1)]
        for (start, end) in intervals:
            (soonest_available, _) = pq[0]
            
            if start >= soonest_available:
                heapq.heappushpop(pq, (end, start))
            else:
                heapq.heappush(pq, (end, start))
        
        return len(pq)
        
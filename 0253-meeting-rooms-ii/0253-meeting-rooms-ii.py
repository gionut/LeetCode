class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         sort
#         pq
#         foreach interval:
#             ends_soon = pq.peek()
#             if interval.end > ends_soon:
#                 pq.pop()
#                 pq.push(interval.end)
#             else:
#                 pq.push(interval.end)
                    
#         return len(hash)
# [[6,15],[6,17], [13,20],]
# [[1, 13], [13, 15]]



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
        
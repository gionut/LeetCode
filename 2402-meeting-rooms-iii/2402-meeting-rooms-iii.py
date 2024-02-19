# n=2 [[0,10],[1,5],[2,7],[3,4]]


# 0, (0, 10) -- 10, (3,4)+(10-3) 
# 1, (1, 5) -- 5, (2,7) -- 10

# availability_time = [0] * n
# * sort meetings by start time
# * for meeting meetings
#     assign meeting to earliest available room -- min heap
#     update room meeting count
#     update room availability
#         availability = room.availability + (meeting.end - meeting.start)
# return max(room meeting count)

# 4
# [[18,19],[3,12],[17,19],[2,13],[7,10]]

# [[2, 13], [3, 12], [7, 10], [17, 19], [18, 19]]

# 0: [2, 13] --
# 1: [3, 12]
# 2: [7, 10], [18, 19]
# 3: [17, 19]
    
#     (12, 1)
#     (13, 0)
#     (19, 2)
#     (19, 3)
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meeting_count = [0] * n
        schedule = []
        free_rooms = [(0, i) for i in range(n)]
        heapq.heapify(free_rooms)
        meetings = sorted(meetings, key=lambda x: x[0])
        # print(meetings)
        for meeting in meetings:
            while len(schedule) > 0 and schedule[0][0] <= meeting[0]:
                (_, room) = heapq.heappop(schedule)
                heapq.heappush(free_rooms, (0, room))
            
            if len(free_rooms) > 0:
                (availability, room) = heapq.heappop(free_rooms)
            else:
                (availability, room) = heapq.heappop(schedule)
                
            meeting_count[room] += 1
            heapq.heappush(schedule, (max(availability, meeting[0]) + (meeting[1] - meeting[0]), room))
        
        return meeting_count.index(max(meeting_count))
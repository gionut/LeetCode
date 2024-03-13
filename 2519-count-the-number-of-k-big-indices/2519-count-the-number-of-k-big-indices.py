# [0, 1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17]
# [4, 11, 14, 18, 16, 10, 15, 6,  2,  6,  9,  16, 6,  18, 5,  16, 3,  6]
# [2, 4, 6
# []
# [0, 0,  0,  1,  1,  0,  1,  0,  0,  0,  1,  1,  0,  1,  0,  1,  0,  1]
class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        k_big = [0] * len(nums)
        heap = []
        for i in range(len(nums)):
            # if the kth element in the queue is less than the current element
            # print(heap,nums[i])
            if len(heap) == k and -1*heap[0] < nums[i]:
                # print("true")
                k_big[i] += 1
            if len(heap) < k:
                heapq.heappush(heap, -1*nums[i])
            else:
                heapq.heappushpop(heap, -1*nums[i])
                
        # print(k_big)
        heap = []
        for i in range(len(nums)-1,-1,-1):
            # print(heap,nums[i])
            if len(heap) == k and -1*heap[0] < nums[i]:
                # print("true")
                k_big[i] += 1
            if len(heap) < k:
                heapq.heappush(heap, -1*nums[i])
            else:
                heapq.heappushpop(heap, -1*nums[i])
        # print(k_big)
        
        result = 0
        for i in k_big:
            if i == 2:
                result += 1
                
        return result
# if len(array) < 2:
#     return 0
# check the ends:
#     if equal:
#         return recurse for the array without the ends
#     else:
#         return min(
#             1 + recurse with left merged array,
#             1 + recurse with right merged array
#         )

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # @lru_cache(maxsize=2**16)
        def minOps(start, end, start_idx, end_idx):
            if end_idx - start_idx < 1:
                return 0
            
            if start < end:
                return 1 + minOps(start+nums[start_idx+1], end, start_idx+1, end_idx)
            
            elif end < start:
                return 1 + minOps(start, end+nums[end_idx-1], start_idx, end_idx-1)
            else:
                return minOps(nums[start_idx+1], nums[end_idx-1], start_idx+1, end_idx-1)

        return minOps(nums[0], nums[-1], 0, len(nums)-1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.LEFT = -1
        self.RIGHT = 1
        self.sortedArray = nums
        self.target = target
        
        def binarySearch(direction):
            leftmost, rightmost = 0, len(self.sortedArray)-1
            position = -1
            
            while leftmost <= rightmost:
                middle = (leftmost + rightmost) // 2
                if self.target > self.sortedArray[middle]: leftmost = middle + 1
                elif self.target < self.sortedArray[middle]: rightmost = middle - 1
                else:
                    position = middle
                    
                    if direction == self.LEFT:
                        rightmost = middle - 1
                    elif direction == self.RIGHT:
                        leftmost = middle + 1
            
            return position
        
        return [binarySearch(self.LEFT), binarySearch(self.RIGHT)]
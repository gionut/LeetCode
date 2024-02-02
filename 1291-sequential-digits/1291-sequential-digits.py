class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # count digits of low
        length = 0
        temp = low
        while temp != 0:
            temp //= 10
            length += 1

        idx = low // 10**(length-1) -1
        
        nr = 123456789
        result = []
        for i in range(100):
            while idx + length <= 9:
                cutRight = 10 ** (9 - (idx + length))
                cutLeft = 10 ** length
                computed = nr // cutRight % cutLeft
                
                if computed > high:
                    return result
                if computed >= low and computed <= high:
                    result.append(computed)
                idx += 1
            
            idx = 0
            length += 1
            
        return result
        
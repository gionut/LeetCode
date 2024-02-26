class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        crt_partition = 0
        for c in s:
            c_bin = 1 << (ord(c)-ord('a'))
            if  c_bin | crt_partition != crt_partition:
                crt_partition = c_bin | crt_partition
            else:
                crt_partition = c_bin
                count += 1
                
        return count
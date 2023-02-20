class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        double_s = s + s
        i = 0
        while i < len(s):
            print(double_s[i:i+len(s)])
            if double_s[i:i+len(s)] == goal:
                return True
            i += 1
        return False
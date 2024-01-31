class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        max_temp = temperatures[-1] 
        
        for i in range(len(temperatures)-1 , -1, -1):
            crr_temp = temperatures[i]
            
            if crr_temp >= max_temp:
                max_temp = crr_temp
                result[i] = 0
                
            else:
                days_forward = 1
                while crr_temp >= temperatures[i + days_forward]:
                    days_forward += result[i + days_forward] 
                    
                result[i] = days_forward
        
        return result
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        
        finished = {}
        for i in range(numCourses):
            finished[i] = False
        
        prereq = {}
        for i in range(numCourses):
            prereq[i] = []
        for (course, prerequisite) in prerequisites:
            prereq[course].append(prerequisite)
        
        for course in range(numCourses):
            if finished[course] == False:
                stack = [course]
                prerequisiteChain = [False] * numCourses
                while len(stack) > 0:
                    c = stack[-1]
                    if finished[c] == True:
                        stack.pop()
                    elif prerequisiteChain[c] == True:
                        stack.pop()
                        finished[c] = True
                        result.append(c)
                        prerequisiteChain[c] = False
                    else:
                        prerequisiteChain[c] = True
                        for p in prereq[c]:
                            if prerequisiteChain[p] == True:
                                return []
                            if finished[p] == False:
                                stack.append(p)
                        
                            
        return result
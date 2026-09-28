class Solution(object):
    def findMaxAverage(self, nums, k):
        p1 = 0
        p2 = k
        result = 0
        summ = 0
        while p2 != len(nums)+1:
            summ = float(sum(nums[p1:p2]))/k
            if summ>result:
                result = summ
            p1+=1
            p2+=1  
        return result    
        

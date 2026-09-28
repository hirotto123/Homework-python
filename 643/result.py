class Solution(object):
    def findMaxAverage(self, nums, k):
        p1=0
        p2=k
        summ=float(sum(nums[p1:p2]))
        result=summ
        while p2!=len(nums):
            summ=summ-nums[p1]+nums[p2]
            p1+=1
            p2+=1
            if summ>result:
                result=summ
        return result/k

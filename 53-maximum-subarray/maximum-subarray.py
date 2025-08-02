class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = global_max = nums[0]
        for i in range(1,len(nums)):
            curr_sum = max(nums[i],curr_sum + nums[i])
            global_max = max(global_max, curr_sum)
        return global_max
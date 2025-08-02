class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_hash = {}
        for i,val in enumerate(nums):
            complement = target - val
            if complement in my_hash:
                return [my_hash[complement], i]
            my_hash[val] = i

        
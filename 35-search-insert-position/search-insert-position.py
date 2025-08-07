class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = int((low+high)/2)
            if (nums[mid] == target):
                
                return mid
                break
            elif (target < nums[mid]):
                high = mid-1
            else:
                low = mid +1
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

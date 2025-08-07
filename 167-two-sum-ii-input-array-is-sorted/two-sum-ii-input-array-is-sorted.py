class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) -1
        my_sum = 0
        while left < right:
            my_sum = numbers[left] + numbers[right]
            if my_sum == target:
                return [left+1,right+1]
                break
            elif my_sum < target:
                left += 1
            else:
                right -= 1
        